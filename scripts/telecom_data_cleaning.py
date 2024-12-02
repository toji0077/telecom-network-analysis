#checking the csv file data
import pandas as pd

df=pd.read_csv("telecom_data.csv")
print(df.head())

#analysis for missing values
print("Missing values per column : ")
print(df.isnull().sum())

df.fillna(0,inplace=True)



#removing duplicates


print(f"Number of duplicates:{df.duplicated().sum()}")

df.drop_duplicates(inplace=True)



#verify datatypes
print("Data Types : ")
print(df.dtypes)


df["Timestamp"]=pd.to_datetime(df["Timestamp"])



#summarize and aggregate data
print(df.describe())
avg_downtime = df.groupby("Region")["Downtime(in min)"].mean()
print("Avg Downtime by region : ")
print(avg_downtime)




df.to_csv("Cleaned _telecom_data.csv",index=False)
print("Cleaned dataset saved as 'cleaned_telecom_data.csv")