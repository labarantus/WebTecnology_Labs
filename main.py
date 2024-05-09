from flask import Flask, render_template, url_for, json, request, Response, jsonify, make_response
app = Flask(__name__)

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


# Обработка POST-за
# проса для демонстрации AJAX
@app.route('/api/client_review', methods=['POST'])
def post_review():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'client_name'
    if not 'client_name' in request.json or not request.json: 
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе отправляем json-ответ
    else:
        msg = request.json['client_name'] + ", thank you for your feedback!"
        return json_response({ 'message': msg })
    
# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)
   
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

if __name__ == "__main__":
    app.run(debug=True)