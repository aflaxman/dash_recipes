import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([html.Div('Start and End Years'),
                       html.Div(
    dcc.RangeSlider(
        id='start_end-id',
        min=1990,
        max=2040,
        marks=dict([(y,y) for y in range(1990, 2041, 10)]),
        step=1,
        value=[2020, 2030],
        updatemode='drag',
    ),
    style={'height': '30px', 'width': '250px'},),
                       html.Div(id='output-container'),
])

@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='start_end-id', component_property='value')]
)
def update_output(value):
    start, end = value
    if start < end:
        return f'Start value of {start} is less than end value of {end}'
    else:
        return html.Div(f'Start value of {start} is not less than end value of {end}',
                        style={'color':'red'})

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
