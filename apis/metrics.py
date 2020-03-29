from flask_restplus import Resource, Namespace

metrics_api = Namespace('health', description='API Health Resource')


@metrics_api.route("/")
class HealthResource(Resource):
    def get(self):
        return "Success"
