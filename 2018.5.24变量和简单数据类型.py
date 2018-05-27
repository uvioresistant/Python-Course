
# coding: utf-8

# In[1]:


action = "exercise"
print(action)


# In[3]:


action = "exercise"
print(action)

action = "hard working"
print(action)


# 'I told my friend,"Python is my favorite language!"'
# "The language 'Python'is named afeter Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community"

# 2.3.1使用方法修改字符串的大小写：
#     - 首字母大写：.title()
#     - 全部大写: .upper()
#     - 全部小写: .lower()
#         

# In[8]:


name = "li xue ying"
print(name.title())
name = "hUang wang ke "
print(name.upper())
print(name.lower())


# 2.3.2合并/拼接字符串
#     - + "" +

# In[14]:


name1 = "li xue ying"
name2 = "huang wang ke"

result = name1.title() + " love " + name2.title()
print(result)


# 2.3.3制表符、换行符添加空白
#     - \t、\n;\n\t是换行

# In[17]:


name1 = "li xue ying"
name2 = "huang wang ke"

result = name1.title() + " love " + name2.title()
print("\n\t"+ result)


# 2.3.4删除空白
#     - rstrip() 去除末尾多余的空白，删除是暂时的，需要修改变量的值，再将新值存回原来的变量中
#     - lstrip() 去除开头的空白
#     - strip() 同时去除两端的空白

# In[21]:


likely = " Lixueying "+" love "+" huang wang ke "
lovely = likely.strip()
print(lovely)


# 2.3.5单引号包含撇号的语法错误
#     - '   '   '

# In[22]:


#apostrophe.py
message = "One of Python's strengths is its diverse community."
print(message)


# In[67]:


#exercise name_case.py
name1 = "Eric"
word1 = '"Hello'
word2 = ',would you like to learn some Python today?"'
print(word1 + " " + name1 + word2)

name2 = "sally"
print("\n" + " " + name2.title())
print(name2.upper())
print(name2.lower())

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

famous_person = "Albert Einstein"
message = ' once said, "A person who never made a mistake never tried anything new."'
print(famous_person + message)


# 2.4.1 整数运算：
# +、-、（x）、/ 、 （**） 乘方

# In[73]:


2 + 3

2 - 3

2 * 3

2 / 3

(2 + 3) ** 3


# In[ ]:


2.4.3 整数型在非字符串型中要用str()
    str(int)


# In[76]:


age = 23
message = "happy " + str(age) + "rd Birthday!"
print(message)


# In[82]:


print(3+5)
print(2*4)
print(10-2)
print(2**3)

