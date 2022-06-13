class config():
     # Server Name
    SERVER_NAME  = "127.0.0.1:5000"

    # Database Constant
    SQL_USERNAME = "root"
    SQL_PASSWORD = "lio2619+kh880606"
    SQL_ROUTE    = "localhost"
    SQL_DATABASE = "taiwan_stock"

    # Database Setting
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