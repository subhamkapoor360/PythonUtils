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

def memory_reduce(df):
    for col in df.columns:
        col_type = df[col].dtype
        if(col_type != object):
            min_val = min(df[col])
            max_val = max(df[col])
            if(str(col_type)[:3] == 'int'):
                if(min_val > np.iinfo(np.int8).min and max_val < np.iinfo(np.int8).max):
                    df[col] = df[col].astype(np.int8)
                elif(min_val > np.iinfo(np.int16).min and max_val < np.iinfo(np.int16).max):
                    df[col] = df[col].astype(np.int16)
                elif(min_val > np.iinfo(np.int32).min and max_val < np.iinfo(np.int32).max):
                    df[col] = df[col].astype(np.int32)
                elif(min_val > np.iinfo(np.int64).min and max_val < np.iinfo(np.int64).max):
                    df[col] = df[col].astype(np.int64)
            else:
                if(min_val > np.finfo(np.float16).min and max_val < np.finfo(np.float16).max):
                    df[col] = df[col].astype(np.float16)
                elif(min_val > np.finfo(np.float32).min and max_val < np.finfo(np.float32).max):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

    return df
    