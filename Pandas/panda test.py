import pandas as pd 
import warnings 
import matplotlib.pyplot as plt

# Stop future warning
warnings.simplefilter(action='ignore',category=FutureWarning)

df = pd.read_csv('ceo_data_pay_merged_r3000.csv', index_col=0, usecols=['ticker','company_name','median_worker_pay','pay_ratio','ceo_name','salary','industry'])

# Remove the useless items. Wrangle data
df['pay_ratio'] = df['pay_ratio'].map(lambda x: x.split(":")[0])
df['pay_ratio'] = df['pay_ratio'].replace(',','',regex=True)
df['pay_ratio'] = df['pay_ratio'].astype(int)
df['salary'] = df['salary'].str.replace(',', '')
df['salary'] = df['salary'].str.replace('$', '')
df['salary'] = df['salary'].astype(int)
df['median_worker_pay'] = df['median_worker_pay'].str.replace(',', '')
df['median_worker_pay'] = df['median_worker_pay'].str.replace('$', '')
df['median_worker_pay'] = df['median_worker_pay'].astype(int)
df['industry'] = df['industry'].replace('%20',' ',regex=True)

# Get industries
unique_vals = df['industry'].unique()

# Init the information dictionaries
info = dict({})
salary_dict = dict({})

for column in unique_vals:
    col_items = df.loc[df['industry'] == column]
    info[column] = col_items['pay_ratio'].sum()/col_items['pay_ratio'].count() # mean

for column in unique_vals:
    col_items = df.loc[df['industry'] == column]
    salary_dict[column] = (col_items['median_worker_pay'].sum()/col_items['median_worker_pay'].count(), col_items['salary'].sum()/col_items['salary'].count()) # or df.mean()

# Sort the dictionary
sort_info = {k:v for k,v in sorted(info.items(), key=lambda i:i[1],reverse=True)}

print("Ordered average pay ratio:")
for k,v in sort_info.items():
    print(f'{k} -> {v:.2f}')

print("Average employee wage vs CEO wage")
for k,v in salary_dict.items():
    print(f'Industry: {k}. \n\tAverage Worker Salary: {v[0]:,.2f}. \n\tAverage CEO: {v[1]:,.2f}')

# ax.bar(x=list(sort_info.keys()), y=list(sort_info.values()), height=max(list(sort_info.values())))
print(sort_info.items())

k = list(sort_info.keys())
v = list(sort_info.values())

plt.bar(k,v, label=k)
plt.xticks(rotation='vertical')
plt.show()

plt.bar(info.keys(),info.values())
plt.show()