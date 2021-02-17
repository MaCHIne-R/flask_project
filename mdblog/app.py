from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def about_page():
    return render_template("about_page.jinja")

@flask_app.route("/admin/")
def admin_page():
    return render_template("admin_page.jinja")

@flask_app.route("/articles/")
def article_page():
    return render_template("articles_page.jinja")
