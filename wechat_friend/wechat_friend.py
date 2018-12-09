# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 14:37
# @Author  : Z.C.Wang
# @Email   : 
# @File    : spider_wechat.py
# @Software: PyCharm Community Edition
"""
Description :
"""
import re
import jieba
import itchat
from pandas import DataFrame
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
import pickle


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


def list2str(wordlist):
    string = ' '
    for word in wordlist:
        string = string + ' ' + word
    return string


if __name__ == '__main__':
    itchat.login()
    friends = itchat.get_friends(update=True)
    male = female = other = 0
    for i in friends[1:]:
        sex = i['Sex']
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    total = len(friends[1:])

    print('男性好友：%.2f%%' % float(male / total * 100))
    print('女性好友：%.2f%%' % float(female / total * 100))
    print('不明性别好友：%.2f%%' % float(other / total * 100))

    Nickname = get_var('NickName')
    Sex = get_var('Sex')
    Province = get_var('Province')
    print(Province)
    City = get_var('City')
    Signature = get_var('Signature')
    data = {'Nickname': Nickname, 'Sex': Sex, 'Province': Province,
            'City': City, 'Signature': Signature}
    pickle.dump(data, open('data.txt', 'wb'))
    frame = DataFrame(data)
    frame.to_csv('info.csv', index=True, encoding='utf-8-sig')

    siglist = []
    for i in friends:
        signature = i['Signature'].strip().replace('spam', '').replace('class', '').replace('emoji', '')
        # rep = re.compile('1f\d+\w*|[<>/=]')
        rep = re.compile("[^\u4e00-\u9fa5^]")
        signature = rep.sub('', signature)
        siglist.append(signature)
    text = ''.join(siglist)
    wordlist = jieba.cut(text, cut_all=True)
    wordlist = list(wordlist)
    String = list2str(wordlist)

    my_wordcloud = WordCloud(background_color='white', max_words=2000, max_font_size=55, random_state=42,
                             scale=2, font_path=r'wechat_friend/Droid-Sans-Fallback.ttf').generate(String)
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()
