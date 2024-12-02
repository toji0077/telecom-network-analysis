import pandas as pd
import numpy as np

#set random seed for reproducibility

np.random.seed(42)


#generate sample data

data={"Timestamp":pd.date_range("24-01-01",periods=1000,freq="H"),
      "Region":np.random.choice(["North","South","East","West"],size=1000),
      "Downtime(in min)":np.random.randint(0,60,size=1000),
      "Users Connected":np.random.randint(100,1000,size=1000),
      "Errors Count":np.random.randint(0,10,size=1000),
      "Data Throughput(MB)":np.random.randint(100,10000,size=1000),
      }

df= pd.DataFrame(data)

df.to_csv("telecom_data.csv",index=False)

print("Dataset Generated and saved as 'telecom_data.csv")
