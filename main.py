import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as pex

# Loading the Excel data into a Pandas DataFrame
df = pd.read_excel(r'C:\Users\Punit\Desktop\python\web_app\SaleData1.xlsx')

# Making an instance as app to Initialize the Dash app
app = dash.Dash(__name__)

# App Layout
#html code to style the heading and labels 
app.layout = html.Div([
    html.H1("Sales Data Visualization", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Select A Sales Column For Visualization:"),
    ], style={'padding': '20px', 'textAlign': 'left'}),
    
     html.Div([
        # Crating a Dropdown menu (styling)
        dcc.Dropdown(
            id='column_list',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[0],  # Default column to show in the plot
            style={'width': '40%', 'margin-top': '5px'}
        ),
    ], style={'padding': '20px', 'textAlign': 'left'}),
    
    # Graph area for displaying the visualizations
    dcc.Graph(id='graph_plot')
])

# Callback to update the graph based on the selected column
@app.callback(
    Output('graph_plot', 'figure'),
    [Input('column_list', 'value')]
)
#function for working condition of column to plotting its respective graph 
def update_graph(column):
    if df[column].isnull().all():
        return pex.scatter(title=f"No data available for {column}")
    
    data = df[column]
    if data.dtype == 'object':
        fig = pex.pie(df, names=column, title=f'{column} - Pie Chart')
    else:
        fig = pex.line(df, y=column, title=f'{column} - Line of Chart')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
