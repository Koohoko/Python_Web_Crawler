## 香港天文台气象数据 爬虫代码
#### 2016-4-6
* 主要负责抓取香港近几年的每日气象数据。
* 香港气象局的网页是ajax动态加载的，主要思路是模拟ajax请求然后获取数据xml，再用正则表达式清洗数据。
* 数据保存成csv格式，以年份命名，具体可查看上方HK文件夹。
* 运行主程序 Spider_Main.py可重现。
