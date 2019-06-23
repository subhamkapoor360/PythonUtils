
import pandas as pd

def get_missing_df(df):
	return df.isna().sum()

