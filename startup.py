#!/usr/bin/env python3
from flask import Flask 
from Flask_application import app
if __name__ == '__main__':
      app.run(host='0.0.0.0',port="8400",debug=True)