import os
from __init__ import app
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from cruddy.query import user_by_id

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_content = Blueprint('content', __name__,
                        url_prefix='/content',
                        template_folder='templates/contenty/',
                        static_folder='static',
                        static_url_path='static')

''' 
Objective of the ideas started with this page is to manage uploading content to a Web Site
Code provided allows user to upload Image into static/uploads folder 
'''
# ... An Image is often called a picture, it works with <image ...> tage in HTML
# ... Supported types jpeg, gif, png, apng, svg, bmp, bmp ico, png ico.

'''
Hack #1 add additional content
'''
# Additional Content
# ... Video, Comma Seperated Values (CSV), Code File (py,java)
# ... One or more uploading capabilities can be provided to support needs of your project

'''
Hack #2 add additional description and capabilities
'''
# Establish a database record that keeps track of content and establishes meta data
# ... user who uploaded
# ... description
# Combine Note and Image upload into single activie
# ... description of Note is Markdown text
# ... try using uploaded image in notes
# ... think about easier markdown UI for user of Note and Images

'''
Hack #3 establish a strategy to manage data being stored through Amazon S3 bucket
'''
# AWS S3 Object Container is a system used to manage content
# ... S3 Bucket Concept: https://www.youtube.com/watch?v=-VVC7uTNJX8


# A global variable is used to provide feedback for session to users, but is considered short term solution
files_uploaded = []


# Page to upload content page
@app_content.route('/')
@login_required
def content():
    # grab user object (uo) based on current login
    uo = user_by_id(current_user.userID)
    user = uo.read()  # extract user record (Dictionary)
    # load content page
    return render_template('content.html', user=user, files=files_uploaded)


# Notes create/add
@app_content.route('/upload/', methods=["POST"])
@login_required
def upload():
    try:
        # grab file object (fo) from user input
        # The fo variable holds the submitted file object. This is an instance of class FileStorage, which Flask imports from Werkzeug.
        fo = request.files['filename']
        # save file to location defined in __init__.py
        # ... os.path uses os specific pathing for web server
        # ... secure_filename checks for integrity of name for operating system. Pass it a filename and it will return a secure version of it.

        fo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(fo.filename)))
        # ... add to files_uploaded to give feedback of success on HTML page
        files_uploaded.insert(0, url_for('static', filename='uploads/' + fo.filename))
    except:
        # errors handled, but specific errors are not messaged to user
        pass
    # reload content page
    return redirect(url_for('content.content'))