#controllers 寫要把甚麼東西放到資料庫裡

from re import L
from app import app
from app import db
from app import ma

from app.user.models import UserTargetPrice
from app.user.models import UserTargetPriceSchema
from app.user.models import UserEmail

from app.utils.request_schema import check_request_json_schema

from flask import make_response
from flask import jsonify
from flask import request

user_target_price_schema = UserTargetPriceSchema(many = True)       #如果用.all()就要用many = True

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
@app.route('/user/get', methods = ['POST'])     #GET需要結合前端
def get_email_stock():
    request_schema = ['email']
    missing, response_body = check_request_json_schema(request_schema, request.json)

    if missing:
        return make_response(jsonify({'error' : {'missing parameter' : response_body}}), 400)

    users_dict = {}

    data = request.get_json()
    email        = data['email']

    users_email = UserEmail.query.all()

    for user_email in users_email:
        users_dict[user_email.email] = user_email.id

    user = UserTargetPrice.query.filter_by(email = users_dict[email]).all()

    return make_response(jsonify({'data': user_target_price_schema.dump(user)}), 200)

#更新目標價格
@app.route('/user/update', methods = ['PUT'])
def update_target_price():
    request_schema = ['email', 'stock_name', 'target_price']
    missing, response_body = check_request_json_schema(request_schema, request.json)

    if missing:
        return make_response(jsonify({'error' : {'missing parameter' : response_body}}), 400)

    users_dict = {}
    users__price_dict = {}

    data = request.get_json()
    email        = data['email']
    stock_name   = data['stock_name']
    target_price = data['target_price']

    users_email = UserEmail.query.all()

    for user_email in users_email:
        users_dict[user_email.email] = user_email.id

    users_target = UserTargetPrice.query.all()

    for user_target in users_target:
        users__price_dict[user_target.email, stock_name] = user_target

    update_target = users__price_dict[users_dict[email], stock_name]
    update_target.target_price = target_price

    db.session.commit()

    del users_dict
    del users__price_dict

    return make_response(jsonify({'message' : 'update target success'}), 200)