from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Render the items page with data from items.json"""
    try:
        with open('items.json') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except Exception:
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
