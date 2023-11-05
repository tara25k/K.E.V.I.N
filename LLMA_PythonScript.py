import openai

openai.api_base = "http://llama.qrt.services:8000/v1" # point to the local server
openai.api_key = ""  # Provide your actual API key

#user_input = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice “without pictures or conversations?”, So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, “Oh dear! Oh dear! I shall be late!” (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge."


# Open the text file for reading
with open('sampleStory.txt', 'r',encoding='utf-8') as file:
    # Read the contents of the file into a variable
    user_input = file.read()

# Now, the 'text' variable contains the contents of the file

completion = openai.ChatCompletion.create(
  model="local-model",  # this field is currently unused
  messages=[
    #current issue here -> I said 100 words, it output response of 103 
    {"role": "system", "content": "Summarize this text in less than 100 words"},
    {"role": "user", "content": user_input}
  ],

  #refers to entropy (proxy for creativity, lack of predictability)
  #if we want consistent answers (the same summary produced each time) --> temperature = 0 
  #parameters for temperature is less than or equal to 2 aka x <2
  temperature=0.2,  
  #max_tokens controls the max num of tokens to generate in the completion
  #tokens are common sequences of characters found in a set of text 
  #1 token = 4 characters so 100 tokens = 75 words 
  #Issue when max_tokens = 100 was it would break mid sentence 
  max_tokens= 3000,     
  #the maximum number of token in an input sequence
  n_ctx=2048         
)



ai_response = completion.choices[0].message['content']
word_count = len(user_input.split())

summary_word_count = len(ai_response.split())
print(ai_response)
print("Original text length: " +  str(word_count))
print("Summary text length: " +  str(summary_word_count))


with open('output.txt', 'w') as file:
    # Write the text to the file
    file.write(ai_response)