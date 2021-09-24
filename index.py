from flask import Flask, Response
from dash import Dash
import dash_html_components as html

app = Flask(__name__)

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
        ]
    )

    # Create Dash Layout
    dash_app.layout = html.H1('Hello Dash')

    return dash_app.server

app = init_dashboard(app)

@app.route('/')
def catch_all():
    return app
