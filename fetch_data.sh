#!/bin/sh
# Reference: https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images
# id: Row number
# Title: Represents the Title of the Food Dish
# Ingredients: Contains the ingredients as they were scraped from the website
# Instructions: Has the recipe instructions to be followed to recreate the dish
# Image_Name: Has the name of the image as stored in the Food Images zipped folder
# 
# SQLite database of 13k recipes
URL=https://github.com/josephrmartinez/recipe-dataset/raw/refs/heads/main/13k-recipes.db
curl -L $URL -o database.db