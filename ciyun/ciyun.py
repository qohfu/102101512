import jieba
import wordcloud
from PIL import Image
from wordcloud import ImageColorGenerator
import numpy as n
jieba.setLogLevel(jieba.logging.INFO)


f = open('/Users/sakana/PycharmProjects/pythonProject2/danmu.txt',encoding='utf-8')
bg=n.array(Image.open('/Users/sakana/Downloads/jianb.jpg'))
text = f.read()


text_list = jieba.lcut(text)
string = ' '.join(text_list)



wc = wordcloud.WordCloud(
    width = 1000,
    height = 1800,
    background_color = 'white',
    font_path = "/System/Library/Fonts/PingFang.ttc",
    scale = 15,
    mode='RGBA',
)
wc.generate(string)
ig=ImageColorGenerator(bg)
wc.recolor(color_func=ig)
wc.to_file('out.png')