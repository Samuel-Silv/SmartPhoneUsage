import pandas as pd

df = pd.read_csv("../ingestion/mobile_usage_behavioral_analysis.csv")

print(df.head())
print(df.columns)