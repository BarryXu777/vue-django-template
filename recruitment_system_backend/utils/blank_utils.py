def contains_none(*objects) -> bool:
    """
    判断变长参数列表objects是否存在None
    :param objects: 变长参数列表
    :return: 是否存在None
    """
    for o in objects:
        if o is None:
            return True
    return False


def contains_false_val(*objects) -> bool:
    """
    判断变长参数列表objects是否存在布尔值为False的值
    None和空串均视为False
    :param objects: 变长参数列表
    :return: 是否存在布尔值为False的值
    """
    for o in objects:
        if not o:
            return True
    return False