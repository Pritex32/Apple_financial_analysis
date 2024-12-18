#!/usr/bin/env python
# coding: utf-8

# # Author: Ukanwa Prisca

# In[227]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings .filterwarnings('ignore')


# In[228]:


df=pd.read_csv(r'C:\Users\USER\Documents\dataset\Apple 2009-2024.csv')


# In[229]:


df.head()


# # About the Dataset:
# ### This dataset provides a deep dive into Apple's financials during one of the most iconic periods in corporate history—2009 to 2014. These were the years when Apple transformed from a tech leader into a global superpower, driven by groundbreaking innovations on a perpetual Cupertino conveyor belt. Explore key financial metrics that fuelled Apple’s meteoric rise, from revenue and profits to product sales and market shifts.  Perfect for anyone interested in analysing the financial backbone of a historic innovation run!

# In[230]:


df.duplicated().sum()


# In[231]:


# checking for null values
df.isnull().sum()


# ## Feature explanations:
# #### 1.Year: Represents the fiscal year of the data being reported.
# #### 2.EBITDA (millions): Earnings Before Interest, Taxes, Depreciation, and Amortization, measured in millions. It indicates a company's profitability from core operations.
# #### 3.Revenue (millions): Total income generated from sales or services, measured in millions.
# #### 4.Gross Profit (millions): Revenue minus the cost of goods sold (COGS), representing the profit before deducting operating expenses, measured in millions.
# ### 5.Op Income (millions): Operating Income, calculated as gross profit minus operating expenses, measured in millions. It reflects the profit from regular business operations.
# #### 6.Net Income (millions): Profit remaining after all expenses, taxes, and interest have been deducted from revenue, measured in millions.
# #### EPS: Earnings Per Share, calculated as net income divided by the total number of shares outstanding. It indicates profitability per share of the company's stock.
# #### 7.Shares Outstanding: The total number of a company’s shares currently held by all shareholders.
# #### 8.Year Close Price: The closing price of the company’s stock at the end of the fiscal year.
# #### 9.Total Assets (millions): The total value of a company’s assets (e.g., cash, inventory, property, equipment), measured in millions.
# #### 10.Cash on Hand (millions): The amount of cash and liquid assets the company has available, measured in millions.
# #### 11.Long Term Debt (millions): Total debt obligations that are due for repayment after one year, measured in millions.
# #### 12.Total Liabilities (millions): The sum of all financial obligations or debts of the company, measured in millions.
# #### 13.Gross Margin: The percentage of revenue remaining after deducting the cost of goods sold, calculated as (Gross Profit / Revenue) * 100.
# #### 14.PE Ratio: Price-to-Earnings Ratio, calculated as the market value per share divided by earnings per share (EPS). It indicates how much investors are willing to pay per dollar of earnings.
# #### 15.Employees: The total number of employees working for the company during the fiscal year.
# #### Long Term Debt (millions)): Duplicate column; same as "Long Term Debt (millions)" but likely an error. This should be corrected or removed.

# ## Data Cleaning:

# In[232]:


# removing special characters
df['EBITDA (millions)']=df['EBITDA (millions)'].str.replace('$','')
df['Revenue (millions)']=df['Revenue (millions)'].str.replace('$','')
df[ 'Gross Profit (millions)']=df[ 'Gross Profit (millions)'].str.replace('$','')
df['Op Income (millions)']=df['Op Income (millions)'].str.replace('$','')
df['Net Income (millions)']=df['Net Income (millions)'].str.replace('$','')
df['EPS']=df['EPS'].str.replace('$','')
df['Long Term Debt (millions)']=df['Long Term Debt (millions)'].str.replace('$','')
df['Cash on Hand (millions)']=df['Cash on Hand (millions)'].str.replace('$','')
df['Total Liabilities (millions)']=df['Total Liabilities (millions)'].str.replace('$','')
df['Gross Margin']=df['Gross Margin'].str.replace('%','')
df['Total Assets (millions)']=df['Total Assets (millions)'].str.replace('$','')


