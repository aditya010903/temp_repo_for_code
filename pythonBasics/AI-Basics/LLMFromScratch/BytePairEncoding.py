import tiktoken 

with open('pythonBasics\\AI-Basics\\LLMFromScratch\\the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

encoder = tiktoken.get_encoding("gpt2")
encoded_data = encoder.encode(raw_data)
print(encoded_data)



