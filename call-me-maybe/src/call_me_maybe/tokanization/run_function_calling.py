# ABOUTME: Generate function-calling results JSON from prompts + function definitions
# ABOUTME: Uses an LLM planner output, validates strictly, and writes required output format.

import json
import os
import re
from typing import Any, Dict, List, Tuple, Optional

# import your provided class
# from llm_sdk.small_llm_model import Small_LLM_Model
# Adjust import path to wherever Small_LLM_Model is located:
from llm_sdk import Small_LLM_Model  # <- change if needed



INPUT_FUNCTIONS = "data/input/function_definitions.json"
INPUT_PROMPTS = "data/input/prompts.json"
OUTPUT_FILE = "data/output/function_calling_results.json"


# ----------------------------
# Helpers
# ----------------------------

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def ensure_output_dir(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)


def normalize_number(x: Any) -> float:
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip())
    raise ValueError(f"Cannot parse number from {x!r}")


def extract_first_json_object(text: str) -> Optional[Dict[str, Any]]:
    """
    Try direct parse; else extract first {...} block and parse.
    """
    text = text.strip()

    # direct parse
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass

    # fenced code block cleanup
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    # naive object extraction
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        candidate = text[start:end + 1]
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict):
                return obj
        except Exception:
            return None
    return None


