*This project has been created as part of the 42 curriculum by ridias.*

# Call Me Maybe

## Description
• Algorithm explanation: Describe your constrained decoding approach in detail

• Design decisions: Explain key choices in your implementation
• Performance analysis: Discuss accuracy, speed, and reliability of your solution
• Challenges faced: Document difficulties encountered and how you solved them
• Testing strategy: Describe how you validated your implementation
• Example usage: Provide clear examples of running your program


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