# In[233]:


df['EBITDA (millions)']=df['EBITDA (millions)'].str.replace(',','')
df['Revenue (millions)']=df['Revenue (millions)'].str.replace(',','')
df[ 'Gross Profit (millions)']=df[ 'Gross Profit (millions)'].str.replace('$','')
df['Op Income (millions)']=df['Op Income (millions)'].str.replace(',','')
df['Net Income (millions)']=df['Net Income (millions)'].str.replace(',','')
df['EPS']=df['EPS'].str.replace('$','')
df['Long Term Debt (millions)']=df['Long Term Debt (millions)'].str.replace(',','')
df['Cash on Hand (millions)']=df['Cash on Hand (millions)'].str.replace(',','')
df['Total Liabilities (millions)']=df['Total Liabilities (millions)'].str.replace(',','')
df['Employees']=df['Employees'].str.replace(',','')
df['Total Assets (millions)']=df['Total Assets (millions)'].str.replace(',','')
df['Shares Outstanding']=df['Shares Outstanding'].str.replace(',','')
df['Gross Profit (millions)']=df['Gross Profit (millions)'].str.replace(',','')


# In[234]:


# converting columns to numeric
df['EBITDA (millions)']=df['EBITDA (millions)'].astype(int)
df['Revenue (millions)']=df['Revenue (millions)'].astype(int)
df['Gross Profit (millions)']=df['Gross Profit (millions)'].astype(float)
df['Op Income (millions)']=df['Op Income (millions)'].astype(int)
df['Net Income (millions)']=df['Net Income (millions)'].astype(int)
df['EPS']=df['EPS'].astype(float)
df['Shares Outstanding']=df['Shares Outstanding'].astype(int)
df['Total Liabilities (millions)']=df['Total Liabilities (millions)'].astype(int)
df['Gross Margin']=df['Gross Margin'].astype(float)
df['Total Assets (millions)']=df['Total Assets (millions)'].astype(int)
df['Cash on Hand (millions)']=df['Cash on Hand (millions)'].astype(int)
df['Total Assets (millions)']=df['Total Liabilities (millions)'].astype(int)
df['Long Term Debt (millions)']=df['Long Term Debt (millions)'].astype(int)
df['Employees']=df['Employees'].astype(int)


# In[ ]:





# # Exploratory Analysis

# # 1.How has revenue and net income trended over the years?

# In[235]:


yearly_revenue=df.groupby('year')['Revenue (millions)'].sum()


# In[236]:


plt.plot(yearly_revenue,marker='o',markerfacecolor='skyblue')
plt.title('revenue and net income trend over the years')
plt.grid(True)


# findings:
# revenue have been on high increase from 2010 till present

# In[237]:


net_income=df.groupby('year')['Net Income (millions)'].sum()


# In[238]:


plt.plot(net_income,marker='*')
plt.title('net income trend')
plt.xlabel('years')
plt.ylabel('net_income')


# findings:
# the net income of the company has been on the rise from 2010 till present
# conclusion:
# over the years the net income and revenue have not declined

# # 2.Is there a correlation between revenue growth and EBITDA?

# In[239]:


df.dtypes # checking for data types


# In[240]:


df.dtypes
# reconfirming the data types


# In[ ]:





# In[241]:


# to determine if the increase of EBITA leasde to increase in revenue
from scipy.stats import pearsonr


# In[242]:


stats,p=pearsonr(df['EBITDA (millions)'],df['Revenue (millions)'])
stats,p
if p >0.05:
    print('there is a relationship')
else:
    print('no relationship')
    


# # findings:
# ##  there is no relationship between EBITDA and revenue , meaning the increase in one does not lead to increase in the order

# In[ ]:





# # 3.What percentage of gross profit is typically converted to net income?

# In[243]:


percentage=df['Gross Profit (millions)']/df['Revenue (millions)']*100
percentage
# the following are percentage converted to net income


# In[244]:


