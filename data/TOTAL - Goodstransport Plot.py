import pandas as pd
import plotly.express as px

# Read data
file_path = "TOTAL - Goodstransport_mld_ton.xlsx"
df = pd.read_excel(file_path)

# Create the plot
fig = px.line(df, x='Year', y=df.columns[1:4], title='Total Transported Goods Over the Years',
              labels={'value': 'Total Transported Goods (kg)', 'variable': 'Transportation Mode'},
              color_discrete_sequence=px.colors.qualitative.Set1)

# Show the plot
fig.show()
