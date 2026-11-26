*This project has been created as part of the 42 curriculum by ridias.*

# Call Me Maybe

## Description
### Algorithm explanation: Describe your constrained decoding approach in detail
My constrained decoding strategy for this project was for the program to builds a prompt from the user’s request and the available function definitions. The tokenizer then turns the prompt into tokens, and the model produces scores (logits) for the next token. After that BasicJsonFSM, which is a finite state machine, checks which next tokens keep the response within its supported JSON structure. It tracks states such as expecting a key, a value, a string escape, or a closing brace. It can check tokens character by character, including tokens that contain multiple characters. Then select_json_token() chooses the highest-scoring allowed token. It tries promising candidates first and falls back to checking the full allowed-token set when needed. The selected token is appended to the input, and generation repeats until the JSON is complete or the token limit is reached.
The program decodes the generated tokens and validates the call against the function definitions. Invalid calls can be retried.

Although the BasicJsonFSM helps enforce format, it doesn’t guarantee the model chose the right function or understood the request correctly. Those require validation and good function descriptions. So it just guarentees it return a vaild generated JSON.

### Design decisions: Explain key choices in your implementation
To utilize the local model I use the llm_sdk as the middleman that allows me to ecode and decode the messages between generations. For performance sake it is utilized one model instance per run, meaning the same loaded model is reused for every prompt in the input batch. For guarenteeing a JSON complient output file a JSON state machine is used this prevents invalid JSON tokens being added to the response during generation, rather than relying only on fixing malformed output afterward. For selecting tokens a Greedy selection is used, that means the decoder chooses the highest-scoring allowed token instead of sampling. This is straightforward and generally repeatable, though it doesn’t explore alternatives. The available functions are described outside the generation code, so the model can be given different tool definitions. For validation and retries, generated arguments are checked before being written to the output and retries give the model another chance after a validation error. As a default the model has 3 retries of 50 tokens each to achieve a valid response, although it could be altered at the file values.py.

### Performance analysis: Discuss accuracy, speed, and reliability of your solution
The model achieves a success probability of above 90% although the precise number is hard to define without hundreds of retries. in regards to time it takes roughly 2.58 to 2.62 minutes for it to generate a response for 11 prompts. The model load speed is around 1.6 to 1.9 seconds, although the first load is always the longest at around 44 seconds.
It is worth mentioning that performances and results may vary depending on function-definitions complexity and size, aswell as number of prompts given.
These numbers are tested on 42 Lisbon computers.

### Challenges faced: Document difficulties encountered and how you solved them
Describe actual problems and what you learned from them. Examples from this project include:

    Ambiguous or unsupported prompts: a request may not correspond to any defined function. The system needs to handle that explicitly rather than assuming every prompt has a valid call.
    Syntax versus meaning: a regex can compile and still match the wrong text. Your vowel and cat examples demonstrate why syntax/type validation alone doesn’t ensure semantic correctness.
    Giving the model enough context: function names and parameter types may not explain how to choose values. Function and parameter descriptions should be included in the generation prompt.
    Retries and failure messages: retry limits should come from the project’s configuration, and exhausted retries should produce a useful explanation rather than an opaque exception.

### Testing strategy: Describe how you validated your implementation
Explain what you ran and what it checked. A good strategy for this project includes:

    Decoder tests: allowed and rejected token transitions, strings and escapes, numbers, and completion of the JSON object.
    Call-validation tests: unknown function names, missing parameters, incorrect value types, and invalid generated JSON.
    Meaning-focused tests: apply substitution patterns to their source strings and check the resulting text—not just whether the patterns compile.
    End-to-end tests: run the prompts in your input file and compare function names and parameters with expected calls.
    Performance checks: record model-load, inference, token-selection, and total time, along with the hardware and model used.

### Example usage: Provide clear examples of running your program


## Instructions
### To setup on 42 school computers
To get around the space constraints you need to direct the cache to be stored on sgoingfre, so run the following cmds to direct their install locations.

```bash
export UV_CACHE_DIR="/sgoinfre/$USER/uv-cache"
export UV_PROJECT_ENVIRONMENT="/sgoinfre/$USER/call-sub-venv"
export HF_HOME="/sgoinfre/$USER/huggingface"
```

### Execute the code
To execute the code you need to run the following commands:
```bash
uv sync
uv run 
```
Note - the uv run already runs the cmd for installing the project.

###
For a more custom approach, there is a way to set each inputted file manually:
```
uv run python -m src [--functions_definition <function_definition_file>] [--input <input_file>] [--output <output_file>]
```
## Resources

- https://www.geeksforgeeks.org/python/read-json-file-using-python/
- https://www.w3schools.com/python/python_dictionaries_access.asp
- https://telnyx.com/learn-ai/logits-ai
- https://medium.com/@c.savur/mastering-the-logits-a-guide-to-constrained-decoding-in-hugging-face-and-vllm-357a5c1b9a28



“Constrained decoding for JSON generation”
“Logit masking token-by-token decoding”
“Finite state machine JSON parser generation”
“Regex / CFG / DFA constrained text generation LLM”
“Function calling schema enforcement LLM”
“Argument extraction from natural language to structured JSON”
“Deterministic fallback for tool calling”
“Validation and repair loop for LLM structured outputs”
“Tokenizer BPE token boundaries JSON generation pitfalls”
“Evaluation metrics for tool selection and argument accuracy”


## FIX ERROR WHEN INPUTTING A OUTPUT FILE AND ONLY A FILE NAME IS GIVEN

check ambiguous prompts
