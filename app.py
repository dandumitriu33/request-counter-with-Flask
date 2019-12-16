from flask import Flask, render_template, request

app = Flask(__name__)

get_counter = 0
post_counter = 0
put_counter = 0
delete_counter = 0


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


def test(name):
    if name == 'John':
        return 'sorted john'


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    global get_counter, post_counter, put_counter, delete_counter
    if request.method == 'GET':
        get_counter += 1
        return render_template('request-counter.html',
                               get_counter=get_counter)
    elif request.method == 'POST':
        post_counter += 1
        return render_template('request-counter.html',
                               post_counter=post_counter)
    elif request.method == 'PUT':
        put_counter += 1
        return render_template('request-counter.html',
                               put_counter=put_counter)
    elif request.method == 'DELETE':
        delete_counter += 1
        return render_template('request-counter.html',
                               delete_counter=delete_counter)
    return render_template('request-counter.html')


@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    global get_counter, post_counter, put_counter, delete_counter
    if request.method == 'GET':
        return render_template('statistics.html',
                               get_counter=get_counter,
                               post_counter=post_counter,
                               put_counter=put_counter,
                               delete_counter=delete_counter)
    elif request.method == 'POST':
        write_to_file()
        return render_template('statistics.html',
                               get_counter=get_counter,
                               post_counter=post_counter,
                               put_counter=put_counter,
                               delete_counter=delete_counter)


def write_to_file():
    global get_counter, post_counter, put_counter, delete_counter
    data_string = 'GET:' + str(get_counter) + '\n' + 'POST: ' + str(post_counter) + '\n' + 'DELETE: ' + str(delete_counter) + '\n' + 'PUT: ' + str(put_counter)
    with open('request_counts.txt', 'w') as file:
        file.write(data_string)


if __name__ == '__main__':
    app.run(debug=True)
