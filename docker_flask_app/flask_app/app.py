from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_message():
    return "Flask App"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
