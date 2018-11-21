"""
基础部分复习以及面试题
"""

# 1. 自我介绍
"""
    - 大学：前端html、css、js或其他语言C#/asp.net
    - 公司做前端开发官网、专题页；C#开发 -> 阿拉环保网
    - 转Python 
        - 简单快速入门
        - 接触底层实现：socket到web框架
        - 人工智能、机器学习
        - 开发效率高
        PS:少儿编程
    - 
"""

# 2. 你了解其他语言吗？以及和python的对比
"""
    了解：C语言、Java   大学学过
    
    C vs Python:  c语言是python的底层实现，解释器就是由Python编写的。
                  C语言开发的程序执行效率高；开发效率低（内存的管理）；python开发效率更好。
                  
    Java vs Python： 同一个级别，都需要解释器来解释代码。
                    python简洁方便；java繁琐
                    python对于机器学习等强大的类库（模块）。
                    
                    
                    
                 def func(arg):
                    print(arg)
                     
                    
                class Foo:
                    def func(int a1):
                        print(a1)

"""

# 3. 解释型和编译型语言？
"""
    解释型：边解释边执行（即时翻译），代表：Python、PHP、shell 
    编译型：将所有代码编译成指定文件，如： .dll ，然后再去执行 .dll 文件。代表：C、C++、Go、C#、Java

"""

# 4. 字节和位的关系？
"""
      位： 0101001110011
    字节：8位
"""

# 5. Python中如何实现 二进制、八进制、十进制、十六进制 之间的转换？
"""
# 其他转十进制
a1 = "010101010101111"
int(a1,base=2)

# 十进制转二进制
bin(8123)
# 十进制转八进制
oct(87234)
# 十进制转十六进制
hex(3453)

练习题：
    如 10.3.9.12 转换规则为：
            10            00001010
              3            00000011 
             9            00001001
             12            00001100 
    再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？

"""

# 6. 字节码和机器码
"""
    机器码：是汇编的结果，给操作系统直接读取使用。
    
    字节码： xxx.pyc 文件
"""

# 7. 执行脚本头文件 #!/usr/bin/env python
"""
    Linux下运行python文件：
        方式一：
            a.py 
                print(123)
                
            python a.py 
            
        方式二：
            a.py 
                #!/usr/bin/env python
                print(123)
            
            赋予可执行权限
            ./a.py 
"""

# 8. 执行脚本头文件 # --coding:utf-8 -*-
"""
    py2: 默认编码ascii   
    py3: 默认编码utf-8
    
    注意：到公司后py2一定要用--coding:utf-8 -*-
"""

# 9. 运算符
"""
v1 = 1 or 2
v2 = 6 and 1 or 2 and 9
print(v2)
练习题：
    v1 = 1 or 3 
    v2 = 1 and 3 
    v3 = 0 and 2 and 1
     v4 = 0 and 2 or 1
     v5 = 0 and 2 or 1 or 4
     v6 = 0 or Flase and 1
"""

# 10. 三元表达式/三元运算/三目运算
"""
v1 = 'x1' if 1==1 else 'x2'

"""

# 11. 常见数据类型
"""
    str: split、join、strip、upper
    list: append、pop、insert、extend、reverse
    tuple:
    dict: ....

练习题：
    data_list = [
        {'id': 1, 'name': '穆学森', 'age': 18, 'pid': None},
        {'id': 2, 'name': '白亨福', 'age': 18, 'pid': None},
        {'id': 3, 'name': '崔凯', 'age': 18, 'pid': None},
        {'id': 4, 'name': '崔天昊', 'age': 18, 'pid': 1},
        {'id': 5, 'name': '胡海', 'age': 18, 'pid': 1},
        {'id': 6, 'name': '张思雨', 'age': 18, 'pid': 2},
        {'id': 7, 'name': '唐刚', 'age': 18, 'pid': 4},
    ]
    
    # 希望结果
    result = [
        {'id': 1, 'name': '穆学森', 'age': 18, 'pid': None,'children':[{'id': 4, 'name': '崔天昊', 'age': 18, 'pid': 1,'children':[{'id': 7, 'name': '唐刚', 'age': 18, 'pid': 4},]},{'id': 5, 'name': '胡海', 'age': 18, 'pid': 1}]},
        {'id': 2, 'name': '白亨福', 'age': 18, 'pid': None,'children':[{'id': 6, 'name': '张思雨', 'age': 18, 'pid': 2}]},
        {'id': 3, 'name': '崔凯', 'age': 18, 'pid': None,'children':[]},
    ]
    
练习题：
    v = [11,232,122,13,122,31,123,111]  获取列表中第二大的数字。

示例一：
    data = [
        {'id': 1, 'name': 'x1'},
        {'id': 2, 'name': 'x2'},
        {'id': 3, 'name': 'x3'},
        {'id': 4, 'name': 'x4'},
    ]
    
    data_dict = {}
    for item in data:
        data_dict[item['id']] = item
    
    while True:
        nid = int(input('请输入ID'))
        if nid in data_dict:
            pass
示例二：
    data = [
        {'id': 1, 'name': 'x1'},
        {'id': 2, 'name': 'x2'},
        {'id': 3, 'name': 'x3'},
        {'id': 4, 'name': 'x4'},
    ]
    
    data_dict = {}
    for item in data:
        data_dict[item['id']] = item
    
    
    data_dict[2]['name'] = '白横幅'
    
    print(data)

示例三：
    data = [
        {'id': 1, 'name': 'x1','pid':None,'children':[]},
        {'id': 2, 'name': 'x2','pid':1,'children':[]},
        {'id': 3, 'name': 'x3','pid':2,'children':[]},
        {'id': 4, 'name': 'x4','pid':1,'children':[]},
    ]
    
    data_dict = {}
    for item in data:
        item['children'] = []
        data_dict[item['id']] = item
    
    for item in data:
        pid = item['pid']
        if not pid:
            continue
    
        data_dict[pid]['children'].append(item)
"""

