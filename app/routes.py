from flask import  render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
  render_template('index.html', message="what up, mutha sucka!")