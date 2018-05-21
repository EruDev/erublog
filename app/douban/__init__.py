from flask import Blueprint

bp = Blueprint('douban', __name__)

from app.douban import routes