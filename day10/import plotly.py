import plotly
import pandas as pd
# Load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/IanHung0109/data/main/test20230810-2.csv")
df.columns = [col.replace("AAPL.", "") for col in df.columns]
print(df)

import plotly.graph_objects as go
line1 = go.Scatter(x=df['Date'], y=df['6'], name='Close')
flg = go.Figure(line1)
flg.show()
