import dotenv
from typing import Dict, Union
from tasks import *
from langchain_community.llms import QianfanLLMEndpoint
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

dotenv.load_dotenv()

model = QianfanLLMEndpoint(
    model="ERNIE-4.0-8K",
)

parser = JsonOutputParser()


async def handler_spell_error(article: str) -> Dict[str, Union[int, str]]:
    """
    这个方法处理错别字检测任务，接收文章并返回扣分数以及解析

    Args:
        article (str): 待批改文章

    Returns:
        Json格式输出 i.e.{"错别字扣分":"具体扣分数（例如：2）","解析":"具体扣分原因描述（例如：“发现2个错别字，分别是‘澡’应为‘藻’，‘彻’应为‘澈’，每个错别字扣1分，共扣2分。”)"}
    """
    prompt = PromptTemplate(
        template=task_spell_error.prompt(),
        input_variables=task_spell_error.input_variables(),
        partial_variables={"format_instructions": task_spell_error.format_instruction()}
    )

    chain = prompt | model | parser
    output = await chain.ainvoke({"article": article})

    return output


async def handler_content_analysis(subject: str, article: str) -> Dict[str, Union[int, Dict[str, str]]]:
    """
    这个方法处理内容主旨分析任务，接收作文题目和文章，返回扣分数以及解析

    Args:
        subject (str): 作文题目
        article (str): 待批改文章

    Returns:
          Json格式输出 i.e.{"内容主旨得分": "xx",解析:{"主旨解析": "xxxxxxxx","论点解析": "xxxxxxxx","论据解析": "xxxxxxxx","思想情感解析": "xxxxxxxx"}}
    """
    prompt = PromptTemplate(
        template=task_content_analysis.prompt(),
        input_variables=task_content_analysis.input_variables(),
        partial_variables={"format_instructions": task_content_analysis.format_instruction()}
    )

    chain = prompt | model | parser
    output = await chain.ainvoke({"subject": subject, "article": article})

    return output


async def handler_express_analysis(subject: str, article: str) -> Dict[str, Union[int, Dict[str, str]]]:
    """
    这个方法处理表达文采分析任务，接收作文题目和文章，返回扣分数以及解析

    Args:
        subject (str): 作文题目
        article (str): 待批改文章

    Returns:
        Json格式输出 i.e.{"表达文采得分": "xx","解析":{"论证手法解析": "xxxxxxxx","引经据典解析": "xxxxxxxx","修辞手法解析": "xxxxxxxx"}}
    """
    prompt = PromptTemplate(
        template=task_express_analysis.prompt(),
        input_variables=task_express_analysis.input_variables(),
        partial_variables={"format_instructions": task_express_analysis.format_instruction()}
    )

    chain = prompt | model | parser
    output = await chain.ainvoke({"subject": subject, "article": article})

    return output


def handler_summary(detail: Dict[str, Dict]) -> str:
    prompt = PromptTemplate(
        template=task_summary.prompt(),
        input_variables=task_summary.input_variables(),
    )

    chain = prompt | model
    output = chain.invoke({"detail":detail})

    return output

