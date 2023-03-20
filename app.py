class Tours:
    def __init__(self, name, desc, dats):
        self.name = name
        self.description = desc
        self.dates = dats

array = []
array.append(Tours("Из Петербурга в Москву", "Наведаться в некультурную столицу никогда не поздно, мы предоставляем такую возможность.", "01.05.2023-09.01.2023"))
array.append(Tours("Из Москвы в Петербург", "Наведаться в культурную столицу никогда не поздно, мы предоставляем такую возможность.", "10.05.2023-18.01.2023"))
array.append(Tours("Из Новосибирска в Пхеньян", "Вынуждены Вас предупредить, это может быть туром в 1 конец, и отнюдь не потому, что Вам там понравится.)", "30.09.2024-16.01.2024"))
array.append(Tours("В прошлое", "Да, тур в прошлое. Я могу тут писать что угодно, задание на знание библиотеки, это всё равно никто не читает...", "01.01.2025-01.01.2024"))
array.append(Tours("В последний спокойный год", "Все ещё думали о коронавирусе и считали Украинцев нашими друзьями на веки.", "01.01.2025-01.01.2021"))
array.append(Tours("Назад в будущее, ёпта", "Потому что могу, да и отсылку к хорошей серии фильмов грех не вставить.", "17.01.2021-17.01.2025"))
path = "http://127.0.0.1:5000/"

import flask

app = flask.Flask(__name__)

@app.route('/')
def welcome():
    return flask.render_template('welcome.html', a = path + "list_tours/0")

@app.route('/list_tours/<int:a>')
def tours(a):
    if a == 0:
        return flask.render_template('list_tours0.html', a = path + "list_tours/", name0 = array[0].name, desc0 = array[0].description, dats0  = array[0].dates, name1 = array[1].name, desc1 = array[1].description, dats1  = array[1].dates)
    if a == 1:
        return flask.render_template('list_tours1.html', a = path + "list_tours/", name = array[2].name, desc = array[2].description, dats  = array[2].dates)
    else :
        return flask.render_template('list_tours2.html', a = path + "list_tours/", name0 = array[3].name, desc0 = array[3].description, dats0  = array[3].dates, name1 = array[4].name, desc1 = array[4].description, dats1  = array[4].dates, name2 = array[5].name, desc2 = array[5].description, dats2  = array[5].dates)

@app.route('/one_tour/<int:a>')
def tour(a):
    return flask.render_template('one_tour.html', name = array[a].name, desc = array[a].description, dats = array[a].dates, vk = "https://vk.com/id505817337")

app.run()