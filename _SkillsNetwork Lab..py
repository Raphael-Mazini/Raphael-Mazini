#!/usr/bin/env python
# coding: utf-8

# # "My Jupyter Notebook on IBM Watson Studio"
# 

# ### Raphael Mazini Aguiar
# #### Commercial manager and future data scientist

# #### I am interested in data science because it makes the perfect union with my professional situation and the skills I already have, joining my experience already acquired with my knowledge that I will have in data science will add a lot to my professional portfolio of experience and skills, thus making me a perfect employee and essential for the modern corporate world of the future.

# In[2]:


from random import randint
sort = randint(0, 5)
print('='*15,'You have two chances to guess','='*15)
for i in range(2):
    luck = print(input('\nTry to hit a number from 0 to 5: '))
    if luck == sort:
        print('You won !')
    else:
        print('You lost !')


# * one
# * two
# * three
# * one
# * two
# * three
# 
