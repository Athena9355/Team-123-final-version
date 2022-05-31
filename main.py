from flask import Flask, render_template, request
from __init__ import app
import requests
from cruddy.app_crud import app_crud
import json


from pathlib import Path

app.register_blueprint(app_crud)


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

@app.route('/crud1/')
def crud1():
    return render_template("crud1.html")

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/discussion/')
def discussion():
    return render_template("discussion.html")

@app.route('/drawing/')
def drawing():
    return render_template("drawing.html")

@app.route('/kamya/',methods=['GET', 'POST'])
def kamya():
    url = "https://random-words5.p.rapidapi.com/getMultipleRandom"

    querystring = {"count":"5"}

    headers = {
        'x-rapidapi-host': "random-words5.p.rapidapi.com",
        'x-rapidapi-key': "baf45032bdmsh1fb0709d81a2d0ep1d1bfejsnb09953cc9b71"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("kamya.html", word=response.json())
    print(response.text)


@app.route('/dictionary/', methods=['GET','POST'])
def dictionary():
    try:
        keyword = request.form['keyword']
    except:
        keyword = "Book"
    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/definition/"
    querystring = {"entry":keyword}
    headers = {
        'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "3d43659d98msh26d5e705bc7d8b6p1d6431jsnba44357aaf20"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code<400:
        results = json.loads(response.content.decode("utf-8"))
        return render_template("dictionary.html", results=results, word=keyword)
    else:
        return render_template("dictionary.html", word=keyword)



@app.route('/stub/')
def stub():
    return render_template("stub.html") #code for the function

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/search/')
def search():
    return render_template("search.html")

@app.route('/thread/')
def thread():
    return render_template("thread.html")

@app.route('/plots/')
def plots():
    return render_template("plots.html")

@app.route('/library/')
def library():
    return render_template("library.html")

@app.route('/quote/')
def quote():
    return render_template("quote.html")

@app.route('/bookapi/',methods=['GET', 'POST'])
def bookapi():
    url = "https://google-books.p.rapidapi.com/volumes"

    querystring = {"key":"undefined"}

    headers = {
        "X-RapidAPI-Host": "google-books.p.rapidapi.com",
        "X-RapidAPI-Key": "baf45032bdmsh1fb0709d81a2d0ep1d1bfejsnb09953cc9b71"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("bookapi.html", book=response.json())
    print(response.text)



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=9000) #says "run this directly" app.run will run the server

#index.html is standard

