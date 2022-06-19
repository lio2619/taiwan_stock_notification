#controllers 寫要把甚麼東西放到資料庫裡

from app import app
from app import db
from app import ma

from app.user.models import UserTargetPrice
from app.user.models import UserEmail

from app.utils.request_schema import check_request_json_schema

from flask import make_response
from flask import jsonify
from flask import request

#創建要找的股票
@app.route('/user/create', methods = ['POST'])
def user_create_target_price():
    request_schema = ['username', 'email', 'stock_name', 'target_price']
    missing, response_body = check_request_json_schema(request_schema, request.json)

    if missing:
        return make_response(jsonify({'error' : {'missing parameter' : response_body}}), 400)

    data = request.get_json()
    username     = data['username']
    email        = data['email']
    stock_name   = data['stock_name']
    target_price = data['target_price']

    judge = UserEmail.query.filter_by(email = email).first()

    if not judge:
        user_email = UserEmail(username, email)
        db.session.add(user_email)
        db.session.commit()
        user = UserEmail.query.filter_by(email = email).first()
        
        price = UserTargetPrice(user.id, user.id, stock_name, target_price)
        db.session.add(price)
        db.session.commit()

        return make_response(jsonify({'message' : 'no user create all success'}), 200)

    price = UserTargetPrice(judge.id, judge.id, stock_name, target_price)
    db.session.add(price)
    db.session.commit()

    return make_response(jsonify({'message' : 'already have user add stock success'}), 200)

#查詢該email下的股票