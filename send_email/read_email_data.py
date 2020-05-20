#############################
# Author: Chen Bi
# Date: 18 May 2020
#############################

import pandas as pd
import os



house_shares = ['booking.com', 'agoda', 'expedia', 'airbnb', 'book easy', 'ctrip', 'hotelbeds']

def read_data_from_excel():
	output = []
	df = pd.read_excel(os.path.dirname(os.path.realpath(__file__)) + '/email_data.xls')

	# clean corrupted data from dataframe
	df['Customer'].fillna('Customer', inplace=True)
	df.dropna(subset = ['Email'], inplace=True) # no NaN
	df.drop_duplicates(subset='Email', keep = False, inplace = True) # no repeated data

	########################################################################################
	# Here needs a faster algorithm to get rid of those email entries contain house_shares
	########################################################################################
	# df = df[df['Email'] != 'Bonds']
	# print(len(df))
	# df = df['Email'].apply(lambda x: x == house_shares)
	# print(len(df))


	# form output list
	for i in range(len(df)):
		###################################################
		# temporary naive solution for dealing this matter
		###################################################
		if 'booking.com' in df.iloc[i]['Email'] or 'agoda' in df.iloc[i]['Email'] or 'expedia' in df.iloc[i]['Email'] or 'airbnb' in df.iloc[i]['Email'] or 'book easy' in df.iloc[i]['Email'] or 'ctrip' in df.iloc[i]['Email'] or 'hotelbeds' in df.iloc[i]['Email']:
			pass
		else:
			temp_dict = {'name': df.iloc[i]['Customer'], 'email': df.iloc[i]['Email']}
			output.append(temp_dict)

	return output


###################################################
# list out all entries
###################################################
def show():
	print('=========================================')
	for i in read_data_from_excel():
		print(i['name'], end='')
		print('          -          ', end='')
		print(i['email'])
	print('=========================================')

# show()

