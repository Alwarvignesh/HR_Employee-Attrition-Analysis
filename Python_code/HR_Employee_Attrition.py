#!/usr/bin/env python
# coding: utf-8

# ## HR Employee Attrition Analysis
# Employee attrition can quietly harm even the most successful organizations in a surprisingly short time. While many companies focus on the expensive process of hiring, not enough attention is given to solving the reasons top talent leaves. 
#  Although people often think that low pay is the main reason for employees leaving, Understanding why employees leave is the first step in fixing the problem before it seriously damages your organization. 
#  This analysis aims to give employers practical insights to understand their employees better and make necessary changes before turnover rates rise, productivity falls, and the company's future becomes uncertain.
#  
#  #### **What does Employee Attrition Means?**
# 
#    Employee attrition happens when people leave a company, like getting a new job or retiring, without someone new coming in right away. The attrition rate is how we figure out how many people leave the company in a certain amount of time.
#      
# #### **What is the difference between employee turnover and attrition?**
# 
#    Employee turnover and attrition both happen when someone leaves a job, but they differ in how it happens. Attrition is when someone leaves because they retire or the employer ends the job. Turnover is when someone leaves, and the company has to find a new person to take their place.
#     
# #### **What is a good employee attrition rate?**
#    A good, average turnover rate is around 10%.
#   
#   ## Problem 
#    We want to figure out why employees are either happy or leaving the company.
# 
# ## Business Objective
#    Identify the things that make employees happy. By looking into these factors, we can know what to improve so that employees are happier and don't leave as much.

# ## Let's Start!!!

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


emp_attrition=pd.read_csv("D:/AVN/Internship/Project - 1-Employee Attrition Analysis Tasklist/Dataset/HR_Employee_Attrition.csv")


# In[3]:


emp_attrition.head(10)


# In[4]:


emp_attrition.info()


# In[5]:


emp_attrition.duplicated().sum()


# In[6]:


emp_attrition.isnull().sum()


# In[7]:


emp_attrition.describe()


# In[8]:


g_retention=emp_attrition.groupby('Attrition').get_group('No').count().iloc[1]
# print(g_retention)
g_attrition=emp_attrition.groupby('Attrition').get_group('Yes').count().iloc[1]
avg=emp_attrition['EmployeeNumber'].size
attrition_rate=g_attrition/avg*100
retention_rate=g_retention/avg*100
total=attrition_rate+retention_rate
print(total)
result = np.concatenate([np.array([attrition_rate]), np.array([retention_rate])])
print(result)


# In[9]:


# Calculate Overall Attrition Rate
fig=plt.figure(figsize=(6,4))
plt.bar(['Attrition','Retention'],[total-retention_rate,retention_rate],color=['orange','maroon'],linewidth=2,edgecolor="Black")
plt.ylabel("Percentage")
plt.title("Overrall Attrition Rate")
plt.show()


# In[10]:


# Calculate attrition rates for each department
dep_total=emp_attrition.groupby('Department')['Attrition'].value_counts().unstack().fillna(0)
per=dep_total/g_attrition*100
dep_high=per.sort_values(by='Yes',ascending=False).iloc[:,1:5]
dep_low=per.sort_values(by='Yes',ascending=True).iloc[:,1:5]
dep_high
plt.figure(figsize=(15,7))
plt.subplot(1,2,1)
sns.barplot(x='Yes', y=dep_high.index, data=dep_high,palette='Reds_r')
plt.title('Top 5 Departments with Highest Attrition Rates') 
plt.xlabel('Attrition Rate(%)')
plt.ylabel('Department')

plt.subplot(1,2,2)
sns.barplot(x='Yes',y=dep_low.index,data=dep_low,palette='Blues_r')
plt.title('Top 5 Departments with Lowest Attrition Rates')
plt.xlabel('Attrition Rate(%)')
plt.ylabel('Department')
plt.tight_layout()
plt.show()


# In[11]:


# Analyze Relationship between Employee Satisfaction and Attrition
sns.boxplot(x="Attrition", y="JobSatisfaction", data=emp_attrition, palette="Set1")
plt.title('Relationship between Employee Satisfaction and Attrition')
plt.xlabel("Attrition (0: No, 1: Yes)")
plt.ylabel('Job Satisfaction')
plt.tight_layout()
plt.show()


# In[12]:


# Compare Attrition Rates by Job Level
fig=plt.figure(figsize=(12,6))
sns.countplot(x="JobLevel", hue="Attrition", data=emp_attrition, palette="Set1")
plt.title('Attrition Rate by Job Level')
plt.xlabel("Job Level")
plt.ylabel('Attriton')
plt.legend(title='Attrition',labels=['No','Yes'])
plt.show()


# In[13]:


# Compare Attrition Rates by Job Role
fig=plt.figure(figsize=(22,10))
sns.countplot(x="JobRole", hue="Attrition", data=emp_attrition, palette="Set2")
plt.title('Attrition Rate by Different Job Role')
plt.xlabel("Job Role")
plt.ylabel('Attriton')
plt.legend(title='Attrition',labels=['No','Yes'])
plt.show()


# In[14]:


# Relationship between Employee Age and Attrition
fig=plt.figure(figsize=(12,6))
custom_palette = ["#FF5733", "#33FF57"]
sns.histplot(x='Age',hue='Attrition',data=emp_attrition,kde='True',palette=custom_palette,bins=30)
plt.title('Realationship between Age and Attrition')
plt.xlabel('Attrition')
plt.ylabel('Age')
plt.legend(title='Attrition',labels=['Yes','No'])
plt.show()


# In[15]:


# Compare Attrition Rates by Education Level
emp_attrition['Attrition_value']=emp_attrition['Attrition'].map({'Yes':1,'No':0})
fig=plt.figure(figsize=(8,6))
custom_palette = ["#FF5733", "#33FF57"] 
sns.barplot(x='Education',y='Attrition_value',data=emp_attrition,palette=custom_palette)
plt.title('Attrition Rate by Education Level')
plt.xlabel('Education')
plt.ylabel('Attrition')
plt.show()


# In[16]:


# Compare Attrition Rates by Total Working Years
fig=plt.figure(figsize=(14,7))
current_palette=["#FF5733", "#33FF57"] 
sns.boxplot(x='Attrition',y='TotalWorkingYears',data=emp_attrition,palette=current_palette)
plt.title('Attrition Rate by Total Working Years')
plt.ylabel('Total working years')
plt.xlabel('Attrition(0:No,1:Yes)')
plt.show()


# In[17]:


# Compare Attrition Rates by Gender
fig=plt.figure(figsize=(12,6))
sns.countplot(x='Gender',hue='Attrition',data=emp_attrition,palette='Greens')
plt.title('Attrition Rate affected by Gender')
plt.xlabel('Gender')
plt.ylabel('count')
plt.legend(title="Attrition",labels=["Yes","No"])
plt.show()


# In[18]:


#Relationship Between Work Environment and Attrition
attrition_rate=emp_attrition.groupby('EnvironmentSatisfaction')['Attrition_value'].mean()
# fig=plt.figure(figsize=(16,8))
bar_color = 'red'

plt.bar(attrition_rate.index,attrition_rate.values,color=bar_color,linewidth=2,edgecolor='Blue')
# sns.barplot(x='EnvironmentSatisfaction',y='Attrition_value',data=emp_attrition,ci=None,capsize=0.1)
plt.title('Relationship between Work Environment and Attrition')
plt.xlabel('EnvironmentSatisfaction')
plt.ylabel('Attrition')
plt.show()


# In[19]:


#Impact of Environment Satisfaction on Attrition
plt.figure(figsize=(12,6))
sns.barplot(x='Attrition',y='EnvironmentSatisfaction',data=emp_attrition,yerr=None)
plt.title("Impact of Environment Satisfaction on Attrition")
plt.xlabel('Environment Satisfication')
plt.ylabel("Attrition")
plt.show()


# In[20]:


job_role=emp_attrition.groupby('JobRole')['Attrition'].value_counts().unstack().fillna(0)
job_sort=job_role.sort_values(by='Yes',ascending=False).iloc[:,1:5]
job_sort


# In[ ]:





# In[21]:


#Most Common Job Roles with Attrition
plt.figure(figsize=(12,6))
sns.barplot(x=job_sort.index,y='Yes',data=job_sort,palette='Set1')
plt.title("Most Common Job Roles with Attrition")
plt.xlabel("JobRole")
plt.ylabel("Attrition")
plt.xticks(rotation=45,ha="right")
plt.show
# sns.barplot(x='Yes',y=dep_low.index,data=dep_low,palette='Blues_r')


# In[22]:


dep_total=emp_attrition.groupby('Department')['Attrition'].value_counts().unstack().fillna(0)
dep_total


# In[23]:


#Attrition rate by Department
plt.figure(figsize=(12,6))
sns.countplot(x='Department',hue='Attrition',data=emp_attrition,palette='Dark2')
plt.title("Attrition rate by Department")
plt.xlabel('Department')
plt.ylabel('Attrition count')
plt.show()


# In[24]:


#Attrition Distribution by Gender
attrition_gender=emp_attrition.groupby('Gender')['Attrition'].value_counts().unstack()
plt.figure(figsize=(6,6))
plt.pie(attrition_gender['Yes'],labels=attrition_gender.index,autopct='%1.1f%%',colors=['green','coral'])
plt.title('Attrition Distribution by Gender')
plt.show()


# In[25]:


#Effect of Distance from Home on Attrition
plt.figure(figsize=(12,6))
sns.kdeplot(x='DistanceFromHome',hue='Attrition',data=emp_attrition,fill=True,common_norm=False,palette='Set2')
plt.title("Effect of Distance from Home on Attrition")
plt.xlabel('Distance From Home')
plt.ylabel('Attrition')
plt.legend(title='Attrition',labels=['No','Yes'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




