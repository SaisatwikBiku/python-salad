#Project Name: WordCloud Generator
#Author Name: Sai Satwik Bikumandla
#Date: 27th March, 2023

import wordcloud
import matplotlib.pyplot as plt

with open("input.txt") as file:
    txt = file.read()

wc = wordcloud.WordCloud(width = 800, height = 800, background_color = "white")
wc.generate(txt)
wc.to_file("wordcloud.png")

plt.imshow(wc, interpolation = "bilinear")
plt.axis("off")
plt.show()
