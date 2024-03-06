"""
======================================================================
ex10
======================================================================
Writen by: Rotem kashani, ID = 209073352,   login = rotemkash
	       David Koplev, ID = 208870279 ,    login = davidkop
Program follows 10 actions from the exercise given:
Q1 - read the file and convert to a chart
Q2 - show the marital status of person
Q3 - combine 2 identical values into the same value
Q4 - find the number of people with a master's degree or higher
Q5 - show the annual income of the singles in descending order
Q6 - add a column of total purchases
Q7 - add a column of low, medium and high according to the total number of purchases the person made
Q8 - show a pie chart by column of low, medium and high
Q9 - display a table by column low medium high and displays an average of online purchases,
 in the store and average annual income
Q10 - present a graph made up of two graphs, the first represents education vs annual income and
 the second represents education vs the number of purchases
"""

import pandas as pd
import matplotlib.pyplot as plt

#  Question 1:
file = pd.read_csv("project_data.csv")

#  Question 2:
print(pd.unique(file["marital_status"]))

#  Question 3:
file = file.replace(to_replace="Widowed", value="Widow")

#  Question 4:
education = (file['educational_level'].value_counts(normalize=True))
print(education.filter(items=["Master", "PhD"]))

#  Question 5:
Singles = file.loc[file["marital_status"].isin(["Single"])]
Sorted_singles = Singles["annual_income"].sort_values(ascending=False)
print(Sorted_singles)

#  Question 6:
file["total_purchases"] = file["online_purchases"] + file["store_purchases"]

#  Question 7:
file["low/medium/high"] = ["low" if x < 10 else "medium" if x in range(10, 20) else "high" for x in file["total_purchases"]]

#  Question 8:
plt.pie(file["low/medium/high"].value_counts(), labels=["low", "medium", "high"])
plt.show()

#  Question 9:
groups = pd.DataFrame(file.groupby(by='low/medium/high')[['online_purchases',
                                                         'store_purchases',
                                                          'annual_income']].mean()).reset_index()
print(groups)

#  Question 10:
x = file['educational_level'].replace({'Basic': 0, 'High School': 1, 'Graduation': 2, 'Master': 3, 'PhD': 4})

plt.subplot(1, 2, 1)
plt.scatter(x, file['annual_income'])
plt.title("Education vs Income")

plt.subplot(1, 2, 2)
plt.scatter(x, file['total_purchases'])
plt.title("Education vs Purchases")

plt.show()

