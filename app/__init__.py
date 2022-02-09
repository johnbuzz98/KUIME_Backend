from flask import Flask
from flask_login import LoginManager

def create_app():
    # 앱 설정
    app = Flask(__name__)
    login_manager = LoginManager()
    login_manager.init_app(app)  # app 에 login_manager 연결
    return app




# @login_required (로그인이 필요한 기능 앞에다 staticmethod 형식으로 선언해주면 됨
# 해당방식은 세션 유지 정보를 통해 로그인된 상태인지 확인 (보안성 조금 떨어짐)

# is.authenticated로 구현하면 직접 확인하는 방식으로도 가능
# current_user.is_authenticated