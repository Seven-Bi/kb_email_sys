#############################
# Author: Chen Bi
# Date: 18 May 2020
# Final version
#############################

import pandas as pd
import os



def read_data_from_excel():
	output = []

	df = pd.read_excel(os.path.dirname(os.path.abspath(__file__)) + '/email_data.xls', sheet_name='Report', usecols='L:O', na_filter=False)

	df.drop_duplicates(keep = False, inplace = True)

	for i in range(len(df)):
		if isinstance(df.iloc[i][0], str) and '@' in df.iloc[i][0]:
			if 'booking.com' in df.iloc[i][0] or 'agoda' in df.iloc[i][0] or 'expedia' in df.iloc[i][0] or 'airbnb' in df.iloc[i][0] or 'book easy' in df.iloc[i][0] or 'ctrip' in df.iloc[i][0] or 'hotelbeds' in df.iloc[i][0]:
				pass
			else:
				output.append(df.iloc[i][0])
	
	return output