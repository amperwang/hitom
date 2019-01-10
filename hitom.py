from flask import Flask

app = Flask(__name__)

@app.route('/hitom')
def hitom():
    return 'Hello hitom rain'

if __name__ == '__main__':
    app.run()
