# Web.py库的使用 #


----------

>一个极简的web开发库，用于简单的开发，推荐使用Flask

使用方式：`pip install web.py`
>在pip install web.py失败的情况下，大多数可通过使用如下命令解决：`pip install web.py==0.40.dev0`
>pip 下载超时： `pip --default-timeout=100 install -U pip`


| 定义方法 | 作用 | 应用 |
| ------ | ------ | ------ |
| def GET | 定义GET方法 | 用于类 |
| render.index("参数") | 模板文件读取 | 用于渲染模板 |
| model.select("sql") | 结果数据获取 | 数据库操作 |
| web.seeother("/") | URL跳转 | 用于重定向和表单操作后 |
