# AutoCorrection

基于LLM的语文作文自动批改应用

# 项目结构

.  
├── llm_func.py  
├── main.py  
├── requirements.txt  
├── tasks.py  
├── test_article.py  
└── utils.py  

**main.py** ：demo主文件夹，评分主流程在此执行，使用大模型异步调用，执行效率更高  
**llm_func.py** ：LLM大模型方法，均为异步方法，对大模型的调用来自此文件  
**tasks.py** ：对大模型任务的类型封装  
**utils.py** ：常用工具方法，如计算文章总字数  
**test_article.py** ：测试使用到的作文题目和文章   

# 运行

直接运行main.py即可：

```bash
python main.py
```

**注意:** 本Demo选用LLM大模型：ERNIE-4.0-8K，运行mai.py前需要为百度千帆的API Key和Secret Key设置环境变量

```bash
touch .env
```

在`.env`文件内输入：

```py
QIANFAN_AK=YOUR_AK
QIANFAN_SK=YOUR_SK
```
然后再运行main.py

# 流程

![](https://raw.githubusercontent.com/Xuezhihengg/Blog_images/main/202408301112114.png)
