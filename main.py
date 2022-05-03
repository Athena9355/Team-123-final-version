# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

# connects default URL to render index.html
@app.route('/') #this is the first page. runs the function: "def index". have to add tab below index. defined roots, roots are connected to functions
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():#these are the different route
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/natalie_abt/')
def natalie_abt():
    return render_template("natalie_abt.html")

@app.route('/to_do/')
def to_do():
    return render_template("to_do.html")

@app.route('/faqs/')
def faqs():
    return render_template("faqs.html")

@app.route('/discussion/')
def discussion():
    return render_template("discussion.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html") #code for the function



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8080) #says "run this directly" app.run will run the server

#index.html is standard
