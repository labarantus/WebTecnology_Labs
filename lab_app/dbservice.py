from lab_app import db

def create_contact_req(json_data):
    try:
        print(json_data)
        db.session.execute(f"INSERT INTO review(name, email, reviewtext) VALUES ('аыва', 'аываа', 'ываа')")
        # Подтверждение изменений в БД
        print('kdlsada')
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

