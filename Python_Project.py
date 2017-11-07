from flask import Flask, render_template, request, escape

app = Flask(__name__)


def log_request(req,res):
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep=' | ')

@app.route('/')
def hello_world():
    return render_template('index.html', the_title = "Welcome")


@app.route('/result', methods=['POST'])
def hello():
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = set(letters).intersection(set(phrase))
    log_request(request, result)
    return render_template('result.html', the_title="Result is", result=result)


@app.route('/viewlog')
def view_the_log():
    content = []
    with open('vsearch.log') as log:
        for line in log:
            content.append([])
            for item in line.split(' | '):
                content[-1].append(item)
    titles = {'Form Data', 'Remote address', 'User agent', 'Result'}
    return render_template('viewlog. html',the_title='Log result',the_row_titles=titles,the_data=content)


if __name__ == '__main__':
    app.run(debug=True)
