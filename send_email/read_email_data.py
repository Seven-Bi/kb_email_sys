#############################
# Author: Chen Bi
# Date: 18 May 2020
#############################

import pandas as pd



def read_data_from_excel():
	output = []

	df = pd.read_excel(r'email_data.xls')

	# clean corrupted data from dataframe
	df['Customer'].fillna('Customer', inplace=True)
	df.dropna(subset = ['Email'], inplace=True)
	df.drop_duplicates(subset='Email', keep = False, inplace = True)

	# form output list
	for i in range(len(df)):
		temp_dict = {'name': df.iloc[i]['Customer'], 'email': df.iloc[i]['Email']}
		output.append(temp_dict)

	return output