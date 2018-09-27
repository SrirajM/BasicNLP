#!/usr/bin/env python
# coding: utf-8

# In[59]:


from nltk.corpus import stopwords


# In[60]:


from nltk.tokenize import word_tokenize


# In[61]:


from nltk.stem import PorterStemmer


# In[62]:


from nltk.tokenize import word_tokenize


# In[63]:


ps = PorterStemmer()


# In[64]:


example_words = ["python" ,"pythoner","pythoning", "pythoned","pythonly"]


# In[65]:


import nltk


# In[51]:


nltk.download("PorterStemmer")


# In[67]:


for w in example_words:
    print(ps.stem(w))


# In[69]:


new_text ="It is very important to be pythonly while you are pythoning with python."


# In[70]:


words = word_tokenize(new_text)


# In[55]:





# In[71]:


for w in words:
    print(ps.stem(w))


# In[ ]:





# In[ ]:




