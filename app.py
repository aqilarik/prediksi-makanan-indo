import flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'API is working :)'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)