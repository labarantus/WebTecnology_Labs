from labapp import app
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json
from . import dbservice    # подключение модуля с CRUD-методами для работы с БД из локального пакета
from collections import OrderedDict


subjs = ["Furniture", "Shop", "About Us", "Review"]
links = ["index", "shop", "about_us", "review"]

chairs_names = ["Sakarias Armchair", "Baltsar Chair", "Anjay Chair", "Nyantuy Chair"]
chairs_pics = ["Chair1.png","Chair2.png","Chair3.png","Chair4.png"]
chairs_prices = ["$392", "$299", "$519", "$921"]
chairs_scores = ["3.7", "2.9", "5", "4.9"]

rev_bg_pics = ["rev1.png","rev2.png","rev3.png"]
cl_pics = ["client1.png","client2.png","client3.png"]
cl_names = ["Bang Upin","Ibuk Sukijan","Mpok Ina"]
cl_jobs = ["Pedagang Asongan","Ibu Rumah Tangga","Karyawan Swasta"]
rev_texts = ["Terimakasih banyak, kini ruanganku menjadi lebih mewah dan terlihat mahal",
                 "Makasih Panto, aku sekarang berasa tinggal di apartment karena barang-barang yang terlihat mewah",
                 "Sangat terjangkau untuk kantong saya yang tidak terlalu banyak"]



@app.route('/')
def index():
    return render_template('index.html', subjs_links = zip(subjs, links), title="Panto")

@app.route('/full_shop')
def full_shop():
    return render_template('full_shop.html', subjs_links = zip(subjs, links), title="Full Shop",
                           chairs = zip(chairs_names, chairs_pics, chairs_prices, chairs_scores))

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', subjs_links = zip(subjs, links), title="About Us")

@app.route('/review')
def review():
    return render_template('review.html', subjs_links = zip(subjs, links),
                           reviews = zip(rev_bg_pics, cl_pics, cl_names, cl_jobs, rev_texts), title="Review")

@app.route('/shop')
def shop():
    categories = ["Chair", "Beds", "Sofa", "Lamp"]
    return render_template('shop.html', subjs_links = zip(subjs, links), categories=categories,
                           chairs = zip(chairs_names, chairs_pics, chairs_prices), title="Shop")

@app.route('/api/contactrequest', methods=['GET'])
# Получаем все записи contactrequests из БД
def get_contact_req_all():
    response = dbservice.get_contact_req_all()
    return json_response(response)


@app.route('/api/contactrequest/<int:id>', methods=['GET'])
# Получаем запись по id
def get_contact_req_by_id(id):
    response = dbservice.get_contact_req_by_id(id)
    print(json_response(response))
    return jsonify(response)

# json(object_pairs_hook=OrderedDict)


@app.route('/api/contactrequest/author/<string:name>', methods=['GET'])
# Получаем запись по имени пользователя
def get_get_contact_req_by_author(name):
    if not name:
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
        # Иначе отправляем json-ответ
    else:
        response = dbservice.get_contact_req_by_author(name)
    return json_response(response)

# Обработка POST-за
# проса для демонстрации AJAX
@app.route('/api/client_review', methods=['POST'])
def create_contact_req():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'client_name'
    if not request.json or not 'client_name' or not 'rev_message' in request.json : 
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе отправляем json-ответ
    else:
        # msg = request.json['client_name'] + ", thank you for your feedback!"
        # return json_response({ 'message': msg })
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        response = dbservice.create_contact_req(request.json)
        return json_response(response)
    
@app.route('/api/contactrequest/<int:id>', methods=['PUT'])
# Обработка запроса на обновление записи в БД
def update_contact_req_by_id(id):
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'reqtext'
    if not request.json or not 'message' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе обновляем запись в БД и отправляем json-ответ
    else:
        response = dbservice.update_contact_req_by_id(id, request.json)
        return json_response(response)


@app.route('/api/contactrequest/<int:id>', methods=['DELETE'])
# Обработка запроса на удаление записи в БД по id
def delete_contact_req_by_id(id):
    response = dbservice.delete_contact_req_by_id(id)
    return json_response(response)

# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)
   
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))