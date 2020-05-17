import pandas as pd
import math



def read_data_from_excel():
	output = []

	df = pd.read_excel(r'email_data.xls')

	# clean corrupted data from dataframe
	df['Customer'].fillna('Customer', inplace=True)
	df.dropna(subset = ['Email'], inplace=True)

	print(len(df))

	df.drop_duplicates(subset='Email', keep = False, inplace = True) 

	print(len(df))

	# form output list
	for i in range(len(df)):
		temp_dict = {'name': df.iloc[i]['Customer'], 'email': df.iloc[i]['Email']}
		output.append(temp_dict)

	return output

read_data_from_excel()