styles = [
    ["╔", "═", "╗", "║", "╚", "╝"],
    ["╭", "─", "╮", "│", "╰", "╯"],
    ["+", "-", "+", "|", "+", "+"],
    ["#", "#", "#", "#", "#", "#"],
]


def string_frame(str, style: int = 0, padding: int = 1):
    str_s = str.split("\n")
    max_len = 0
    for i in str_s:
        current_len = len(i)
        if current_len > max_len:
            max_len = current_len
    res = [(styles[style][0]
        + (styles[style][1] * (max_len + (padding * 2))) + styles[style][2])]
    for i in str_s:
        space = max_len - len(i) + padding
        res.append(
            styles[style][3] + (" " * padding) + i + (" " * space) + styles[style][3]
        )
    res.append(
        styles[style][4]
        + (styles[style][1] * (max_len + (padding * 2)))
        + styles[style][5]
    )
    return "\n".join(res)
