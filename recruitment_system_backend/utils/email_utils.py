import re


def valid_email(email: str) -> bool:
    """
    正则表达式验证邮箱是否合法
    :param email: 邮箱名
    :return: 邮箱是否合法
    """
    if re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', email):
        return True
    else:
        return False