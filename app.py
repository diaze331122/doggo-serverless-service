from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql.functions import now

app = Flask(__name__)
app.config.from_object('configurations.config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Event(db.Model):
    __tablename__ = 'events'

    id = mapped_column(Integer, primary_key=True)
    category = mapped_column(String(255), nullable=False)
    message = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, server_default=now())

    def __init__(self, category, message):
        self.category = category
        self.message = message


@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event(category=data['category'], message=data['message'])
    db.session.add(event)
    db.session.commit()
    return "Ok", 200


if __name__ == '__main__':
    app.run()
