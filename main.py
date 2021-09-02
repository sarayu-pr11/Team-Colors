# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/sarayu/')
def sarayu():
    return render_template("sarayu.html")


@app.route('/sarayu/', methods=['GET', 'POST'])
def sarayu2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sarayu.html", name=name)
    # starting and empty input default
    return render_template("sarayu.html", name="World")


@app.route('/saathvika/')
def saathvika():
    return render_template("saathvika.html")


@app.route('/saathvika/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("saathvika.html", name=name)
    # starting and empty input default
    return render_template("saathvika.html", name="World")


@app.route('/pranavi/')
def pranavi():
    return render_template("pranavi.html")


@app.route('/pranavi/', methods=['GET', 'POST'])
def pranavi2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("pranavi.html", name=name)
    # starting and empty input default
    return render_template("sarayu.html", name="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
