# ChatGPTDevFriendly


This package can be used by developers to quickly develop ChatGPT applications with the robustness 
and boilerplate code being taken care of by this wrapper.

## Requirements 
`pip install openai`

## Usage 

```python
chatgpt_client = ChatGptSmartClient(api_key, model_name)
# We can query with some previous context and also decide whether to add a prompts answer to the context
prompt="List the top 10 upcoming startups in India?"
rsp = chatgpt_client.query(prompt, w_context=True, add_to_context=True)
print(f"The answer from ChatGPT is {rsp}")

# We build on previous context but do not add the current prompts answer to context
prompt="Ok thanks, can you give me the valuation of these startups in tabular format"
rsp  = chatgpt_client.query(prompt, w_context=True, add_to_context=False)
...

```

## Features
We currently have the features of
- Retries: This is incase of failures like connection based request exceptions, API errors. 
- Erasing Context: We can erase all previous chat history to star from fresh.
- Embeddings: We can get the query embeddings and cache them for further use. (In developement)
- Rollback: we can rollback to a particular Chat to an restart from there.(In development)

## Contributions

This project is meant to make the chatgpt developer life easy, so please do add any featues you feel is needed! Also if you fnd it useful please leave a star!! 
