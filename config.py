class config():
     # Server Name
    SERVER_NAME  = "127.0.0.1:5000"

    # Database Constant
    SQL_USERNAME = "root"
    SQL_PASSWORD = "lio2619+kh880606"
    SQL_ROUTE    = "localhost"
    SQL_DATABASE = "taiwan_stock"

    # Database Setting
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+SQL_USERNAME+":"+SQL_PASSWORD+"@"+SQL_ROUTE+"/"+SQL_DATABASE

class mail_config():
    # Mail Server
    MAIL_SERVER = 'smtp.gmail.com'

    # Mail Port
    MAIL_PROT = 587
    MAIL_USE_TLS = True

    # Mail Username
    MAIL_USERNAME = 'cs.club2p0@gmail.com'

    # Mail Password
    MAIL_PASSWORD = '&g4AU@;><5;{Q*FZ'

class apscheduler_job_config(object):
    JOBS = [
        {
            'id'                 : 'compare_price',                     #自己設定的id
            'func'               : 'app.user.utils:compare_price',      #要啟動的程式  移動到資料夾後用:來表示要啟動哪個
            'args'               : None,                                #輸入的參數
            'trigger'            : 'cron',                          #interval = 循環   cron = 相對時間
            'day_of_week'        : 'mon-fri',
            'hour'               : '9-12',
            'minute'             : '0-59',
            'second'             : '0',
            'misfire_grace_time' : 10                                   #就算超過時間。只要在10秒內就ok
        }
    ]