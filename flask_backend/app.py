from flask import Flask
from flask_restful import Api, Resource, reqparse
from core.ApiHandler import ApiHandlerFunction
from core.CsvDataHandler import DataHandlerFunction

app = Flask(__name__)
api = Api(app)


class RootApi(Resource):

    def get(self):
        return {'resultStatus': 'SUCCESS', 'message': 'Hello from RootApi'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('RequestType', type=str)
        args = parser.parse_args()

        message = "RequestType: {}".format(args['RequestType'])
        final_result = {'status': 'SUCCESS', 'message': message}
        return final_result


api.add_resource(ApiHandlerFunction, '/v1/bye')
api.add_resource(DataHandlerFunction, '/v1/datareader')
api.add_resource(RootApi, '/v1/hello')
app.run(host="0.0.0.0", port=3003, debug=True)
