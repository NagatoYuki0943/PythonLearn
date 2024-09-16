import re


def tokenize(text):
    """
    英文句子分成单个的单词,去除标点符号
    """

    # fileters = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    fileters = [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "\(",
        "\)",
        "\*",
        "\+",
        ",",
        "-",
        "\.",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "\?",
        "@",
        "\[",
        "\\",
        "\]",
        "^",
        "_",
        "`",
        "\{",
        "\|",
        "\}",
        "~",
        "\t",
        "\n",
        "\x97",
        "\x96",
        "”",
        "“",
    ]
    # 替换 <??> 为 ""
    text = re.sub(
        "<.*?>", " ", text, flags=re.S
    )  # re.S: 使 . 匹配包括换行在内的所有字符
    # 替换出现的字符为 ""
    text = re.sub(
        "|".join(fileters), " ", text, flags=re.S
    )  # re.S: 使 . 匹配包括换行在内的所有字符
    # 分隔文本并去除空格
    return [i.strip() for i in text.split()]


if __name__ == "__main__":
    res = tokenize("hello world, my name is Yuki!!!")
    print(res)
    # ['hello', 'world', 'my', 'name', 'is', 'Yuki']
