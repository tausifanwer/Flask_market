from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template("market.html",items=items)

















# @app.route('/about')
# def about():
#     return "<h1>This about page</h1>"
# # Dynamic route
# @app.route('/about/<username>')
# def about_username(username):
#     return f"<h1>This username is {username}</h1>"


app.run(debug=True)