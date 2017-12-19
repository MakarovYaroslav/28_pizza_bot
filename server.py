from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib import sqla
from models import Pizza, Choice
from werkzeug.exceptions import HTTPException
from os import getenv


app = Flask(__name__)

app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class ModelView(sqla.ModelView):
    def is_accessible(self):
        unauthorized_status_code = 401
        auth = request.authorization
        if not auth or (auth.username, auth.password) != (getenv('USERNAME'), getenv('PASSWORD')):
            raise HTTPException('', Response(
                "Введите корректные имя пользователя и пароль!",
                unauthorized_status_code,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            ))
        return True


class PizzaView(ModelView):
    column_searchable_list = ['title']
    column_labels = dict(title='Название',
                         description='Описание',
                         choices='Варианты')


class ChoiceView(ModelView):
    column_default_sort = 'price'
    column_labels = dict(title='Размер пиццы', price='Стоимость')


admin = Admin(app, name='Пиццерия', template_mode='bootstrap3')
admin.add_view(PizzaView(Pizza, db.session, name='Пицца'))
admin.add_view(ChoiceView(Choice, db.session, name='Варианты'))


if __name__ == '__main__':
    app.run()
