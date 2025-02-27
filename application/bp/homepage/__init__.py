"""Homepage blueprint module"""
from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__, template_folder='templates')

@homepage.route('/')
def home():
    """Default homepage route"""
    return render_template('homepage.html')

@homepage.route('/about')
def about():
    """About page route"""
    return render_template('about.html')