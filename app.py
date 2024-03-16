from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)
from . import models


user_info= {
    "name": "kimdongmin",
    "age": 16,
    "bio": "I'm a web developer.",
    "profile_picture": "picture.jpg"  # 여기에 프로필 사진 파일 이름을 넣으세요.
}

@app.route('/')
def index():
    print(3)
    return render_template('index.html', user=user_info)


if __name__ == '__main__':
    app.run(debug=True)
