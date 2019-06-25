import operator
import pandas as pd

def get_missing_df(df):
	return df.isna().sum()

def get_missing_df_by_percent(df):
	total = df.isnull().sum().sort_values(ascending=False)
	percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
	missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
	return missing_data

def get_df_col_distribution_rate(df):
	distribution_max_rate = {}
	for col in df.columns:
		rate = df[col].value_counts(normalize=True, dropna=False).values[0]
		distribution_max_rate[col] = round(rate,4)
	distribution_max_rate = pd.DataFrame(distribution_max_rate,index = [0]).T
	distribution_max_rate.columns = ['Max Rate']
	return distribution_max_rate

def get_feature_unique(df):
	nunique_map = {}
	for column in df.columns:
		nunique_map.update({column:df[column].nunique()})
	nunique_map = sorted(nunique_map.items(), key=operator.itemgetter(1),reverse = True)
	nunique_df = pd.DataFrame(dict(nunique_map),index = [0]).T
	nunique_df.columns = ['Unique Feature Count']
	return nunique_df