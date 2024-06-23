import json
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from account_sys.models import *
from utils.blank_utils import contains_false_val, contains_none
from utils.email_utils import valid_email
from utils.response_utils import *
from utils.session_utils import *

# Create your views here.
@csrf_exempt
def register(request):
    if request.method != 'POST':
        return method_disallowed_response(request.method, 'POST')
    if has_login(request):
        user: User = get_login_user(request)
        return login_status_response(user.to_dict(), actual_login_status=True)
    
    data = json.loads(request.body)
    user_name = data.get('user_name')
    email = data.get('email')
    password = data.get('password')

    if contains_none(user_name, email, password):  # 不存在该键
        return format_error_response()

    if contains_false_val(user_name, email, password):  # 为空串
        return build_response(errno=2001, msg="user_name, email, password均不能为空")

    if not (2 <= len(user_name) <= 31) or valid_email(user_name):  # 不可以使用邮箱格式的用户名
        return build_response(errno=2002, msg="用户名不合法")

    if not (6 <= len(email) <= 63) or not valid_email(email):
        return build_response(errno=2003, msg="邮箱不合法")

    if not (4 <= len(password) <= 31):
        return build_response(errno=2004, msg="密码不合法")

    if User.objects.filter(name=user_name).exists():
        return build_response(errno=2005, msg="用户名已存在")

    if User.objects.filter(email=email).exists():
        return build_response(errno=2006, msg="邮箱已存在")

    User.objects.create(name=user_name, email=email, password=password)
    return build_response(msg="注册成功")

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return method_disallowed_response(request.method, 'POST')

    if has_login(request):
        user = get_login_user(request)
        return login_status_response({
            "user": user.to_dict()
        }, actual_login_status=True)

    data = json.loads(request.body)
    account = data.get('account') # 用户名或邮箱
    password = data.get('password')

    if contains_none(account, password):  # 不存在该键
        return format_error_response()

    if contains_false_val(account, password):  # 为空串
        return build_response(errno=2001, msg="account, password均不能为空")

    # 获取user对象和登录方式（user_name或email），获取失败则user置为None
    cur_login_method = "email" if valid_email(account) else "name"
    try:
        user = User.objects.get(**{cur_login_method: account})
    except User.DoesNotExist:
        user = None

    if user is None:
        return build_response(errno=2002, msg="账户不存在")

    if password != user.password:
        return build_response({
            "login_method": cur_login_method
        }, errno=2003, msg="密码错误")

    set_login_user(request, user)
    return build_response({
        "login_method": cur_login_method,
        "user": user.to_dict()
    }, msg="登录成功")

@csrf_exempt
def logout(request):
    if request.method != 'POST':
        return method_disallowed_response(request.method, 'POST')

    if not has_login(request):
        return login_status_response()

    del_login_user(request)
    return build_response(msg="登出成功")

@csrf_exempt
def get_current_user(request):
    if request.method not in ['POST', 'GET']:
        return method_disallowed_response(request.method, 'POST', 'GET')

    if not has_login(request):
        return login_status_response()

    user = get_login_user(request)

    return build_response({
        "user": user.to_dict()
    }, msg="获取成功")