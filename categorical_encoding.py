
import pandas as pd
df = pd.read_csv('Life Expectancy Data.csv')
# Clean column names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
# Encode categorical columns
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
# Save encoded dataset
df_encoded.to_csv('Life-Expectancy-Encoded.csv', index=False)
print("Categorical features encoded and saved as 'Life-Expectancy-Encoded.csv'")