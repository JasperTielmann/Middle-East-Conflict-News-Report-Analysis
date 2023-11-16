#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

cnn1 = pd.read_csv("cnn.csv")
bbc = pd.read_csv("bbc.csv")
fox = pd.read_csv("fox.csv")


# In[2]:


bbc_text = bbc["Text"].str.lower()
cnn_text = cnn1["Text"].str.lower()
fox_text = fox["Text"].str.lower()


# In[3]:


def tool():
    """Receives an Word as input and returns Chart with Frequency of the Word used per News Site"""
    word = input("Please enter a word you would like to know the Freqeuncy of: ")
    word = word.lower()
    word_count = {}
    texts = [cnn_text, bbc_text, fox_text]
    index = 0
    for text in texts:
        total_count = text.str.count(word).sum()
        word_count[index] = total_count/len(text)
        index += 1
    word_count["CNN"] = word_count.pop(0)
    word_count["BBC"] = word_count.pop(1)
    word_count["Fox News"] = word_count.pop(2)
    df = pd.DataFrame.from_dict(word_count, orient="index")
    x = df.index
    y = df[0]

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color=['red', 'blue', 'orange'])


    plt.xlabel('News Site')
    plt.ylabel("Frequency of the word")
    plt.title(f'{word.title()}')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return plt.show()


# In[ ]:


for i in range(int(input("How many words do you want to check?"))):
    tool()


# In[ ]:




