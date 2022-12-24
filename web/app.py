from flask import Flask
from flask_restful import Api

from web.resources.health import Health
from web.resources.hello_world import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(Health, "/health")
api.add_resource(HelloWorld, '/greet')


if __name__ == "__main__":
    # Use this in non-prod envs only
    app.run(debug=False)
