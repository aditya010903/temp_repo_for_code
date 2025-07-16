# building a simple tokenizer from scratch using the text data avaialble in the file the-verdict.txt .

import re 
with open('pythonBasics\\AI-Basics\\LLMFromScratch\\the-verdict.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

preprocessed = re.split(r"(\b'\b|[,.;:?_!\"()--]|\s)" , raw_data) # this will split the text from the book into words and punctuations.
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_words = sorted(set(preprocessed))
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"]) # adding the end of text token and unknown token to the list of tokens to handle unknown exceptions.
vocab = {token : integer for integer , token in enumerate(all_tokens)}
print(len(vocab.items()))
for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)

# creating a tokenizer class that accepts the text given to it and encodes it into tokens and then show the token to the user
# this class will also have a decode method that will convert the tokens into text.

class MyTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r"(\b'\b|[,.;:?_!\"()--]|\s)", text) # this will split the text given to the tokenizer into words and punctuations.
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = ["<|unk|>" if item not in self.str_to_int else item for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!\"()\\\'])', r'\1', text) # this will remove the extra spaces before the punctuations.
        return text

tokenizer = MyTokenizerV1(vocab)
text ='''It's the last he painted, you know, hello"   
Mrs. Gisburn said with pardonable pride.'''
# NOTE : in this piece of text, 'hello' isnt available in the vocabulary of the tokenizer. But since we have handled this case, it wont throw any error
ids = tokenizer.encode(text)
print(ids)

decoded_text = tokenizer.decode(ids)
print(decoded_text)

# this was the code for the tokenizer class that we have created from scratch.