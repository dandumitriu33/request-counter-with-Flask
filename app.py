from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/request-counter', methods=['GET', 'POST'])
def request_counter():

    return render_template('request-counter.html')


@app.route('/statistics')
def statistics():
    return render_template('statistics.html')


if __name__ == '__main__':
    app.run(debug=True)
