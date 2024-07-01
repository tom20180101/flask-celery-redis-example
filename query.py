from celery import Celery
from flask import Flask
from db import db
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend='redis://localhost:6379/2',
        broker='redis://localhost:6379/1',
    )
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args,**kwargs)
    celery.Task = ContextTask
    return celery
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1:3306/sheet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config["SECRET_KEY"] = "2b7beee0ea7e37a1f8e69714b7a56add89957470621111111"
db.init_app(app)
celery_app = make_celery(app)



