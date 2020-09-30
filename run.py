from flask import Flask

from app2 import appViews




my_app = Flask(__name__)

from app2 import appViews

my_app.register_blueprint(appViews)

my_app.config["SECRET_KEY"] = "helloekwing"

if __name__ == '__main__':
    my_app.run()
