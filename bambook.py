from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index')
@app.route( '/bambook')
def bambook():
    return '''
    <!DOCTYPE html>
<html>
    <head>
        <title>Main page</title>
    </head>
    <body>
        <br>
         <img src=" " alt="">" alt="">
        <br>
        <p>Bamboook!</p>
        <hr><hr><hr>
    </body>
</html>
'''
app.run(debug=True)