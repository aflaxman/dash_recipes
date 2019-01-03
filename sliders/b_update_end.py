import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from a_basic import app

# make start_year less than end year, if necessary
@app.callback(
    Output(component_id=f'start-id', component_property='value'),
    [Input(component_id=f'end-id', component_property='value')],
    [State(component_id=f'start-id', component_property='value')]
)
def update_start(end, start):
    if end <= start:
        return end-1
    else:
        return start


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
