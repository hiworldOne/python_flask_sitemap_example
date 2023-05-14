from flask import Flask, url_for
from flask_sitemap import Sitemap

# flask object
app = Flask(__name__)

# sitemap object
ext = Sitemap(app=app)

# http or https, default is http
app.config['SITEMAP_URL_SCHEME'] = 'https'


@app.route('/')
def index():
    """
    home page
    :return: html home page
    """
    html = f"""
        <p><a href="https://hiworld.one/">hiworld</a></p>
        <p><a href="/sitemap.xml">sitemap</a></p>
        <p><a href="{url_for('about')}">about</a></p>
        """
    for i in range(1, 11):
        html += f"""
        <p><a href="{url_for('location', number=i)}">location {i}</a></p>
        """
    return html


@app.route('/about/')
def about():
    """
    page about
    :return: html about page
    """
    return '<p>about</p>'


@app.route('/location/<int:number>/')
def location(number):
    """
    page location
    :param number: number location
    :return: html location number page
    """
    return f'<p>location {number}</p>'


@ext.register_generator
def sitemap():
    """
    generator sitemap
    :return: sitemap.xml
    """
    # sitemap index
    yield 'index', {}
    # sitemap about
    yield 'about', {}
    # sitemap location for number
    for i in range(1, 11):
        yield 'location', {'number': i},


if __name__ == '__main__':
    app.run(debug=True)
