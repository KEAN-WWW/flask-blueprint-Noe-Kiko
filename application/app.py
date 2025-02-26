"""
Initializes Flask app and registers blueprints.
"""
from flask import Flask
from application.bp.homepage.homepage import homepage
# initialize Flask service
app = Flask(__name__)
# register blueprint
app.register_blueprint(homepage)

if __name__ == "__main__":
    app.run(debug=True)

