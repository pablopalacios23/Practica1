from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hola'

    #importamos las diferentes views que tenemos
    from .views import views
    from .auth import auth #hemos importado ya nuestros blueprints

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app