plt.figure(figsize=(10,5))
sns.barplot(x=df['year'],y=percentage,palette='magma')
plt.xticks(rotation='vertical')
plt.title('% of gross profit converted to netincome')


# the percentage of gross profit converted to net income had a massive increase from 2021 till present, this indicates that the  company revenue have massively increased.

# In[ ]:





# # 4.How does the gross margin compare across different years, and what does it indicate about cost efficiency?

# In[245]:


sns.lineplot(x=df['year'],y=df['Gross Margin'])
plt.grid(True)
plt.title(' Gross margin over the years')


# ### findings:
# ### from 2010 gross margin has been on a decrease untill year 2020, their profit margin took a rise till present, indicating increase in revenue

# In[ ]:





# ## 5.How does operating income relate to gross profit and EBITDA?

# In[246]:


from scipy .stats import f_oneway


# ### h1:is there relationship between operating system,gross profit and EBITDA
# ### h0:there is no relationship between operating system,gross profit and EBITDA

# In[247]:


stat,p=f_oneway(df['Op Income (millions)'],df['EBITDA (millions)'],df['Gross Profit (millions)'])
print(stat,p)
if p>0.05:
    print('there is relationship')
else:
    print('no relationship')


# conclusion: 
# from the hypothesis testing, it is discovered that there is a relationship between operation income,gross income and EBITDA.
# which simply means that an increase or decrease of one will affect the others.

# In[ ]:





# ## 6.Is the company's gross profit margin improving or declining over time?

# ### from the chart from number 4, the gross margin is increasing over time

# In[ ]:





# ## 7.What is the relationship between EPS (Earnings Per Share) and shares outstanding?

# In[248]:


from scipy.stats import spearmanr


# In[249]:


stat,p=spearmanr(df['EPS'],df['Shares Outstanding'])
print(stat,p)
if p>0.05:
    print('there is relationship')
else:
    print('no relationship')


# finding:
# there is no relationship between EPS and outstanding share

# In[ ]:





# # Financial Health

# ### 7.How has the company's long-term debt and total liabilities changed over time?

# In[250]:


plt.plot(df['year'],df['Long Term Debt (millions)'],color='yellow',marker='d',markerfacecolor='purple')
plt.title('long term debt over the years')
plt.grid(True)


# ## finding : long term debt have been on increase until 2018, it started it's decrease from 2018 till present

# In[ ]:





# In[251]:


plt.plot(df['year'],df['Total Liabilities (millions)'],color='Red')
plt.title('liablilites over the years')


# ### findings: liabilites have been increasing till present

# In[ ]:





# ## 8.What is the ratio of cash on hand to long-term debt, and how has it evolved?

# In[252]:


df['Cash_Ratio'] = df['Cash on Hand (millions)'] / df['Long Term Debt (millions)']


# In[253]:


plt.plot(df['year'],df['Cash_Ratio'],color='green',marker='o',markerfacecolor='red')
plt.title('ratio of cash over time')


# ### An increasing ratio indicates improved financial liquidity and reduced dependency on long-term debt. but in this case, the ratio has been decreasing over time.

# In[ ]:





# ## 9.Does the company's total assets sufficiently cover its total liabilities?

# In[254]:


plt.plot(df['Total Assets (millions)'],df['Total Liabilities (millions)'],marker='o',markerfacecolor='yellow')
plt.title(' total asset vs total liabilities')
plt.xlabel('total asset')
plt.ylabel('total liabilities')


# ## the chart shows that the company total asset covers its liablities

# In[ ]:





# ## 10.How does the company's PE ratio (Price-to-Earnings ratio) compare over the years, and does it align with market expectations?

# In[255]:


plt.plot(df['year'],df['PE ratio'],marker='d',markerfacecolor='green')
plt.title('Price-to-Earnings ratio')
plt.xlabel('Year')
plt.ylabel('PE ratio')


# ### findings: from 2018, the earning per ratio spike to an increase , a little decline in 2022 and recovered it strenght till present 2024