# 12. 函数的参数
"""
    def func(a1,a2=[]):
        a2.append(a1)
        return a2
    
    
    v1 = [11,22,33]
    
    result1 = func(55)
    print(result1)
    
    result2 = func(44,v1)
    print(result2)
    
    result3 = func(66)
    print(result3)
"""

# 13. 闭包函数
"""
SQLAlchemy源码

    class Query(object):
    
        def get(self, a1):
            return 1
    
        def filter(self, a1, a2):
            return 2
    
    
    class NewFoo(object):
        pass
    
    
    def method(name):
        def inner(*args, **kwargs):
            return getattr(Query, name)(*args, **kwargs)
        return inner
    
    
    for name in ['get', 'filter']:
        setattr(NewFoo, name, method(name))
    
    obj = NewFoo()
    print(obj.get(1111))
    
Stark组件
    
    class UserInfoConfig(ModelStark):
        
        def show_gender(...):
            if is_header:
                return "性别"
            
            return obj.get_gender_display()
        
        def show_level(...):
            if is_header:
                return "级别"
            
            return obj.get_level_display()
        
        def show_status(...):
            if is_header:
                return "状态"
            
            return obj.get_status_display()
            
        list_display = ['name','email',show_gender,show_level,show_status]
        
    
    
    def get_display(filed_name,title):
        def show(obj,is_header):
            if is_header:
                return title 
            tpl = "get_%s_display" %filed_name
            
            return getattr(obj,tpl)()
            
        return show
    
    class UserInfoConfig(ModelStark):
        
       
        list_display = ['name','email',get_display('gender','性别'),get_display('level','级别'),get_display('status','状态')]

"""

# 14. 装饰器

"""
1. 编写装饰器计算函数执行时间


2. 装饰器实现函数重复执行
    
    def counter(num):
        
        def outer(func_name):
            def innter
                ...
                
            return inner 
            
        return outer 

    @counter(5)
    def func():
        print(123)
        
    func()

3. 装饰器的应用场景？
    - flask路由系统
    - django用户登录 auth 
    - django csrf token (from django.views.decorators.csrf import csrf_protect,csrf_exempt)
"""

# 15. 列表生成式 + lambda 表达式
"""
# 示例一
for i in range(10):
    pass
print(i)

# 示例二
def func(a1):
    return a1 + 100

func_list = []
for i in range(10):
    func_list.append(func)

result = func_list[2](1)
print(result)

# 示例三
def func():
    return i + 100

func_list = []
for i in range(10):
    func_list.append(func)

result = func_list[2]()
print(result)


# 示例四
func_list = []
for i in range(10):
    func_list.append(lambda: i + 100)

result = func_list[2]()
print(result)


# 示例五
func_list = [lambda: i + 100 for i in range(10)]
result = func_list[7]()
print(result)


# 示例六

def num():
    return [lambda x: i * x for i in range(4)]
print([m(2) for m in num()])
"""

# 16. 玩玩
"""
def outer(value):
    def inner():
        print(value)

    return inner


func_list = []
for i in range(10):
    func_list.append(outer(i))

func_list[0]()
func_list[1]()
func_list[2]()
func_list[3]()
func_list[4]()
"""

# 17. 生成器
"""
def func():
    yield 1
    yield 2
    yield 3
    yield 4
obj = func()

# 练习：通过yield自己实现一个类似于py3 range的功能

# 补充：
# py3:
#     list(range(100000000000000000000000))
#     range(100000000000000000000000)
# py2:
#     range(10000000000000000000000000)
#     xrange(10000000000000000000000000)
"""

