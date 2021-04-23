import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import distribution as dis
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate

dist= ["Normal_dist", "Prob_densi"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

colors = {
    'background': '#99b3ff',
    'text': '#7FDBFF'
}

app.layout= html.Div(style={'backgroundColor': colors['background']},
    #children is like a body of the dash
    children=[
        html.H1("Probablity Distribution",style={'text-align':'center'} ),
        html.P("Select Distribution",style={'background-color': "#1a53ff",'font-weight': 'bold'}),
        dcc.Dropdown(id="select_distribution",
                     options=[{"label":val,"value":val}for val in dist],
                     value="Normal_dist",style={"width": "35%"}),
        html.P("Mean",style={'background-color': "#1a53ff",'font-weight': 'bold'}),
        dcc.Input(id="mu",type="number",placeholder="Mean",),
        html.P("Standard_distribution",style={'background-color': "#1a53ff",'font-weight': 'bold'}),
        dcc.Input(id="std",type="number",placeholder="Standard Distribution"),
        html.P("Samples",style={'background-color': "#1a53ff",'font-weight': 'bold'}),
        dcc.Slider(id="n",min=0,max=100, step=1, value=10), #value will initialize it to 10
        dcc.Graph(id="Probablility_denstiy_Graph")
    ]
)

#to connect everythingh that has been created so callback will take two arg i.e. output and input in LIST
@app.callback(Output(component_id="Probablility_denstiy_Graph", component_property= "figure"),
              [Input(component_id="mu",component_property="value"),
               Input(component_id="std",component_property="value"),
               Input(component_id="n",component_property="value")])
def update_graph(mu, std, n):
    #would get error bcoz we havent updates mean or any value and its trting to plot
    if mu==None or std== None or n==None:
        raise PreventUpdate
    values , probabilities= dis.normal_distribution(mu,std,n)
    fig= go.Figure(data=go.Scatter(x= values, y =probabilities),
                   layout=go.Layout(
                       title=go.layout.Title(text="Distribution Graph")
                   )
                   )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True,port=5002)