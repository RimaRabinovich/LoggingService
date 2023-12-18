from flask import Flask, request

app = Flask(__name__)


@app.route('/log', methods=['POST'])
def log_data():
    message = request.json["message"]
    print(f"Logging Service - Received: {message}")
    return "Logged successfully"


if __name__ == '__main__':
    app.run(port=5000)