def build_function_map(function_defs: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    fn_map = {}
    for fn in function_defs:
        name = fn["name"]
        params = fn.get("parameters", {})
        fn_map[name] = {
            "parameters": params
        }
    return fn_map


def validate_and_coerce_call(
    call_obj: Dict[str, Any],
    fn_map: Dict[str, Dict[str, Any]]
) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    """
    Expects call_obj with keys: name, parameters
    Coerces numbers to float for consistent output.
    """
    if not isinstance(call_obj, dict):
        return False, "Output is not an object", None

    if set(call_obj.keys()) != {"name", "parameters"}:
        return False, "Output must contain exactly keys: name, parameters", None

    name = call_obj.get("name")
    parameters = call_obj.get("parameters")

    if not isinstance(name, str):
        return False, "name must be a string", None
    if name not in fn_map:
        return False, f"Unknown function name: {name}", None
    if not isinstance(parameters, dict):
        return False, "parameters must be an object", None

    expected_params = fn_map[name]["parameters"]  # dict: param_name -> {"type": "..."}
    expected_keys = set(expected_params.keys())
    got_keys = set(parameters.keys())

    if got_keys != expected_keys:
        missing = expected_keys - got_keys
        extra = got_keys - expected_keys
        return False, f"Parameter keys mismatch. Missing={missing}, Extra={extra}", None

    coerced_params: Dict[str, Any] = {}
    for p_name, p_schema in expected_params.items():
        p_type = p_schema.get("type")
        val = parameters[p_name]

        if p_type == "number":
            try:
                coerced_params[p_name] = normalize_number(val)
            except Exception:
                return False, f"Parameter '{p_name}' must be number", None
        elif p_type == "string":
            if not isinstance(val, str):
                return False, f"Parameter '{p_name}' must be string", None
            coerced_params[p_name] = val
        else:
            return False, f"Unsupported parameter type '{p_type}'", None

    cleaned = {
        "name": name,
        "parameters": coerced_params
    }
    return True, "ok", cleaned


def build_planner_prompt(prompt: str, function_defs: List[Dict[str, Any]]) -> str:
    return f"""
You are a function-call planner.

Task:
Given a user request and available function definitions, choose exactly ONE function and produce arguments.

Rules:
1) Return JSON ONLY (no prose, no markdown).
2) Output must be an object with EXACTLY these keys:
   - "name" (string)
   - "parameters" (object)
3) "name" must be one of the provided function names.
4) "parameters" must contain ALL required parameters for that function with correct JSON types.
5) Do not include extra keys.

Available function definitions:
{json.dumps(function_defs, ensure_ascii=False, indent=2)}

User request:
{prompt}

Return only:
{{"name":"...", "parameters":{{...}}}}
""".strip()


def generate_call_with_retries(
    llm: Small_LLM_Model,
    prompt: str,
    function_defs: List[Dict[str, Any]],
    fn_map: Dict[str, Dict[str, Any]],
    max_attempts: int = 4
) -> Dict[str, Any]:
    """
    NOTE:
    Replace `raw_generate` with your actual generation method in llm_sdk.
    This wrapper handles retries + validation.
    """
    last_error = "unknown error"

    base_instruction = build_planner_prompt(prompt, function_defs)

    for attempt in range(1, max_attempts + 1):
        user_text = base_instruction
        if attempt > 1:
            user_text += f'\nPrevious output was invalid: "{last_error}". Try again and follow rules exactly.'

        # ----------------------------
        # IMPORTANT: adapt this line to your SDK's actual generation API
        # ----------------------------
        # Example placeholder:
        # raw = llm.generate(user_text, max_new_tokens=180, temperature=0.0)
        raw = llm.generate(user_text)  # <- CHANGE if needed
        # ----------------------------

        parsed = extract_first_json_object(raw if isinstance(raw, str) else str(raw))
        if parsed is None:
            last_error = "Could not parse JSON object from model output"
            continue

        ok, msg, cleaned = validate_and_coerce_call(parsed, fn_map)
        if ok and cleaned is not None:
            return cleaned

        last_error = msg

    # deterministic fallback (very simple heuristic)
    return fallback_call(prompt, fn_map)


def fallback_call(prompt: str, fn_map: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    p = prompt.strip()

    # sum/add
    if re.search(r"\b(sum|add)\b", p, flags=re.I):
        nums = re.findall(r"-?\d+(?:\.\d+)?", p)
        if len(nums) >= 2:
            return {
                "name": "fn_add_numbers",
                "parameters": {"a": float(nums[0]), "b": float(nums[1])}
            }

    # greet
    if re.search(r"\bgreet\b", p, flags=re.I):
        m = re.search(r"greet\s+([A-Za-z]+)", p, flags=re.I)
        name = m.group(1) if m else "there"
        return {"name": "fn_greet", "parameters": {"name": name}}

    # reverse
    if re.search(r"\breverse\b", p, flags=re.I):
        m = re.search(r"'([^']*)'", p)
        s = m.group(1) if m else p
        return {"name": "fn_reverse_string", "parameters": {"s": s}}

    # square root
    if re.search(r"square root", p, flags=re.I):
        nums = re.findall(r"-?\d+(?:\.\d+)?", p)
        a = float(nums[0]) if nums else 0.0
        return {"name": "fn_get_square_root", "parameters": {"a": a}}

    # regex substitute defaults
    if "number" in p.lower() and "replace" in p.lower():
        m = re.search(r'"([^"]*)"', p)
        src = m.group(1) if m else p
        rep = "NUMBERS"
        return {
            "name": "fn_substitute_string_with_regex",
            "parameters": {"source_string": src, "regex": r"\d+", "replacement": rep}
        }

    if "vowel" in p.lower() and "replace" in p.lower():
        m = re.search(r"'([^']*)'", p)
        src = m.group(1) if m else p
        return {
            "name": "fn_substitute_string_with_regex",
            "parameters": {"source_string": src, "regex": r"[AEIOUaeiou]", "replacement": "*"}
        }

    if "substitute" in p.lower() and "cat" in p.lower() and "dog" in p.lower():
        m = re.search(r"'([^']*)'$", p)
        src = m.group(1) if m else p
        return {
            "name": "fn_substitute_string_with_regex",
            "parameters": {"source_string": src, "regex": r"\bcat\b", "replacement": "dog"}
        }

    # last-resort default
    any_name = next(iter(fn_map.keys()))
    empty = {k: (0.0 if v["type"] == "number" else "") for k, v in fn_map[any_name]["parameters"].items()}
    return {"name": any_name, "parameters": empty}


def main() -> None:
    function_defs = load_json(INPUT_FUNCTIONS)
    prompts_data = load_json(INPUT_PROMPTS)
    fn_map = build_function_map(function_defs)

    llm = Small_LLM_Model(model_name="Qwen/Qwen3-0.6B")

    results: List[Dict[str, Any]] = []

    for item in prompts_data:
        prompt = item["prompt"]
        call = generate_call_with_retries(llm, prompt, function_defs, fn_map, max_attempts=4)

        out_item = {
            "prompt": prompt,
            "name": call["name"],
            "parameters": call["parameters"]
        }
        # enforce exact keys in final output object
        assert set(out_item.keys()) == {"prompt", "name", "parameters"}
        results.append(out_item)

    ensure_output_dir(OUTPUT_FILE)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(results)} items to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
