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

@app.route('/work1')
def work1():
    return render_template ('/work/work1.html')
@app.route('/work2')
def work2():
    return render_template ('/work/work2.html')
@app.route('/work3')
def work3():
    return render_template ('/work/work3.html')
@app.route('/work4')
def work4():
    return render_template ('/work/work4.html')
@app.route('/work5')
def work5():
    return render_template ('/work/work5.html')
@app.route('/work6')
def work6():
    return render_template ('/work/work6.html')
@app.route('/work7')
def work7():
    return render_template ('/work/work7.html')
@app.route('/work8')
def work8():
    return render_template ('/work/work8.html')
@app.route('/work9')
def work9():
    return render_template ('/work/work9.html')
@app.route('/work10')
def work10():
    return render_template ('/work/work10.html')
@app.route('/work11')
def work11():
    return render_template ('/work/work11.html')
@app.route('/work12')
def work12():
    return render_template ('/work/work12.html')
@app.route('/work13')
def work13():
    return render_template ('/work/work13.html')
@app.route('/work14')
def work14():
    return render_template ('/work/work14.html')
@app.route('/work15')
def work15():
    return render_template ('/work/work15.html')
@app.route('/work16')
def work16():
    return render_template ('/work/work16.html')
@app.route('/work17')
def work17():
    return render_template ('/work/work17.html')
@app.route('/work18')
def work18():
    return render_template ('/work/work18.html')
@app.route('/work19')
def work19():
    return render_template ('/work/work19.html')
@app.route('/work20')
def work20():
    return render_template ('/work/work20.html')
@app.route('/work21')
def work21():
    return render_template ('/work/work21.html')
@app.route('/work22')
def work22():
    return render_template ('/work/work22.html')
@app.route('/work23')
def work23():
    return render_template ('/work/work23.html')
@app.route('/work24')
def work24():
    return render_template ('/work/work24.html')
@app.route('/work25')
def work25():
    return render_template ('/work/work25.html')
@app.route('/work26')
def work26():
    return render_template ('/work/work26.html')
@app.route('/work27')
def work27():
    return render_template ('/work/work27.html')
@app.route('/work28')
def work28():
    return render_template ('/work/work28.html')