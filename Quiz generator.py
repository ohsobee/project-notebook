#!/usr/bin/env python
# coding: utf-8

# In[2]:


questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A) London', 'B) Berlin', 'C) Paris', 'D) Madrid'],
        'correct_answer': 'C) Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['A) Venus', 'B) Mars', 'C) Jupiter', 'D) Saturn'],
        'correct_answer': 'B) Mars'
    },
   #this code defines questions and provides options, then it has the
    #correct answer underneath
]


# In[ ]:


#here is the function that collects the answer and checks if it is correct
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['question'])
        for option in question['options']:
            print(option)
        
        user_answer = input('Enter the letter corresponding to your answer: ').upper()
        if user_answer == question['correct_answer'][0]:
            print('Correct!\n')
            score += 1
        else:
            print(f'Wrong! The correct answer is {question["correct_answer"]}\n')
    
    print(f'Your score is: {score}/{len(questions)}')

run_quiz(questions)


# In[ ]:





# In[ ]:





# In[ ]:




