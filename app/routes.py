from flask import render_template, request, send_from_directory

from app import app
#
# @app.route('/')
# def root():
#     return app.send_static_file('/templates/index.html')



@app.route('/')
def index():
    return render_template('index.html', title='Home')
@app.route('/price')
def price():
    return render_template('price.html', title='Price')

