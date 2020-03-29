# Spark provides 4 hidden RESTFUL API
#
# 1) Submit the job - curl -X POST http://SPARK_MASTER_IP:6066/v1/submissions/create
#
# 2) To kill the job - curl -X POST http://SPARK_MASTER_IP:6066/v1/submissions/kill/driver-id
#
# 3) To check status if the job - curl http://SPARK_MASTER_IP:6066/v1/submissions/status/driver-id
#
# 4) Status of the Spark Cluster - http://SPARK_MASTER_IP:8080/json/


import connexion
import logging
from flask_cors import CORS
from flask import request

app = connexion.FlaskApp(__name__,
                         specification_dir='../openapi/',
                         arguments={'global': 'global_value'},
                         server='tornado')


@app.app.before_request
def log_request_info():
    logging.info('Body: %s', request.get_data())


app.add_api('api.yaml', arguments={'api_local': 'local_value'})
CORS(app.app)
app.run(port=8888)
