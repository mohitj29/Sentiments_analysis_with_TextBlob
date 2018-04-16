# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17_ZWfnM3s4qxUmCUEKNWKjZMaZlAuybl
"""

# importing the dependencies 
import numpy as np
from lightfm.datasets import fetch_movielens  # movie dataset
from lightfm import LightFM  # library for various recommondation models

data = fetch_movielens(min_rating=4) # using only movies with 4 or higher rating
model = LightFM(loss = 'warp') # defining the loss function

model.fit(data['train'], epochs=50, num_threads = 4) # training the model

# created a function to recommend movies to the user
def my_rec(model,data, user_ids):  # trained model, our dataset, and the userid
  n_users,n_item = data['train'].shape  # calculating the number of user and movies
  for id in user_ids:
    # extrating the known positive movie means movies already liked by user
    known_positive =  data['item_labels'][data['train'].tocsr()[user_ids].indices]
    score = model.predict(id,np.arange(n_item)) # predicting the score for every movie
    topitem = data['item_labels'][np.argsort(-score)] # arranging into desc order
    print(id)
    for i in known_positive[:3]:
      print(i)  # printing the top 3 known positive movie
    for j in topitem[:3]:
      print (j) # printing the top 3 recommendation
my_rec(model, data, [3,4,5])  # calling the function