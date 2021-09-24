from flask import Flask, Response

from dash import Dash

app = Flask(__name__)

dash_app = dash.Dash(
        server=app,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
        ]
    )

dash_app.layout = html.Div(['Test'], id='dash-container')

@app.route('/')
def catch_all():
    return dash_app.server
