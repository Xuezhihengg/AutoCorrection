import asyncio
import math

from test_article import *
from llm_func import *
from utils import *

SUBJECT = subject_3
ARTICLE = article_3


async def main():
    n_words = count_chinese_characters(ARTICLE)
    upper_limit, deduct_by_words = words_count_handler(n_words)

    results = await asyncio.gather(
        handler_spell_error(ARTICLE),
        handler_content_analysis(SUBJECT, ARTICLE),
        handler_express_analysis(SUBJECT, ARTICLE)
    )
    results_spell = results[0]
    results_content = results[1]
    results_express = results[2]

    factor = upper_limit / 60
    mark = math.ceil(factor * (int(results_express["表达文采得分"]) + int(results_content["内容主旨得分"]) + int(
        (20 - int(results_spell["错别字扣分"])))))
    detail = {"错别字解析": results_spell["解析"], "内容主旨解析": results_content["解析"], "表达文采解析": results_express["解析"]}
    summary = handler_summary(detail)

    print(f"最终得分{mark}\n{summary}")


if __name__ == '__main__':
    asyncio.run(main())
