from ..exceptions import BadColorError, BadFormatError


def code(*id):
    """
    generate an ANSI escape code composed of the parameters pased on id
    :param id: al SGR parameters included in the result
    :return: ANSI escape code
    """
    cleared_ids = []
    final = ""
    for x in id:
        if isinstance(x, list) and x:
            identifier, r, g, b = x
            cleared_ids += [identifier, 2, r, g, b]
        elif x or x == 0:
            if x not in cleared_ids:
                if isinstance(x, set):
                    for y in x:
                        cleared_ids.append(y)
                    continue
                cleared_ids.append(x)
            # "\033[38;2;125;52;235;4m hello"
    for i, x in enumerate(cleared_ids):
        if i == cleared_ids.__len__() - 1:
            final += str(x)
        else:
            final += str(x) + ";"
    final = f"\033[{final}m"
    return final
