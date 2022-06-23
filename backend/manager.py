from app import app
from app import db
from app import manager

if __name__ == '__main__':
    db.create_all()
    manager.run()