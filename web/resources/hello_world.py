from flask_restful import Resource

from sample.hello_world import Greeter

class HelloWorld(Resource):
    def get(self):
        greeter = Greeter()
        return {"message": greeter.say_hello()}