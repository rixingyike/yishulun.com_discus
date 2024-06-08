# mowen-note-crawling
莫问笔记Web页面抓取评论区数据并分析、写进Excel文件。



这是一个很好的页面抓取示例，使用selenium+chrome+chromedriver抓取，可以绕过服务器防抓取，可以抓取js动态页面。



req3是普通示例，req5是抓取示例，可以修改后基本一切无登录网页。

## 原理

莫问本身服务器端有防抓取，页面又是js动态加载的，没有办法，只能动用终极大法selenium了。



## 准备工作

安装python

直接在官网下载安装



安装selenium

pip install selenium



下载chromedrivers

去这个（https://googlechromelabs.github.io/chrome-for-testing/#stable）页面找到chromedriver.exe下载。注意不是下载chrome.exe，第一次测试的时候没看清此处，导致后来出错了。



其它py代码在运行时需要的类库，直接使用pip安装即可。



## 导出

安装

pip install pyinstaller 



指令

pyinstaller --onefile --add-binary "chromedriver.exe;." req5.py



为了保证导出后不影响正常运行，chromedriver.exe与程序是打包在一起的。且只生成一个文件。直接运行生成的req5.exe便可以产生一个results.xls文件。

