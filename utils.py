import math


def count_chinese_characters(article: str) -> int:
    """
    这个方法计算文章中总的中文字符数

    Args:
       article (str): 待计数文章

    Returns:
        文章中的中文字符数(int)
    """
    chinese_characters = [char for char in article if '\u4e00' <= char <= '\u9fff']
    return len(chinese_characters)


def words_count_handler(n_words: int) -> [int, int]:
    """
    这个方法按规则计算总字数对应的评分上限和字数扣分项

    Args:
       n_words (int): 文章总字数

    Returns:
        评分上限(int), 字数扣分(int)
    """
    assert n_words >= 0, "n_words不应为负数"
    if n_words >= 800:
        return 60, 0
    elif 400 <= n_words < 800:
        return 60, math.floor((800 - n_words) / 50)
    elif 200 <= n_words < 400:
        return 20, 0
    elif 50 <= n_words < 200:
        return 10, 0
    else:
        return 5, 0
