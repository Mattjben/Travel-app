from flask import Flask
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.config['SECRET_KEY']='CCA1s3923076'
app.config['WTF_CSRF_SECRET_KEY']='CCA1s3923076'
CSRFProtect().init_app(app)

from Flask_application import routes