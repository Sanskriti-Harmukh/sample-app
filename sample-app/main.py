from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def home():
    out = (
        f'Greetings DevOps enthusiasts'
    )
    return out
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')