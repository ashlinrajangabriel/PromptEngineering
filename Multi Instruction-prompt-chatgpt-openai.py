
import openai
import os


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


text = f"""
In a charming village, siblings Jack and Jill set out on \ 
a quest to fetch water from a hilltop \ 
well. As they climbed, singing joyfully, misfortune \ 
struck—Jack tripped on a stone and tumbled \ 
down the hill, with Jill following suit. \ 
Though slightly battered, the pair returned home to \ 
comforting embraces. Despite the mishap, \ 
their adventurous spirits remained undimmed, and they \ 
continued exploring with delight.
"""
# example 1
prompt_1 = f"""
Perform the following actions: 
step 1 - Segment sentences ,Tokenize the sentences, Lemmatize the words and remove conjunctions.
step 2 - from the step 1 tokens generate embedding .
step 3 - For each of the sentences identify positive,negative,neutral sentiments.
step 4 - Assign relevant Topic name for each sentences not more than 4 topics.

step 5 - add three similar sentences for each current sentence and similarity score
step 6 - Output a json object that contains the following \
keys: sentence, tokens and embeddings, sentiments,similar sentence,score,Topic name .
Separate your answers with line breaks.

Text:
```{text}```
"""
response = get_completion(prompt_1)
print("Completion for prompt 1:")
print(response)
