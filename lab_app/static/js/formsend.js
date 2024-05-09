/*
Реализация AJAX с помощью асинхронного метода fetch. Современный вариант реализации AJAX.
*/

var sendbtn = document.getElementById("sendbtn");    // выбираем DOM-елемент (кнопку)

// Привязываем к элементу обработчик события "click"
if(sendbtn)
{
    sendbtn.addEventListener("click", function (e) {
        /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
        если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
        e.preventDefault();
        // Получаем данные полей формы
        let name = document.getElementsByName("name")[0].value;
        let email = document.getElementsByName("email")[0].value;
        let message = document.getElementsByName("message")[0].value;
        // Преобразуем полученные данные в JSON
        if (name == '' || message == '') 
            alert("Заполните обязательные поля");
        else { 
            var formdata = JSON.stringify({ client_name: name, client_email: email, rev_message: message});
            
            // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
            fetch("/api/client_review",
            {
                method: "POST",
                body: formdata,
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then( response => {
                // fetch в случае успешной отправки возвращает Promise, содержащий response объект (ответ на запрос)
                // Возвращаем json-объект из response и получаем данные из поля message
                response.json().then(function(data) {
                    console.log(data)
                    let respond_message = document.getElementById("respond_message");
                    respond_message.textContent = data.message;
                    //statfield.textContent.bold();
                    //alert(data.message);
                });
            })
            .catch( error => {
                alert(error);
                console.error('error:', error);
            });
        }
    });
}

