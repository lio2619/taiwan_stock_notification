#utils = 寫controller裡面會用到的程式

from app import app
from app import db
from app import ma

from app.user.models import UserTargetPrice
from app.user.models import UserEmail

from app.utils.get_stock_price import stock_price

#比較目標價與目前價
def compare_price():
    stock = []
    counts = UserEmail.query.count()
    
    for count in range(1, counts + 1):
        user_email = UserEmail.query.get(count)
        users = UserTargetPrice.query.filter_by(email = user_email.id, already_send = 0).all()

        for user in users:
            currently_price = stock_price(user.stock_code)[1:]

            if float(currently_price) >= float(user.target_price):
                stock.append([user.stock_name, user.target_price, user_email.email])
                user.already_send = 1
                db.session.commit()
    print(stock)
    return stock