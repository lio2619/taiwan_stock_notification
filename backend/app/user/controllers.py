#controllers 寫要把甚麼東西放到資料庫裡

from app import app
from app import db
from app import ma

from app.user.models import UserTargetPrice
from app.user.models import UserTargetPriceSchema
from app.user.models import UserEmail

from app.utils.request_schema import check_request_json_schema
from app.utils.get_stock_price import read_csv_dict

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
        return make_response(jsonify({'error' : {'missing parameter' : response_body}}), 406)

    data = request.get_json()
    username     = data['username']
    email        = data['email']
    stock_name   = data['stock_name']
    target_price = data['target_price']
    
    stock_code = read_csv_dict(stock_name)
    if not stock_code:
        return make_response(jsonify({'error' : {'wrong stock name' : stock_name}}), 400)

    judge = UserEmail.query.filter_by(email = email).first()

    if not judge:
        user_email = UserEmail(username, email)
        db.session.add(user_email)
        db.session.commit()
        user = UserEmail.query.filter_by(email = email).first()
        
        price = UserTargetPrice(user.id, user.id, stock_name, target_price, stock_code)
        db.session.add(price)
        db.session.commit()

        return make_response(jsonify({'message' : 'no user create all success'}), 200)

    already = UserTargetPrice.query.filter_by(email = judge.id, stock_name = stock_name).first()

    if already:
        already.target_price = target_price
        db.session.commit()
    else:
        price = UserTargetPrice(judge.id, judge.id, stock_name, target_price, stock_code)
        db.session.add(price)
        db.session.commit()

    return make_response(jsonify({'message' : 'already have user add stock success'}), 200)

#查詢該email下的股票
@app.route('/user/get', methods = ['POST'])     #GET需要結合前端
def get_email_stock():
    request_schema = ['email']
    missing, response_body = check_request_json_schema(request_schema, request.json)

    if missing:
        return make_response(jsonify({'error' : {'missing parameter' : response_body}}), 406)

    data = request.get_json()
    email        = data['email']

    user_email = UserEmail.query.filter_by(email = email).first()
    if not user_email:
        return make_response(jsonify({'error' : {'wrong email' : email}}), 400)

    user = UserTargetPrice.query.filter_by(email = user_email.id).all()

    return make_response(jsonify({'data': user_target_price_schema.dump(user)}), 200)

#更新目標價格
@app.route('/user/update', methods = ['PUT'])
def update_target_price():
    request_schema = ['email', 'stock_name', 'target_price']
    missing, response_body = check_request_json_schema(request_schema, request.json)

    if missing:
        return make_response(jsonify({'error' : {'missing parameter' : response_body}}), 406)

    data = request.get_json()
    email        = data['email']
    stock_name   = data['stock_name']
    target_price = data['target_price']

    
    user_email = UserEmail.query.filter_by(email = email).first()
    if not user_email:
        return make_response(jsonify({'error' : {'wrong email' : email}}), 400)

    update_target = UserTargetPrice.query.filter_by(email = user_email.id, stock_name = stock_name).first()
    if not update_target:
        return make_response(jsonify({'error' : {'wrong stock name' : stock_name}}), 400)

    update_target.target_price = target_price

    db.session.commit()

    return make_response(jsonify({'message' : 'update target success'}), 200)