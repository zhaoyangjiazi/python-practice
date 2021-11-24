#!/usr/bin/env python
# coding: utf-8

# In[5]:


#输出十九大的字表
#计算多少个自然段和多少句子
#句子平均数和句子长度方差
#Nvo.14
def shijiu():
    zibiao=[]
    fo=open(r"C:\Users\86182\Documents\新建文件夹\chars.txt.txt")
    text=fo.read()
    fo.close()
    for i in text:
        if i not in zibiao:
            zibiao.append(i)
    print("字表为:",zibiao)
    return text

def shuliang(text):
    n=0
    m=0
    for i in text:
        if i=="。":
            n+=1
        if i=="！":
            n+=1
        if i=="?":
            n+=1
        if i=="\n":
            m+=1
    s=(len(text)-m-n)/n
    print("句子个数:",n)
    print("自然段个数:",m)
    print("平均字数:",s)
    return s
    

def zishu(s):
    fo=open(r"C:\Users\86182\Documents\新建文件夹\chars.txt.txt")
    text=fo.read()
    fo.close()
    a=0
    b=0
    n=0
    bao=[]
    for i in text:
        if i=="。":
            a=len(bao)+a
            bao=[]
            b=(a-s)**2+b
            a=0
        elif i=="！":
            a=len(bao)+a
            bao=[]
            b=(a-s)**2+b
            a=0
        elif i=="?":
            a=len(bao)+a
            bao=[]
            b=(a-s)**2+b
            a=0
        elif i=="\n":
            a=a
        else:
            bao.append(i)
    for i in text:
        if i=="。":
            n+=1
        if i=="！":
            n+=1
        if i=="?":
            n+=1
    print("句子长度方差为:",b/n)
            
    
    
zishu(shuliang(shijiu()))


# In[4]:


#输出十九大报告中最长的句子和最短的句子
#Nvo.14
import re
fo=open(r"C:\Users\86182\Documents\新建文件夹\chars.txt.txt")
text=fo.read()
fo.close()
text1=re.split(r"[。！\n,、]",text)
textmax=sorted(text1,reverse=True)
text2=re.split(r"[。]",text)
textmin=sorted(text2,key=len,reverse=False)
print("最长的三句话:",textmax[0],textmax[1],textmax[2])
print("最短的三句话:",textmin[0],textmin[1],textmin[2])


# In[23]:


#出现了多少成语
#Nvo.14
fo=open(r"C:\Users\86182\Desktop\作业\新建文件夹\新建文件夹\idioms.txt")
idioms=fo.read()
fo.close
fo=open(r"C:\Users\86182\Documents\新建文件夹\chars.txt.txt")
text=fo.read()
fo.close()
idiom=idioms.split(r"、")
a=0
for i in range(len(text)-3):
    if text[i]+text[i+1]+text[i+2]+text[i+3] in idiom:
        a=a+1
    elif "\n"+text[i]+text[i+1]+text[i+2]+text[i+3] in idiom:
        a=a+1
print("十九大出现了:",a,"个成语")


# In[ ]:




