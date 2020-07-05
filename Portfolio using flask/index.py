from flask import Flask, render_template, send_file
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/resume/')
def return_files_tut():
    try:
        return send_file('static', attachment_filename='AyushUpdate2.pdf')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
