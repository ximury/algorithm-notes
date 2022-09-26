"""
@Date:        2022/9/21 上午9:40
@Author:      wyj
@FileName:    回文字符串.py
@Description: None
"""


def is_palindrome(s: str) -> bool:
    # s = s.lower()
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    str_reverse = s[::-1]
    if str_reverse == s:
        return True
    else:
        return False


if __name__ == '__main__':
    res = is_palindrome("asdsA")
    print(res)
    str_param = "A man, a plan, a canal: Panama"
    res = is_palindrome(str_param)
    print(res)