# 18. 常见的内置函数
"""
    max、min、len、bin、oct、hex、zip
    
    区别：map、filter、reduce（functools）
"""

# 19. 列举常见的内置模块、第三方模块
"""
    内置：os、sys、json、time、random、uuid、logging、hashlib、re ...
    第三方模块：pandas、numpy、bs4、xpath、requests、scrapy、pymysql、dbutils、gevent-websocket、redis
"""


# 20. re模块
"""
    - match/search区别？
    - 贪婪匹配
    - 常见正则：手机、邮箱、IP
"""


# 21. 面向对象
"""
    - 基础：三大特性，封装、继承、多态
            - 封装，对象、类。  应用场景：分页组件；stark组件
            - 继承，多继承继承顺序mro；经典类和新式类；super;  应用场景：drf视图
            
                class Base1(object):
                    def func(self):
                        print('base1.func')
                        super(Base1,self).func()
                    
                class Base2(object):
                    def func(self):
                        print('base2.func')
                    
                class Foo(Base1,Base2):
                    pass
                
                1. 
                    obj = Foo() # Foo > Base1 > Base2
                    obj.func()
                2. 
                    obj = Base1() # Base1 
                    obj.func()
                
            - 多态
                def func(arg):
                    print(arg)
                    
                def func(int arg): # 可以传递int或int子类的对象。
                    print(arg)
    
    - 成员
        - 字段
        
            class Foo:
                COUNTRY = "中国" # 类变量；静态字段；静态属性
                def __init__(self,name):
                    self.name = name  # 实例变量；字段；对象属性
            
            obj = Foo('天珠')
        
        - 方法
            class Foo:
                def f1(self):  # 实例方法   Foo().f1()
                    pass
                    
                @classmethod
                def f2(cls):   # 类方法    Foo.f2()     Foo().f2()
                    pass

                @staticmethod  # 静态方法  Foo.f2()     Foo().f2()
                def f3():
                    pass
        - 属性
            class Foo:
            
                @property
                def start():
                    pass 
            
            obj = Foo()
            obj.start
            
    - 特殊成员：
        __init__ # 初始化方法
        __new__  # 构造方法
        __call__
        __getattr__
        __setattr__
        __delattr__
        __getitem__
        ...
        __dict__
        __add__
        __str__
        __repr__
        __iter__
        __doc__
        __name__
        __enter__
        __exit__
            class Foo(object): # 上下文管理
                def __enter__(self):
                    print('进入')
                    return '1'
            
                def __exit__(self, exc_type, exc_val, exc_tb):
                    print('出去')
            
            obj = Foo()
            
            
            with obj as num:
                print(123,num)
        __add__
            class Foo(object):
                def __init__(self,num):
                    self.num = num
            
                def __add__(self, other):
                    return self.num + other.num
            
            obj1 = Foo(11)
            obj2 = Foo(22)
            
            result = obj1 + obj2
            
            print(result)

"""


# 22. 反射
"""
    什么是反射：
        getattr/delattr.....
        
    应用场景？
        django CBV，
        django、flask、scrapy等所有的配置文件： v = "django.contrib.sessions.middleware.SessionMiddleware"
        
            def import_string(dotted_path):
                try:
                    # 'django.contrib.sessions.middleware.    SessionMiddleware'
                    module_path, class_name = dotted_path.rsplit('.', 1)
                except ValueError:
                    msg = "%s doesn't look like a module path" % dotted_path
                    six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])
                # from django.contrib.sessions import middleware
                module = import_module(module_path)
            
                try:
                    # middleware.SessionMiddleware
                    return getattr(module, class_name)
                except AttributeError:
                    msg = 'Module "%s" does not define a "%s" attribute/class' % (
                        module_path, class_name)
                    six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])
    
"""

# 23. py2和py3的区别？
"""
字符串和字节
    py2： unicode  -> encode utf-8 ->      str(字节串)  = bytes
    py3： str      -> encode utf-8 ->      bytes 

经典类和新式类
    py2：经典类、新式类
    py3：新式类
yield from
    def foo():
        yield 666
        yield 999
    
    def func():
        yield 1
        yield from foo()
        yield 2
        yield 3
    
    obj = func()
    
    for item in obj:
        print(item)
默认解释器编码
range和xrange
readlines和xreadlines
print
input/raw_input
...


"""


# 24. 给你一个路径“D:\EVCapture” 找到目录下的所有文件（子目录中的文件）。
"""
os.walk
"""

# 25. 一行代码实现两个值的互换 & 一行实现 9*9 乘法表
"""
a = 1
b = 2
"""

# 26. 利用面向对象创建一个栈。
"""
class Stack(object):
    
    def push(self,item):
        pass
    
    def pop(self):
        pass
"""







































