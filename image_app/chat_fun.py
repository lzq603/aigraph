import os
import uuid
import re
import time
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
OPENAI_API_KEY = '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'

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema.output_parser import StrOutputParser
from langchain.utilities.python import PythonREPL
from langchain.globals import set_verbose
set_verbose(True)

# template = """Write some python code to solve the user's problem. Do not define new functions.

# Return only python code in Markdown format, e.g.:

# ```python
# ....
# ```"""


def generate_unique_string_with_time():
    # 生成基于当前时间的 UUID
    unique_uuid = uuid.uuid1()

    # 将 UUID 转换为字符串形式
    unique_string = str(unique_uuid)

    return unique_string


def gen_funart(text='', aip_key=OPENAI_API_KEY):

    template = """根据用户的要求写出Python代码（Linux系统上运行），注意不要定义函数，禁止使用def关键字

只需要按如下格式返回python代码：

```python
....
```"""
    prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])

    def _sanitize_output(text: str):
        print(text)
        code = re.findall('```python(.*)```', text, re.M|re.S)
        if not code:
            code = text
        else:
            code = code[0]
        code = code.replace('plt.show()', '')
        if code.find('plt.') >= 0:
            code += '\nplt.clf()'
        print(code)
        return exec(code)

    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.0, request_timeout=120, max_retries=1)
    chain = prompt | model | StrOutputParser() | _sanitize_output
    filename = generate_unique_string_with_time()
    output = chain.invoke({"input": text + "，并保存为文件\"static/function_art/{}.png\"".format(filename)})
    print("输出：")
    print(output)
    return filename



def gen_graph(text='', api_key=OPENAI_API_KEY):

    template = """根据用户输入的数据和要求写出用Echats生成图表的js脚本，DOM容器的id为chart，只需要按以下格式返回js代码：
```javascript
....
```"""
    prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])


    def _sanitize_output(text: str):
        # print(text)
        code = re.findall('```javascript(.*)```', text, re.M|re.S)
        if not code:
            code = text
        else:
            code = code[0]
        # code = code.replace('plt.show()', '')
        # if code.find('plt.') >= 0:
        #     code += '\nplt.clf()'
        # print(code)
        # return exec(code)
        return code

    model = ChatOpenAI(openai_api_key=aip_key, temperature=0.0, request_timeout=120, max_retries=1)
    chain = prompt | model | StrOutputParser() | _sanitize_output
    output = chain.invoke({"input": text})
    print("输出：")
    print(output)
    return output
