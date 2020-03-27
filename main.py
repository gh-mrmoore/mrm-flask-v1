from flask import Flask, request, redirect, render_template, session, flash

app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = 'jpfsop0495nfuianrgp019283iuern0n87unrnub098346ounb'

@app.route('/', methods=['POST', 'GET', 'PUT'])   #PUT method is used for updates from form data
def index():
    return render_template('index.html', title="A Little Project")

if __name__ == '__main__':
    app.run()