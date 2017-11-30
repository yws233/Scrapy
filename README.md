# Scrapy
> 说明，利用scrapy 抓取网页信息，并生成多种文件格式，存入mongoDB数据库，方便后期数据分析
**在终端创建scrapy项目**
1.创建项目
!(create)[]
2.连接所要抓取的网站
!(create)[]
3.查看创建的文件
!(create)[]
**在IDE运行scrapy文件**
```
scrapy crawl quotes
```
**生成不同的文件格式**
```
scrapy crawl quotes -o quotes.json/xml/jl等等
```
