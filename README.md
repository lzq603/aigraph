# AI智能图表

AI智能图表绘制系统是一个基于Langchain和ChatGPT的AI图表生成与数据可视化平台。该平台融合了自然语言理解和人工智能绘图技术，致力于为用户提供高度个性化的数据可视化解决方案。通过整合Langchain和ChatGPT的强大功能，该平台能够快速理解用户输入的描述，并智能推断最适合的图表类型，使用户能够在无需专业技能的情况下创建复杂而富有表现力的统计图表。

## 主要特点

*   **智能推断：** 利用先进的自然语言处理和人工智能算法，系统能够智能推荐最适合用户需求的图表类型，提高图表选择的准确性和效率。

*   **个性化定制：** 用户可以通过简单的自然语言描述，定制图表的样式、颜色、标签等参数，使图表更符合用户的个性和需求。

*   **多种图表类型支持：** 系统已支持多种常见的图表类型，包括折线图、柱状图、饼图等，满足用户在不同场景下的图表绘制需求。

*   **用户友好界面：** 设计直观友好的用户界面，使用户能够轻松上手，享受到高效的图表绘制体验。

*   **持续创新与优化：** 团队致力于不断引入新的图表类型、算法和用户反馈机制，确保系统始终保持创新性和用户满意度。

## 项目结构

<img style="width:50%;margin-left:auto;margin-right:auto" src="https://github.com/lzq603/aigraph/blob/master/sample/AIChart.png?raw=true"></img>

## 使用说明

1.  在输入框中描述您想要创建的图表，如：“帮我画出z=x^2+y^2在空间坐标下的图像”。

2.  输入完毕后，点击“生成图表”按钮。

3.  系统将根据您的描述生成相应的图表，并在页面上显示。

**注意：** 每次使用前请清空原有图表，以确保新图表能够正确生成。

![示例.gif](https://github.com/lzq603/aigraph/blob/master/sample/simple.gif?raw=true)

## 安装部署

1.  克隆项目到本地：

```bash
git clone https://github.com/lzq603/aigraph.git
cd aigraph
```

2.安装依赖：

```bash
pip install -r requirements.txt
```

3.运行项目：

```bash
python manage.py runserver 0.0.0.0:8000
```

项目将在本地启动，您可以通过浏览器访问 <http://localhost:8000/graphai/generate_graph/> 查看。
