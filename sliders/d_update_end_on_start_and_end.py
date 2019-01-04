import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from a_basic import app

# make end more than start year, if necessary
@app.callback(
    Output(component_id=f'end-id', component_property='value'),
    [Input(component_id=f'start-id', component_property='value'),
     Input(component_id=f'end-id', component_property='value')]
)
def update_start(start, end):
    if end <= start:
        return start+1
    else:
        return end



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
