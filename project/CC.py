#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import pandas as pd
import random

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns',None)
#显示所有行
pd.set_option('display.max_rows',None)
#设置数据的显示长度，默认为50
pd.set_option('max_colwidth',200)
#禁止自动换行(设置为Flase不自动换行，True反之)

dataset = pd.read_excel('Veales superheroes.xlsx')
corpushe = pd.read_excel('starter.xlsx','He')
corpusshe = pd.read_excel('starter.xlsx','She')
corpusit = pd.read_excel('starter.xlsx','It')
corpusme = pd.read_excel('starter.xlsx','Me')
corpusyou = pd.read_excel('starter.xlsx','You')
dataset.fillna('you', inplace = True)
corpushuman = corpushe.append([corpusshe,corpusme,corpusyou])
# print(corpushuman)
# print(corpushe[corpushe.tag=='morden'])
material = {}
verbs = []
for action in dataset['Action']:
    strs = action.replace('_',' ')
    verbs.append(strs)
# print(verbs)

starters = []
for starter in dataset['A']:
    starters.append(starter.split(','))
# print(starters)

holders = []
for holder in dataset['B']:
    holders.append(holder.split(','))
# print(holders)

com = []
for i in range(len(verbs)):
    name = 'verb'+str(i)
    material[name] = verbs[i]
    name1 = 'starter' +str(i)
    material[name1] = starters[i]
    name2 = 'holder' + str(i)
    material[name2] = holders[i]
# print(com)
# print(len(material))
LOG_LINE_NUM = 0


def superherocorpus():
    a  = random.randint(0,len(material)/3-1)
    veb = 'verb'+str(a)
    sta = 'starter'+str(a)
    hol = 'holder'+str(a)
    b = random.randint(0,len(material[sta])-1)
    c = random.randint(0,len(material[hol])-1)
    text = material[sta][b].title()+' '+material[veb]+' '+material[hol][c]+'.'
    d = random.randint(0,len(corpusit[corpusit.tag=='superhero'])-1)
    e = random.randint(0, 1)
    if e == 0:
        text1 = text + corpusit[corpusit.tag == 'superhero']['corpus'].iloc[b]
    else:
        text1 = corpusit[corpusit.tag == 'fantasy']['corpus'].iloc[b] + text
    return text1


def allcorpus():
    score = {'science fiction':0.5,'superhero':0.25,'fantasy':0,'morden':1}
    a,b = (random.sample(range(0, len(corpushuman)-1), 10),random.sample(range(0, len(corpusit)-1), 10))
    tagid = 0
    tagscore = 10
    temp = 0
    for i in range(0,10):
        temp = abs(score[corpushuman['tag'].iloc[i]]-score[corpusit['tag'].iloc[i]])
        if temp > 0 and temp < tagscore:
            tagscore = temp
            tagid = i
        # atag.append(corpushuman['tag'].iloc[a])
        # btag.append(corpusit['tag'].iloc[b])
    c = random.randint(0,1)
    if c ==0:
        text = corpushuman['corpus'].iloc[a[tagid]]+corpusit['corpus'].iloc[b[tagid]]
    else:
        text = corpusit['corpus'].iloc[b[tagid]]+corpushuman['corpus'].iloc[a[tagid]]
    return text

def mordencorpus():
    a = random.randint(0,len(corpushuman[corpushuman.tag=='morden'])-1)
    b = random.randint(0,len(corpusit[corpusit.tag=='morden'])-1)
    c = random.randint(0,1)
    if c ==0:
        text = corpushuman[corpushuman.tag=='morden']['corpus'].iloc[a]+corpusit[corpusit.tag=='morden']['corpus'].iloc[b]
    else:
        text = corpusit[corpusit.tag=='morden']['corpus'].iloc[b]+corpushuman[corpushuman.tag=='morden']['corpus'].iloc[a]
    return text

def fantasycorpus():
    a = random.randint(0,len(corpushuman[corpushuman.tag=='fantasy'])-1)
    b = random.randint(0,len(corpusit[corpusit.tag=='fantasy'])-1)
    c = random.randint(0,1)
    if c ==0:
        text = corpushuman[corpushuman.tag=='fantasy']['corpus'].iloc[a]+corpusit[corpusit.tag=='fantasy']['corpus'].iloc[b]
    else:
        text = corpusit[corpusit.tag=='fantasy']['corpus'].iloc[b]+corpushuman[corpushuman.tag=='fantasy']['corpus'].iloc[a]
    return text
def scificcorpus():
    a = random.randint(0,len(corpushuman[corpushuman.tag=='science fiction'])-1)
    b = random.randint(0,len(corpusit[corpusit.tag=='science fiction'])-1)
    c = random.randint(0,1)
    if c ==0:
        text = corpushuman[corpushuman.tag=='science fiction']['corpus'].iloc[a]+corpusit[corpusit.tag=='science fiction']['corpus'].iloc[b]
    else:
        text = corpusit[corpusit.tag=='science fiction']['corpus'].iloc[b]+corpushuman[corpushuman.tag=='science fiction']['corpus'].iloc[a]
    return text
def fantasycorpus():
    a = random.randint(0,len(corpushuman[corpushuman.tag=='fantasy'])-1)
    b = random.randint(0,len(corpusit[corpusit.tag=='fantasy'])-1)
    c = random.randint(0,1)
    if c ==0:
        text = corpushuman[corpushuman.tag=='fantasy']['corpus'].iloc[a]+corpusit[corpusit.tag=='fantasy']['corpus'].iloc[b]
    else:
        text = corpusit[corpusit.tag=='fantasy']['corpus'].iloc[b]+corpushuman[corpushuman.tag=='fantasy']['corpus'].iloc[a]
    return text
print(allcorpus())


# print(superherocorpus())
class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

        # 功能


    #windows
    def set_init_window(self):
        # name
        self.init_window_name.title("Spark of Story")
        self.init_window_name.geometry('1068x681+10+10')
        # self.init_window_name["bg"] = "pink"
        #label
        self.init_data_label = Label(self.init_window_name, text="tags")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="Welcome to an beginning")
        self.result_data_label.grid(row=0, column=12)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=40)
        self.tag = Listbox(self.init_window_name,selectmode=SINGLE,width=67, height=40)  #原始数据录入框
        self.tag.grid(row=1, column=0, rowspan=10, columnspan=10)
        # listbox
        for item in ['All','Fantasy', 'Science Fiction', 'Morden', 'Superhero',  ]:
            self.tag.insert(END, item)
        self.result_data_Text = Text(self.init_window_name, width=67, height=55)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)
        #Button
        self.story_maker = Button(self.init_window_name, text="Begin！", bg="lightblue", width=10,command= lambda :self.startergene())
        self.story_maker.grid(row=5, column=11)
    def startergene(self):

        tags = self.tag.curselection()
        # print(tags[0])
        if tags[0] == 0:
            try:
                test = allcorpus()
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, test)
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "some error occurs")
        elif tags[0] == 1:
            try:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, fantasycorpus())
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "some error occurs")
        elif tags[0] == 2:
            try:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, scificcorpus())
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "some error occurs")
        elif tags[0] == 3:
            try:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, mordencorpus())
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "some error occurs")
        elif tags[0] == 4:
            try:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, superherocorpus())
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "some error occurs")
        # else:
        # self.write_log_to_Text("ERROR:str_trans_to_md5 failed")







def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()