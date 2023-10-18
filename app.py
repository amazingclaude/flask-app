from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample names for our generator
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie"]
last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Miller"]

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ""
    if request.method == 'POST':
        name = random.choice(first_names) + " " + random.choice(last_names)
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
