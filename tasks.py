from module.hot import Hot
from query import celery_app
@celery_app.task

def send_email(to,body):
    print(f'Sending email to: {to} with body: {body}')
    return 'Email sent successfully'

@celery_app.task

def insert_data():

    new_hot = Hot(
        detail_id=1,
        view_count=2
    )
    try:
        new_hot.save_to_db()
        print('111111')
    except Exception as e:
        print(e)
        print('22222')

