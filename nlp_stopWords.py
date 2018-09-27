#!/usr/bin/env python
# coding: utf-8

# In[47]:


from nltk.corpus import stopwords


# In[48]:


from nltk.tokenize import word_tokenize


# In[49]:


example_sentence = "This is an example showing off stop word fliltration"


# In[50]:


import nltk


# In[51]:


nltk.download("stopwords")


# In[52]:


words = word_tokenize(example_sentence)


# In[53]:


stop_words =set(stopwords.words("english"))


# In[54]:


filtered_sentence = [w for w in words if not w in stop_words]


# In[55]:


print(filtered_sentence)


# In[ ]:





# In[ ]:





# In[ ]:




