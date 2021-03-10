
from flask import Flask, request

app = Flask(__name__)

messages = {}


@app.route('/logging-service', methods=['GET', 'POST'])
def logger():
    if request.method == 'POST':
        print(f'\n --- post request from facade --- \n {request.json}\n')
        messages.update({request.json['uuid']: request.json['message']})
        print('--- SUCCESSFULLY SAVED ---')
        return app.response_class(status=200)
    else:
        print('\n --- get request from facade --- \n')
        return ','.join([msg for msg in messages.values()]) or ''


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8081, debug=True)