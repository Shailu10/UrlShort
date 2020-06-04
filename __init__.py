from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key='ade2r43fret545h4y3t45u5u4645y'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app
