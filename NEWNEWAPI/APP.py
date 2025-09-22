from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Дані
cars = [
    {"car brand": "Mercedes", "model": "G-Class", "color": "Black", "price": "$50000"},
    {"car brand": "BMW", "model": "X5", "color": "White", "price": "$40000"},
    {"car brand": "Audi", "model": "Q7", "color": "Blue", "price": "$45000"},
    {"car brand": "Toyota", "model": "Camry", "color": "Silver", "price": "$30000"},
    {"car brand": "Honda", "model": "Civic", "color": "Red", "price": "$25000"},
    {"car brand": "Ford", "model": "Mustang", "color": "Yellow", "price": "$55000"},
    {"car brand": "Chevrolet", "model": "Camaro", "color": "Blue", "price": "$50000"},
    {"car brand": "Nissan", "model": "Altima", "color": "Black", "price": "$28000"},
    {"car brand": "Volkswagen", "model": "Golf", "color": "White", "price": "$22000"},
    {"car brand": "Porsche", "model": "911", "color": "Red", "price": "$120000"}
]
colors = [
    {"id": 1, "name": "Червоний", "number": "#ff0066"},
    {"id": 2, "name": "Зелений", "number": "#008000"},
    {"id": 3, "name": "Чорний", "number": "#000000"},
    {"id": 4, "name": "Синій", "number": "#0000cc"},
    {"id": 5, "name": "Коричневий", "number": "#a52a2a"},
    {"id": 6, "name": "Блакитний", "number": "#33ccff"},
    {"id": 7, "name": "Жовтий", "number": "#ffff66"},
    {"id": 8, "name": "Рожевий", "number": "#ffc0cb"},
    {"id": 9, "name": "Білий", "number": "#ffffff"},
    {"id": 10, "name": "Оранжевий", "number": "#ffa500"}
]

tips = [
    "Вчися щодня по 30 хв.",
    "Роби перерви під час роботи.",
    "Пий більше води."
    "Раз на рік проходьте загальне медичне обстеження.",
    "Говоріть людям компліменти, будьте доброзичливі.",
    "Займайтеся спортом 2-3 рази на тиждень по 1 годині.",
    "Тренуйте мізки: вчіть вірші, розгадуйте кросворди, грайте в шахи.",
    "Щодня приділяйте читанню хоча б 30 хвилин.",
    "Пийте достатню кількість чистої, негазованої води: не менше 1500 мл на день.",
    "Провітрюйте кімнату перед сном. Спіть в прохолоді.",
    "Робіть гімнастику для очей.",
    "Вивчайте 10 іноземних слів щодня."
]

riddles = [
    {"question": "Хто ходить без ніг?", "answer": "час", "hint": "Він завжди рухається вперед"},
    {"question": "Що більше, чим менше?", "answer": "яма", "hint": "Коли копаєш глибше..."},
    {"question": "Хто говорить усіма мовами?", "answer": "луна", "hint": "Повторює те, що чує"},
    {"question": "Що росте донизу?", "answer": "бурулька", "hint": "Зимова краса"},
    {"question": "З якого крана не можна помити руки?", "answer": "будівельного", "hint": "він дуже великий"},
    {"question": "Скільки та які місяці мають по 28 днів?", "answer": "всі 12 місяців", "hint": "не тільки лютий"},
    {"question": "Чим більше з неї береш, тим більшою вона стає.", "answer": "Яма", "hint": "на дорогах"}
]
songs = [
   {"title": "Червона рута", "emoji": "🌹"},
   {"title": "Пісня про рушник", "emoji": "🧵"},
   {"title": "Океан Ельзи — Все буде добре", "emoji": "🌊"},
   {"title": "Несе Галя воду", "emoji": "💧"},
   {"title": "Ой на горі два дубки", "emoji": "🌳"},
   {"title": "Щедрик", "emoji": "✨"}
]

fairy_tales = [
   {"title": "Івасик-Телесик", "characters": ["Івасик-Телесик", "мати", "змія", "качка"], "emoji": "🦆"},
   {"title": "Котигорошко", "characters": ["Котигорошко", "змій", "брати", "кінь", "дівчина"], "emoji": "🌱"},
   {"title": "Лисичка-сестричка", "characters": ["лисиця", "вовк", "ведмідь"], "emoji": "🦊"},
   {"title": "Пан Коцький", "characters": ["кіт", "заєць", "вовк", "ведмідь", "кабан"], "emoji": "🐱"},
   {"title": "Кривенька качечка", "characters": ["качечка", "дід", "баба"], "emoji": "🐥"}
]


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/random_car')
def random_car():
    return jsonify(random.choice(cars))

@app.route('/random_color')
def random_color():
    return jsonify(random.choice(colors))

@app.route('/tip')
def get_tip():
    return jsonify({"tip": random.choice(tips)})

@app.route('/calculate')
def calculate():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    return jsonify({"num1": num1, "num2": num2, "result": num1 + num2})

@app.route('/subtract')
def subtract():
    num3 = float(request.args.get('num3', 0))
    num4 = float(request.args.get('num4', 0))
    result = num3 - num4
    return jsonify({"num3": num3, "num4": num4, "result": result})

@app.route('/multiply')
def multiply():
    num5 = float(request.args.get('num5', 0))
    num6 = float(request.args.get('num6', 0))
    result = num5 * num6
    return jsonify({"num5": num5, "num6": num6, "result": result})

@app.route('/divide')
def divide():
    num7 = float(request.args.get('num7', 0))
    num8 = float(request.args.get('num8', 1))  # щоб уникнути ділення на 0
    if num8 == 0:
        return jsonify({"error": "Ділення на нуль заборонене!"}), 400
    result = num7 / num8
    return jsonify({"num7": num7, "num8": num8, "result": result})

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Гість')
    age = request.args.get('age', '???')
    return jsonify({"greeting": f"Привіт, {name}! Тобі {age} років."})

if __name__ == '__main__':
    app.run(debug=True)
