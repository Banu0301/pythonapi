from flask import Flask  # Correct import statement

app = Flask(__nam__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, I am Banu!"

if __nam__ == '__main__':
    app.run(debug=True)
