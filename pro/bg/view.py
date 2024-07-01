from flask import Blueprint
from tasks import insert_data
bg= Blueprint('bg',__name__)
@bg.route('/123')
def insert():
    task =insert_data.delay()
    print('1122222')
    print(task.id)
    return {
               "message": "11212123"
           },200