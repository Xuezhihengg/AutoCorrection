from typing import List


class BaseTask:
    def __init__(self, prompt: str, input_variables: List[str], format_instruction: str) -> None:
        self.__prompt: str = prompt
        self.__format_instruction: str = format_instruction
        self.__input_variables: List[str] = input_variables

    def prompt(self) -> str:
        return self.__prompt

    def format_instruction(self) -> str:
        return self.__format_instruction

    def input_variables(self) -> List[str]:
        return self.__input_variables


task_spell_error = BaseTask(
    prompt="""
你是一个高考语文阅卷老师，现在有一篇待批改作文，需要你对这篇待批改作文进行错别字检测，统计出所有的错别字并按规则计算出错别字扣分项。
以下是完成这一任务的步骤：
Step1:找出文章中所有的错别字并统计个数
Step2:根据以下规则计算出扣分项：
1）出现错别字，1个错别字扣1分；
2）重复出现的错别字不重复扣分；
3）扣分上限为5分，扣分超过5分则不再扣错别字分
输出格式：{format_instructions}
待批改作文：{article}""",
    input_variables=["article"],
    format_instruction="""
统计出所有错别字并计算出扣分项后，对其进行如下Json格式的输出：
{"错别字扣分":"具体扣分数（例如：2）","解析":"具体扣分原因描述（例如：“发现2个错别字，分别是‘澡’应为‘藻’，‘彻’应为‘澈’，每个错别字扣1分，共扣2分。”)"}
"""
)

task_content_analysis = BaseTask(
    prompt="""
你是一个高考语文阅卷老师，现在有一个高考作文题目和一篇待批改作文，需要你对这篇待批改作文进行内容主旨的分析，并给出内容主旨层面的最终评分。
具体评分规则如下：
1）符合题意、中心突出、内容充实、思想健康、感情真挚为一等，可按16-20分酌情给分；
2）符合题意、主题明确、内容较充实、思想健康、感情真实为二等，可按11-15分酌情给分3）基本符合题意、中心基本明确、内容单薄、思想基本健康、感情基本真实为三等，可按6-10分酌情给分；		4）偏离题意、中心不明确、内容不当、思想不健康、感情虚假为四等，可按0-5分酌情给分。
在分析过程中应特别注意一下几个方面的解析：
1）题目期望的主旨是什么，文章作者表达的主旨是什么，从哪里得以体现，这二者是否契合？
2）文章论点是否清晰，是否契合主题，找出文章的中心论点与分论点加以分析；
3）文章内容是否充实，论据是否翔实，是否举出具体的事例加以分析（若有请找出并加以分析），是否有假大空说空话之嫌？
4）文章思想是否积极健康，是否有政治层面的不健康思想，若有则判为四等；
5）分析文章情感，找出情感流露的句段进行分析
输出格式：{format_instructions}
作文题目：{subject}
待批改作文：{article}""",
    input_variables=["subject", "article"],
    format_instruction="""分析与评分结束后请以如下Json格式进行输出：
{"内容主旨得分": "xx",解析:{"主旨解析": "xxxxxxxx","论点解析": "xxxxxxxx","论据解析": "xxxxxxxx","思想情感解析": "xxxxxxxx"}}"""
)

task_express_analysis = BaseTask(
    prompt="""
你是一个高考语文阅卷老师，现在有一个高考作文题目和一篇待批改作文，需要你对这篇待批改作文进行表达文采的分析，并给出表达文采层面的最终评分。
具体评分规则如下：
1）深刻、丰富、有文采、有创意为一等，可按16-20分酌情给分；
2）较深刻、较丰富、较有文采、较有创意为二等，可按11-15分酌情给分；
3）略显深刻、略显丰富、略显文采、略显创意为三等，可按6-10分酌情给分；		
4）个别语句有深意、个别例子较好、个别语句较精彩、个别地方有深意为四等，可按0-5分酌情给分。
在分析过程中应特别注意一下几个方面的加分项解析：
1）是否使用到比喻论证，若有请举例并分析其论证效果和合理性，趣味性；
2）是否使用到道理论证，若有则举例并分析其提出的真理与论点的契合度；
3）是否使用到对比论证，若有则举例解释其对比对象，分析对比效果；
4）是否引用诗歌，名人名言，典故等，若有则举例分析；
5）是否使用排比、对偶、用典、借代等修辞手法，若有则举例分析；
输出格式：{format_instructions}
作文题目：{subject}
待批改作文：{article}""",
    input_variables=["subject", "article"],
    format_instruction="""分析与评分结束后请以如下Json格式进行输出：
{"表达文采得分": "xx","解析":{"论证手法解析": "xxxxxxxx","引经据典解析": "xxxxxxxx","修辞手法解析": "xxxxxxxx"}}
    """
)

task_summary = BaseTask(
    prompt="""
    你是一个高考语文阅卷老师,现在有一篇待批改作文，其错别字检测，内容主旨分析，表达文采分析等方面的工作均已完成，现在需要你对这些工作解析做一个总结。
    解析细节：{detail}""",
    input_variables=["detail"],
    format_instruction=None
)
