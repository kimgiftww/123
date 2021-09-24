from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    
    r = render_template(
        'index.jinja2',
        title='Plotly Dash Flask Tutorial',
        description='Embed Plotly Dash into your Flask applications.',
        template='home-template',
        body="This is a homepage served with Flask."
    )
    
    return Response(r)
