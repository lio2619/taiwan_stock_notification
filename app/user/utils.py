#utils = 寫controller裡面會用到的程式

from app import app
from app import db
from app import ma

from app.user.models import UserTargetPrice
from app.user.models import UserEmail
from app.user.models import UserStockPrice

from app.utils.get_stock_price import stock_price
from app.utils.send_mail import send_mail

#比較目標價與目前價
def compare_price():
    stock = []
    counts = UserEmail.query.count()
    
    for count in range(1, counts + 1):
        user_email = UserEmail.query.get(count)
        users = UserTargetPrice.query.filter_by(email = user_email.id).all()
        
        if not users:
            continue
        
        for user in users:
            try:
                user_stock_price = UserStockPrice.query.filter_by(stock_code = user.stock_code).first()
                currently_price = user_stock_price.stock_price
            except:
                currently_price = stock_price(user.stock_code)[1:]
                price = UserStockPrice(user.stock_code, currently_price)
                db.session.add(price)
                db.session.commit()

            if float(currently_price) >= float(user.target_price):
                stock.append([user.stock_name, user.target_price])
                db.session.delete(user)
                db.session.commit()
        #寄信
        if stock:
            mail_message = ''
            mail_title = '{}先生/小姐，您所設定的目標價格已經達到'.format(user_email.username)
            
            for i in stock:
                mail_message += '●{name}已經到達目標價格{price}\n'.format(name = i[0], price = i[1])

            send_mail(mail_title, user_email.email, mail_message)

#刪除比對資料庫
def delete_stock_price_db():
    users = UserStockPrice.query.all()

    for user in users:
        db.session.delete(user)
        db.session.commit()