# In[ ]:





# # Market and Shareholder Insights

# ## 11.How does the year close price correlate with EPS and PE ratio?

# In[256]:


plt.plot(df['EPS'],df['Year Close Price'],marker='d',markerfacecolor='yellow',color='blue')
plt.title('EPS vs year close price')
plt.xlabel('eps')
plt.ylabel('year close price')


# In[257]:


stat,p=pearsonr(df['EPS'],df['Year Close Price'])
print(stat,p)
if p>0.05:
    print('relationship')
else:
    print('no relationshp')


# ### findings: year open price  and EPS has no correlation, which means that the year open price doesnt affeect earnings per share

# In[258]:


stat,p=pearsonr(df['Year Close Price'],df['PE ratio'])
print(stat,p)
if p>0.05:
    print('relationship')
else:
    print('no relationshp')


# In[259]:


plt.plot(df['Year Close Price'],df['PE ratio'],color='red',marker='*')
plt.title('year close price vs pe ratio')
plt.xlabel('PE ratio')
plt.ylabel('Year Close Price')


# ### findings: year open price and PE ratio has no correlation, which means that the year open price doesnt affect earning ratio

# In[ ]:





# ## 12. Is there a relationship between net income and the number of shares outstanding?

# In[260]:


plt.plot(df['Shares Outstanding'],df['Net Income (millions)'],color='red')
plt.title('Shares Outstanding vs Net Income ')
plt.xlabel('share outstanding')
plt.ylabel('net income')


# In[261]:


stat,p=pearsonr(df['Shares Outstanding'],df['Net Income (millions)'])
print(stat,p)
if p>0.05:
    print('relationship')
else:
    print('no relationshp')


# ### findings: there is no relationship between share outstanding and net come, that means the increase or decrease of one does not affect the other

# In[ ]:





# # Employee and Operational Efficiency

# ## 13.How has the number of employees affected profitability metrics like EBITDA and Op Income?

# In[262]:


plt.plot(df['Employees'],df['Op Income (millions)'])
plt.title('employees vs op income')


# ### findings: the employees does not affect the operating income from the chart above

# In[ ]:





# ## 14. What is the revenue or profit generated per employee, and has this changed over time?

# In[263]:


Revenue_per_Employee = df['Revenue (millions)']/ df['Employees']
Profit_per_Employee = df['Net Income (millions)'] / df['Employees']


# In[264]:


plt.plot(df['year'],Revenue_per_Employee,marker='*',color='purple')
plt.title('year vs revenue')


#  A consistent increase in revenue or profit per employee over time signal that the company is becoming more efficient, growing, or leveraging its workforce better.

# In[ ]:





# # Comparative Ratios

# ## 15.Are there specific years where cash on hand relative to gross profit or net income significantly deviates?
# 

# In[265]:


plt.plot(df['year'],df['Cash on Hand (millions)'],marker='*',markerfacecolor='black',color='orange')
plt.grid(True)
plt.title('year vs cash on hand')
plt.xlabel('year')
plt.ylabel('cash on hand')


# findings: from 2018 to 2024, the cash on hand have been declining massively. A decline in cash on hand can signal financial distress, limit growth potential, and reduce operational flexibility

# In[ ]:





# ## 16.What is the trend of long-term debt as a percentage of total liabilities, and does it indicate improving or worsening debt structure?

# In[266]:


Total_Liabilities = (df['Long Term Debt (millions)'] / df['Total Liabilities (millions)']) * 100


# In[267]:


plt.plot(df['year'],Total_Liabilities,marker='o',markerfacecolor='grey',color='red')
plt.title('percentage liabilities')
plt.grid(True)
plt.ylabel('liablities')
plt.xlabel('year')


#  the ratio have started decreasing from 2018, suggesting that the company is reducing its reliance on long-term debt relative to total liabilities, which could indicate an improvement in financial stability. It may be paying down long-term debt or using other financing sources, such as equity or short-term debt, to cover liabilities.

# In[ ]:




