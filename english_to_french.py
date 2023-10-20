#!/usr/bin/env python
# coding: utf-8

# In[4]:


#here I will install the google translator library
get_ipython().system('pip install googletrans==4.0.0-rc1')


# In[2]:


#then I need to import the module
from googletrans import Translator


# In[3]:


#I define the translator class
translator = Translator()


# In[5]:


# english text to be translated
english_text = "I like eating cookies."

# translate to french
french_translation = translator.translate(english_text, src='en', dest='fr')
# print the translated text
print(french_translation.text)


# In[ ]:




