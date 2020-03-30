import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

covid = pd.ExcelFile('COVID.xlsx').parse("COVID (copy)")
covid = covid.drop(['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Nguồn'], axis=1)

covid_Viet = covid[covid['Quốc tịch'] == 'Việt Nam']

sex = covid[['Giới tính']]
sex['Giới tính'] = sex['Giới tính'].astype('category')

age = covid[['Tuổi']]
age['Tuổi'] = pd.to_numeric(age['Tuổi'],errors = 'coerce')

sns.set(style='ticks',
        color_codes=True,
        palette = 'deep',
        rc={'figure.figsize':(10,8)})


# Make a histogram for age

bin_edge = [0, 10, 20, 30, 40, 50, 60, 70, 80]
age.hist(bins=bin_edge, color = 'DarkCyan')

plt.title('Số ca theo tuổi tại Việt Nam / Cases for Age in Vietnam')
plt.xlabel('Tuổi / Age')
plt.ylabel('Số ca / Cases')
plt.grid(b=None)

#Make a bar chart for sex
"""
Male = sex['Giới tính'] == 'Nam'
Female = sex['Giới tính'] == 'Nữ'

GenderSplit = {'Gender': ['Male','Female'],
               'Cases': [Male.sum(),Female.sum()]}

GenderSplit_df = pd.DataFrame(GenderSplit,index=['Male','Female'])
GenderSplit_df.plot.bar(rot=0,color='PaleVioletRed')


plt.ylabel('Số ca')
plt.title('Số ca theo giới tính / Cases for Sex in Vietnam')
plt.legend().remove()
"""

plt.show()
