from flask import Flask, render_template, request, redirect, url_for
from __init__ import app, login_manager
from flask_login import login_required


from cruddy.app_crud import app_crud


from pathlib import Path

from cruddy.login import logout

app.register_blueprint(app_crud)


# connects default URL to render index.html
@app.route('/') #this is the first page. runs the function: "def index". have to add tab below index. defined roots, roots are connected to functions
def index():
    return render_template("index.html")


# Flask-Login directs unauthorised users to this unauthorized_handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    global next_page
    next_page = request.endpoint
    return redirect(url_for('main_login'))


# if login url, show phones table only
@app.route('/login/', methods=["GET", "POST"])
def main_login():
    # obtains form inputs and fulfills login requirements
    global next_page
    if request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if login(email, password):
            try:        # try to redirect to next page
                temp = next_page
                next_page = None
                return redirect(url_for(temp))
            except:     # any failure goes to home page
                return redirect(url_for('index'))


    # if not logged in, show the login page
    return render_template("login.html")


# if login url, show phones table only
@app.route('/logout/', methods=["GET", "POST"])
@login_required
def main_logout():
    logout()
    return redirect(url_for('index'))


@app.route('/authorize/', methods=["GET", "POST"])
def main_authorize():
    error_msg = ""
    # check form inputs and creates user
    if request.form:
        # validation should be in HTML
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")  # password should be verified
        if password1 == password2:
            if authorize(user_name, email, password1):
                return redirect(url_for('main_login'))
        else:
            error_msg = "Passwords do not match"
    # show the auth user page if the above fails for some reason
    return render_template("authorize.html", error_msg=error_msg)
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

#@app.route('/crud1/')
#def crud1():
    #return render_template("crud1.html")

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



@app.route('/stub/')
def stub():
    return render_template("stub.html") #code for the function

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/thread/')
def thread():
    return render_template("thread.html")

@app.route('/plots/')
def plots():
    return render_template("plots.html")

@app.route('/library/')
def library():
    return render_template("library.html")

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
    app.run(debug=True,port=8000) #says "run this directly" app.run will run the server

#index.html is standard

