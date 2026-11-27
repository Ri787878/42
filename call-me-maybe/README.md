*This project has been created as part of the 42 curriculum by ridias.*

# Call Me Maybe

## Description
### Algorithm explanation:
My constrained decoding strategy for this project was for the program to builds a prompt from the user's request and the available function definitions. The tokenizer then turns the prompt into tokens, and the model produces scores (logits) for the next token. After that BasicJsonFSM, which is a finite state machine, checks which next tokens keep the response within its supported JSON structure. It tracks states such as expecting a key, a value, a string escape, or a closing brace. It can check tokens character by character, including tokens that contain multiple characters.

Then select_json_token() chooses the highest-scoring allowed token. It tries promising candidates first and falls back to checking the full allowed-token set when needed. The selected token is appended to the input, and generation repeats until the JSON is complete or the token limit is reached.
The program decodes the generated tokens and validates the call against the function definitions. Invalid calls can be retried.

Although the BasicJsonFSM helps enforce format, it doesn't guarantee the model chose the right function or understood the request correctly. Those require validation and good function descriptions. So it just guarentees it return a vaild generated JSON.

### Design decisions:
To utilize the local model I use the llm_sdk as the middleman that allows me to ecode and decode the messages between generations. For performance sake it is utilized one model instance per run, meaning the same loaded model is reused for every prompt in the input batch. For guarenteeing a JSON complient output file a JSON state machine is used this prevents invalid JSON tokens being added to the response during generation, rather than relying only on fixing malformed output afterward. For selecting tokens a Greedy selection is used, that means the decoder chooses the highest-scoring allowed token instead of sampling. This is straightforward and generally repeatable, though it doesn't explore alternatives. The available functions are described outside the generation code, so the model can be given different tool definitions. For validation and retries, generated arguments are checked before being written to the output and retries give the model another chance after a validation error. As a default the model has 3 retries of 50 tokens each to achieve a valid response, although it could be altered at the file values.py.

### Performance analysis:
The model achieves a success probability of above 90% although the precise number is hard to define without hundreds of retries. in regards to time it takes roughly 2.58 to 3.4 minutes for it to generate a response for 11 prompts. The model load speed is around 1.6 to 1.9 seconds, although the first load is always the longest at around 44 seconds.
It is worth mentioning that performances and results may vary depending on function-definitions complexity and size, aswell as number of prompts given.
These numbers are tested on 42 Lisbon computers.

### Challenges faced:
While developing this project many issues arose, the main one was how to get the program to provide a valid output under the time constraints of 5 minutes. To solve this problm I simplefied the way I was selecting each next token for the algorithm.
Another big problem that came up was understading what and how a llm actually does, this question answered it self after asking many diferent students and many google queries aswell as some help with Artificial Inteligence.

### Testing strategy:
To test this project I rellied much on the provided examples and even creating a few of my own, with diferent types of prompts and queries to ask of it. The only part I didnt create much was new functions to test the model on.

I also used timestamps to help me ensure my model loading speeds, generation loop speeds, single call speeds and token selection speeds were correct on the schools computers being weaker than my own. The time stamps show the time it took to load the model, the time of generating the new information (each call generation time/token selection) and the time it takes for each of the prompts to load. Finally it also show the time it took to run the whole project.

### Example usage:
Simple utilization usinng provided tests and function definitions:
```
$ make run
uv run python -m src
Model loading took 2.87s
[SYSTEM] Function_Definitions File Exist.
[SYSTEM] Input File Exist.

[SYSTEM] Output File Created.
Prompt: 185 tokens; generated: 21 tokens; model: 13.73s; token selection: 0.51s
Function generation took 14.24s
Prompt: 189 tokens; generated: 25 tokens; model: 16.84s; token selection: 0.53s
Function generation took 17.37s
Prompt: 179 tokens; generated: 14 tokens; model: 8.67s; token selection: 0.05s
Function generation took 8.72s
Prompt: 178 tokens; generated: 13 tokens; model: 8.51s; token selection: 0.05s
Function generation took 8.56s
Prompt: 180 tokens; generated: 13 tokens; model: 8.61s; token selection: 0.53s
Function generation took 9.13s
Prompt: 180 tokens; generated: 13 tokens; model: 8.39s; token selection: 0.53s
Function generation took 8.92s
Prompt: 184 tokens; generated: 17 tokens; model: 11.44s; token selection: 0.07s
Function generation took 11.50s
Prompt: 184 tokens; generated: 18 tokens; model: 12.09s; token selection: 0.07s
Function generation took 12.16s
Prompt: 196 tokens; generated: 39 tokens; model: 28.77s; token selection: 0.66s
Function generation took 29.43s
Prompt: 187 tokens; generated: 34 tokens; model: 26.01s; token selection: 0.63s
Function generation took 26.64s
Prompt: 197 tokens; generated: 35 tokens; model: 25.89s; token selection: 0.64s
Function generation took 26.53s
Total generation took 173.23s
--- 176.69915390014648 seconds ---
```
Note: the model is already loaded on this test.

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
make run 
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
- https://www.kunwar.page/chapter/043-structured-generation-guided-decoding-json-mode-regex-constraints-fsm-masking
- https://en.wikipedia.org/wiki/Softmax_function
- https://numpy.org/doc/stable/reference/generated/numpy.argmax.html


The use of AI was used for better understanding the logit behind an llm, improving functions for more clarity, and to format the ReadMe.
