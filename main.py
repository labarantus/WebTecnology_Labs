from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/full_shop')
def full_shop():
    return render_template('full_shop.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

if __name__ == "__main__":
    app.run(debug=True)