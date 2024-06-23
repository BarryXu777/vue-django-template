from typing import Optional

from django.core.handlers.wsgi import WSGIRequest

from account_sys.models import User


def has_login(request: WSGIRequest) -> bool:
    """
    判断当前是否已登录
    :param request: 请求体
    :return: 当前是否已登录
    """
    return "user_id" in request.session


def _get_login_id(request: WSGIRequest) -> Optional[int]:
    """
    获取当前登录的用户id，前置条件：已登录
    :param request: 请求体
    :return: 用户id
    """
    assert has_login(request)
    return request.session.get("user_id")


def get_login_user(request: WSGIRequest) -> User:
    """
    获取当前登录的用户，前置条件：已登录
    :param request: 请求体
    :return: 用户
    """
    return User.objects.get(id=_get_login_id(request))


def _set_login_id(request: WSGIRequest, user_id: str) -> None:
    """
    设置当前登录的用户id
    :param request: 请求体
    :param user_id: 用户id
    :return: None
    """
    request.session["user_id"] = user_id

def set_login_user(request: WSGIRequest, user: User) -> None:
    """
    设置当前登录的用户
    :param request: 请求体
    :param user: 用户
    :return: None
    """
    _set_login_id(request, user.id)


def del_login_user(request: WSGIRequest) -> None:
    """
    删除当前登录的用户
    :param request: 请求体
    :return: None
    """
    del request.session["user_id"]
