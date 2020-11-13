import pandas as pd 

import pandas as pd 

# set file path and read content
filepath = 'Resources/budget_data.csv'
budget_df = pd.read_csv(filepath)
budget_df

total_months = len(budget_df.index) #budget_df.['Date'].count
# total_months
print(f"Total months: {total_months}")

Total = budget_df['Profit/Losses'].sum()
# total_revenue = budget_df.sum(axis=1, skipna=True)
# total_revenue
# print(f"Totals: {total_revenue}")
print(f"Total: {Total}")