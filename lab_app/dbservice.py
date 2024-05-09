from lab_app import db
from lab_app import Review
from lab_app import app

def create_contact_req(json_data):
    with app.app_context():
        try:
            print(json_data)
            new_review = Review(name=json_data['client_name'], email=json_data['client_email'], reviewtext=json_data['rev_message'])
            db.session.add(new_review)
        # Подтверждение изменений в БД
            print('Added')
            db.session.commit()
            print('All Right.')
            # Возвращаем результат
            return {'message': "ContactRequest Created!"}
        # если возникла ошибка запроса в БД
        except Exception as e:
            # откатываем изменения в БД
            db.session.rollback()
            # возвращаем dict с ключом 'error' и текcтом ошибки
            return {'message': str(e)}

