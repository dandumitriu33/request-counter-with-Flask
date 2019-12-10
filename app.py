from flask import Flask, render_template, request

app = Flask(__name__)

GET_COUNTER = 0
POST_COUNTER = 0
PUT_COUNTER = 0
DELETE_COUNTER = 0


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    global GET_COUNTER, POST_COUNTER, PUT_COUNTER, DELETE_COUNTER
    if request.method == 'GET':
        GET_COUNTER += 1
        return render_template('request-counter.html', get_counter=GET_COUNTER)
    elif request.method == 'POST':
        POST_COUNTER += 1
        return render_template('request-counter.html', post_counter=POST_COUNTER)
    elif request.method == 'PUT':
        PUT_COUNTER += 1
        return render_template('request-counter.html', put_counter=PUT_COUNTER)
    elif request.method == 'DELETE':
        DELETE_COUNTER += 1
        return render_template('request-counter.html', delete_counter=DELETE_COUNTER)
    return render_template('request-counter.html')


@app.route('/statistics')
def statistics():
    global GET_COUNTER, POST_COUNTER, DELETE_COUNTER, PUT_COUNTER
    return render_template('statistics.html',
                           get_counter=GET_COUNTER,
                           post_counter=POST_COUNTER,
                           put_counter=PUT_COUNTER,
                           delete_counter=DELETE_COUNTER)


if __name__ == '__main__':
    app.run(debug=True)
