from flask import render_template, redirect, url_for, request
from app.models import DouBan
from app.douban import bp
from app import db


@bp.route('/douban', methods=['GET', 'POST'])
def douban():
    page = request.args.get('page', 1, type=int)
    pagination = DouBan.query.order_by(DouBan.title).paginate(page, 10, False)
    doubans = pagination.items
    # print(doubans)
    next_url = url_for('douban.douban', page=pagination.next_num) if pagination.has_next else None
    prev_url = url_for('douban.douban', page=pagination.prev_num) if pagination.has_prev else None
    return render_template('douban.html', doubans=doubans, pagination=pagination, next_url=next_url, prev_url=prev_url)
