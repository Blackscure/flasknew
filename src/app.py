from flask import Flask, render_template

app = Flask(__name__)  # '__main__'


@app.route('/home')
def hello_method():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
   

if __name__ == '__main__':
    app.run(port=5000)


