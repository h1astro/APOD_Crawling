from lxml import etree
import requests
r=requests.get("https://apod.nasa.gov/apod/astropix.html")
html=etree.HTML(r.text)

# 获取内容介绍
result=html.xpath('./body/p/text()|./body/p/a/text()')
print(result)
text="".join(result)
text=text.replace("\n"," ")
print(text)

# 标题 title
result=html.xpath('./body/center[2]/b[1]/text()')
title="".join(result)
print(title)

# 图片地址 pic_url
result=html.xpath('./body/center[1]/p[2]/a/@href')
pic_url="https://apod.nasa.gov/apod/"+"".join(result)
print(pic_url)

# 版权
result=html.xpath('./body/center[2]/a/text()')
copyright=",".join(result)
print(copyright)

#google API 翻译
from googletrans import Translator
translator = Translator(service_urls=['translate.google.cn'])
source=text
trans = translator.translate(source,src='en',dest='zh-cn').text
print(trans)
