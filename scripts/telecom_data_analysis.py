#analysis of dataset

#load


import pandas as pd
df=pd.read_csv("C:/Users/shivansh/PycharmProjects/pythonProject3/Cleaned _telecom_data.csv")
print(df.head())




#analysis on downtime
print()
print("Analysis done on downtime")
total_downtime=df["Downtime(in min)"].sum()
print(f"Total Downtime : {total_downtime}minutes")

#avg donwtime by region
print()
print("Avg donwtime by region")
avg_downtime_by_region=df.groupby("Region")["Downtime(in min)"]. mean()
print("Average downtime by region:")
print(avg_downtime_by_region)


#downtime distribution(we'll take top 5 )

print()
print("Downtime distribution")
top_downtime=df.sort_values("Downtime(in min)",ascending=False).head(5)
print("Top 5 downtime Entries : ")
print(top_downtime[["Timestamp","Region","Downtime(in min)"]])




#analysis on user load
print()
print("Analysis on user load")
avg_users_by_region=df.groupby("Region")["Users Connected"].mean()
print("Average Users Connected By Region : ")
print(avg_users_by_region)



#correlation between users connected and downtime
print()
print("Correlation between users connected and downtime")
correlation=df[["Users Connected","Downtime(in min)"]].corr()
print("Correlation between Users Connected and Downtime : ")
print(correlation)



#analyzing error count
print()
print("Analyzing error count")
total_errors=df["Errors Count"].sum()
print(f"Total Errors : {total_errors}")

#avg errors by region
print("Avg errors by region")
avg_errors_by_region=df.groupby("Region")["Errors Count"].mean()
print("Average Errors by Region : ")
print(avg_errors_by_region)



#errors distribution
print()
print("Errors distribution")

top_errors=df.sort_values("Errors Count",ascending=False).head(5)
print("Top 5 Errors Entries:")
print(top_errors[["Timestamp","Region","Errors Count"]])

















#analyze data throughput
print()
print("Analyze data throughput")
total_throughput=df["Data Throughput(MB)"].sum()
print(f"Total Data Throughput : {total_throughput}MB")



#average data throughput by region
print()
print("Average data throughput by region")
print("Average data throughput by region")
avg_throughput_by_region=df.groupby("Region")["Data Throughput(MB)"].mean()
print("The Average data throughput by region : " )
print(avg_throughput_by_region)


analysis_results={
    "Total_Downtime":[total_downtime],
    "Total Errors":[total_errors],
    "Total Throughput":[total_throughput],
    "Avg Downtime by Region":[avg_downtime_by_region],
    "Avg Users by Region":[avg_users_by_region],
    "Avg Errors by Region":[avg_errors_by_region],
    "Average Throughput by Region":[avg_throughput_by_region]
}



analysis_df=pd.DataFrame.from_dict(analysis_results)
analysis_df.to_csv("telecom_analysis_results.csv",index= False)
print("Analysis results saved as 'telecom_analysis_results.csv'")