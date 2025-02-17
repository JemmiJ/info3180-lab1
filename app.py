from flask import Flask, render_template, url_for

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''
@app.route('/')
def home():
    return 'My home page'

@app.route('/about')
def about():
    image_urls = [url_for('static', filename='images/anya_forger.jpg'), url_for('static', filename='images/kiki.jpg')]

    return render_template('about.html', images=image_urls)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
