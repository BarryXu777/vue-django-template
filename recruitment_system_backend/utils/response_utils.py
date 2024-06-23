from typing import Optional
from django.http import JsonResponse


def build_response(other_info: Optional[dict] = None,
                   *, errno: int = 1, msg: str = "操作成功", status: int = 200):
    """
    生成响应体
    :param other_info: Json响应体的其它信息
    :param errno: 错误码
    :param msg: 提示信息
    :param status: http状态码
    :return: Json响应体
    """
    if other_info is None:
        other_info = {}
    response_dict = {
        "errno": errno,
        "msg": msg,
    }
    response_dict.update(other_info)
    return JsonResponse(response_dict, status=status)


def method_disallowed_response(current_method: str, *allowed_methods: str, errno: int = 1001, status: int = 400) -> JsonResponse:
    """
    生成响应体：请求方式错误
    :param current_method: 当前的请求方式
    :param allowed_methods: 允许的请求方式列表
    :param errno: 错误码
    :param status: http状态码
    :return: Json响应体
    """
    return JsonResponse({
        "errno": errno,
        "msg": "请求方式错误",
        "current_method": current_method,
        "allowed_methods": allowed_methods
    }, status=status)


def format_error_response(*, errno: int = 1002, msg: str = "请求体格式错误", status: int = 400) -> JsonResponse:
    """
    生成响应体：请求体格式错误
    :param errno: 错误码
    :param msg: 提示信息
    :param status: http状态码
    :return: Json响应体
    """
    return JsonResponse({
        "errno": errno,
        "msg": msg
    }, status=status)


def login_status_response(other_info: Optional[dict] = None, *, actual_login_status: bool = False, errno: int = 1003, status: int = 200) -> JsonResponse:
    """
    生成响应体：登录状态异常
    :param other_info: Json响应体的其它信息
    :param actual_login_status: 实际登录状态（错误的登录状态）
    :param errno: 错误码
    :param status: http状态码
    :return: Json响应体
    """

    if other_info is None:
        other_info = {}
    response_dict = {
        "errno": errno,
        "msg": "当前已登录" if actual_login_status else "当前未登录",
    }
    response_dict.update(other_info)
    return JsonResponse(response_dict, status=status)

