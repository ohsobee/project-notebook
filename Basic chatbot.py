#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# Define a list of greetings and responses
greetings = ["hello", "hi", "hey", "howdy"]
responses = ["Hello!", "Hi there!", "Hey!", "Howdy!"]

# Define a list of questions and responses
questions = ["how are you", "what's your name", "who are you"]
question_responses = ["I'm just a chatbot.", "I don't have a name, but you can call me ChatGPT.", "I'm here to chat with you."]

# Function to generate a response
def get_response(user_input):
    user_input = user_input.lower()
    
    if user_input in greetings:
        return random.choice(responses)
    elif user_input in questions:
        return random.choice(question_responses)
    else:
        return "I'm not sure how to respond to that."

# Chat loop
print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)


# In[ ]:




