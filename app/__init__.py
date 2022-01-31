from flask import Flask
from flask_login import LoginManager

def create_app():
    # 앱 설정
    app = Flask(__name__)
    login_manager = LoginManager()
    login_manager.init_app(app)  # app 에 login_manager 연결
    return app


# flask_login에서 제공하는 login_required를 실행하기 전 사용자 정보를 조회한다.
@login_manager.user_loader
def user_loader(user_id):
    # 사용자 정보 조회
    user_info = User.get_user_info(user_id)
    # user_loader함수 반환값은 사용자 '객체'여야 한다.
    # 결과값이 dict이므로 객체를 새로 생성한다.
    login_info = User(user_id=user_info['data'][0]['USER_ID'])

    return login_info


# login_required로 요청된 기능에서 현재 사용자가 로그인되어 있지 않은 경우
# unauthorized 함수를 실행한다.
@login_manager.unauthorized_handler
def unauthorized():
    # 로그인되어 있지 않은 사용자일 경우 첫화면으로 이동
    return redirect("/")

