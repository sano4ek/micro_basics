import uuid
import requests
from flask import Flask, request

app = Flask(__name__)

logger_service_url = "http://0.0.0.0:8081/logging-service"
messenger_service_url = "http://0.0.0.0:8082/messenger"


@app.route('/facade-service', methods=['GET', 'POST'])
def facade_service():
    if request.method == 'POST':
        logging_service_response = requests.post(
            url=logger_service_url,
            json={
                "uuid": str(uuid.uuid4()),
                "message": request.json.get('message')
            }
        )
        status = logging_service_response.status_code
        return app.response_class(status=status)
    else:
        logging_service_response = requests.get(logger_service_url)
        messages_service_r = requests.get(messenger_service_url)
        return str(logging_service_response.text) + ' : ' + str(messages_service_r.text)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080, debug=True)
