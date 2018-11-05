#Importing all necessary modules for analysis
#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Version Checks
print("Numpy Version ->", np.__version__)
print("Panda Version ->", pd.__version__)
print("Seaborn Version ->", sns.__version__)

# Using pandas to convert the vehicles.csv file into a DataFrame
vehicles = pd.read_csv('Data/vehicles.csv', index_col=None)

# Check for values in vehicles.csv DataFrame
vehicles.head()

# Check for Null values in vehicles DataFrame
vehicles.isnull().sum()

# Using pandas to convert the reservations.csv file into a Data Frame
reservations = pd.read_csv('Data/reservations.csv', index_col=None, header=0)

# Check for values in reservations.csv DataFrame
reservations.head()

# Check for Null values in vehicles DataFrame
reservations.isnull().sum()

# Create a results variables to hold merged Pandas Dataframe on the vehicle_id column
# Used innerjoin to avoid NaN values and join on relevant vehicle_id values
result = pd.merge(v, r, how='inner', on='vehicle_id')

# Check for values in results DataFrame
result.head()

# Check for Null values in result DataFrame
result.isnull().sum()

# Value type check for result DataFrame
result.info()

# Initially, we can see that there is a linear positive correlation between recommended_price and actual_price.
# I'll ignore any plot with two data points (Ex: 0, 1) because it will skew the linear regression line.
sns.pairplot(result, kind='reg')

# Let's create a correlation heat map to confirm our pairplots assumptions.

corr = result.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(result.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(result.columns)
ax.set_yticklabels(result.columns)
plt.show()

# The Jupyter cell below is used to visualize the linear relationship determined through Regression Plots.

# Regression plot for recommended_price and actual_price
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
sns.regplot(x='recommended_price', y='actual_price', data=result)

# The Jupyter cell below is used to visualize the the relationship between actual_price and number of images.

# There's a very slight increase in price with an increase in number of images, but the median price is pretty constant
# There seems to be a slight variation in upper quartile of price when there are 18 to 20 images.

# Boxplot for number of images and acutal price
num_images = result[result['num_images'] >= 0]
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
axl = sns.boxplot(x='num_images', y='actual_price', data=num_images)

# The Jupyter cell below is used to visualize the the relationship between is_recent_model and actual_price
# Based on the two violin plots below, there are more reservations with older models then newer models. 
# There is a commonality between the two plots. Users all want to rent within the $50 range / day

# The ViolinPlot below shows how the is_recent_model and actual_price is distributed. 

# Creates a Series that finds all the recent models
recent_model = result[result['is_recent_model'] <= 1]
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
axl = sns.violinplot(x='is_recent_model', y='actual_price', data=recent_model)

# Below you can see the median and lower/upper quartile of prices for vehicles with reservation_type == 1
# Building a Panda Series where all the reservation_type's are 1
res_1 = result[result['reservation_type'] == 1]
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
ax1 = sns.boxplot(x="reservation_type", y="actual_price", data=res_1)

# Below you can see the median and lower/upper quartile of prices for vehicles with reservation_type == 2

# Building a Panda Series where all the reservation_type's are 2
res_2 = result[result['reservation_type'] == 2]
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
ax2 = sns.boxplot(x="reservation_type", y="actual_price", data=res_2)

# In order to take a closer look at the median and lower/upper quartile, we want to display voilin plot of all
# all cars priced a between the lower and upper quartile.

# Distribution of price points for reservation type
res_3 = result[result['actual_price'] < 200]
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
ax1 = sns.violinplot(x="reservation_type", y="actual_price", data=res_3)
