from flask_jwt_extended import jwt_required
from sqlalchemy.sql import text
from flask_restplus import Namespace, Resource
from starter import db
cli_api = Namespace('cli', description='cli related operations')


@cli_api.route('/list')
class ListTableCommand(Resource):

    @jwt_required
    @cli_api.doc('list all table', security='jwt')
    def get(self):
        return [table.name for table in db.get_tables_for_bind()]


@cli_api.route('/init')
class InitDBCommand(Resource):

    # @jwt_required
    @cli_api.doc('init table from seed.sql')
    def get(self):
        with open('seed.sql') as seed:
            db.session.execute(text(seed.read()))
            db.session.commit()
        return {"status": "success"}


@cli_api.route('/drop')
class DropDBCommand(Resource):

    @jwt_required
    @cli_api.doc('drop all table', security='jwt')
    def get(self):
        db.drop_all()
        return {"status": "success"}


