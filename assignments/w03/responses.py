# responses.py
#   usage:      example code for coercing python into acting like R for factors(levels))
#   
#   B. Theisen wrote this code on 4/6/2021, based on tutorial below:
# 
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#sorting-and-order
# 
# 
# import pandas as pd
responses = pd.Series(["Strongly Disagree", "Disagree", "Neither Agree nor Disagree", "Agree", "Strongly Agree"], dtype="category")
#responses = pd.Series(["Strongly Disagree", "Disagree", "Neither Agree nor Disagree", "Agree", "Strongly Agree"]).astype(CategoricalDtype(ordered=True))
responses = responses.cat.set_categories(["Strongly Disagree", "Disagree", "Neither Agree nor Disagree", "Agree", "Strongly Agree"])
print(responses)