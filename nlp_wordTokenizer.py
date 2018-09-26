#!/usr/bin/env python
# coding: utf-8

# In[12]:


from nltk.tokenize import sent_tokenize,word_tokenize


# In[13]:


print("Hello There")


# In[14]:


example_text = "Hello Mr. Smith , how are you doing ?The weather is great and python is awesome . Dont eat cardboard"


# In[15]:


import nltk


# In[16]:


nltk.download("punkt")


# In[17]:


print(sent_tokenize(example_text))


# In[18]:


print(word_tokenize(example_text))


# In[19]:


for i in word_tokenize(example_text):
    print(i)

