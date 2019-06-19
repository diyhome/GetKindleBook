# 介绍
* 这个项目是用来从一些不允许下载小说的网站上面下载小说.使用的`Python`版本是`3.6`
* 写爬虫的时候发现代码重用的地方有点多,就给集成到`func`里面了

---
本项目依赖于
* BeautifulSoup
* lxml

# 新手上路
1. 在`GerKindleBook`(即根目录)下新建一个文件(e.g.:`name.py`)
2. 在文件头添加`from func.WebPage import WebPage`使用最基本的库(当然,还有一些库可以自由添加)    
3. 写入`if __name__=="__main__":`表明程序起点
4. 建立一个对象`object = WebPage()`
5. 使用对象:eg`object.GUrl(url)`  

> 示例可以查看`gmrb.py`

# 项目文件介绍
## WebPage
* 这个文件是进行一些与网页有关的操作，引用`BeautifulSoup`    
* 默认解释器为`lxml`,可以通过修改文件中`_INTERPRETER`变量改为其它解释器

### GUrl
获取网页上面的url
> 具体用途是已知一个章节列表,批量获取章节信息

 *注意* 其返回值是一个`数组`
### GContent
获取网页上面的内容
> 获取小说内容
### self.BTitle
小说的`名字`
### self.CTitlle
小说的`章节名`

