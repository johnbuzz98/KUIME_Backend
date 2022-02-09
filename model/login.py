from flask import render_template, redirect, request, url_for
#from app import app
from flask_login import login_user, logout_user
#from model.model_menu import Menu
from model.model_user import User



#로그인 상태와 관련된 함수들
#사용자 정보 조회하는 함수
@login_manager.user_loader
def user_loader(user_id):
    # 사용자 정보 조회
    user_info = User.get_user_info(user_id)
    login_info = User(user_id=user_info['data'][0]['USER_ID'])

    return login_info


# login_required로 요청된 기능에서 현재 사용자가 로그인되어 있지 않은 경우
@login_manager.unauthorized_handler
def unauthorized():
    # 로그인되어 있지 않은 사용자일 경우 첫화면으로 이동
    return redirect("/") #바꿀수 있음


# 로그인 실행 함수

# 로그인 계정 정보는 post로 받아오지만
# 일반 리소스들은 get으로 받아오므로 get과 post모두 선언해줘야 한다.
@app.route('/login/get_info', methods=['GET', 'POST'])
def login_get_info():
    user_id = request.form.get('userID')
    user_pw = request.form.get('userPW')

    if user_id is None or user_pw is None:
        return redirect('/relogin')#이거는 바꿀 수 있음

    # 사용자가 입력한 정보가 회원가입된 사용자인지 확인
    user_info = User.get_user_info(user_id, user_pw)

    if user_info['result'] != 'fail' and user_info['count'] != 0:
        # 사용자 객체 생성
        login_info = User(user_id=user_info['data'][0]['USER_ID'])
        # 사용자 객체를 session에 저장
        login_user(login_info)
        return redirect('/main')
    else:
        return redirect('/relogin')


# 로그인 실패 시 재로그인
@app.route('/relogin')
def relogin():
    login_result_text = "로그인에 실패했습니다. 다시 시도해주세요."

    return #팝업 모듈

# 로그아웃
# session 정보를 삭제한다.
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')