"""
数据库
"""

# 1. 数据库设计
"""
    a. 单表
    b. FK（单表；一张表存储时，如果有重复出现的字段为了防止硬盘的浪费，所以做一个FK；去掉FK变成单表）
    c. M2M
    
    到底是什么关系？单选的下拉框/radio FK；多选下拉框/checkbox M2M
        
        
    问题：员工信息表员工当前薪资；保留员工的所有的调薪记录。
        
        思路一：
            员工表：
                id  name salary 
                
            调薪：
                id  price  time  员工ID 
                  
        思路二：
             员工表：
                id  name salary 
                
             调薪：
                id  price  time 
                
                
            员工调薪表：
                id   uid   sid
"""

# 2. 基本SQL
"""
    分组：
        select depart_id,count(1),max(salary),min(age),sum(age) from user group by depart_id
        select depart_id,count(1),max(salary),min(age),sum(age) from user group by depart_id having count(1)>5
    连表：
        inner join / left join / right join 
        数据：
            部门表：
                id   title 
                1      销售
                2      运营
                3      IT
                
            用户表：
                id          name        部门id
                1           x1          1
                2           x2          1
                3           x3          1
                4           x4          1
                5           x5          1
        
        请问查到多少条数据？
            select * from userinfo left join depart on userinfo.did = depart.id    5
        
            select * from depart left join userinfo on userinfo.did = depart.id    7
        
            select * from userinfo inner join depart on userinfo.did = depart.id   5
        
            select * from depart inner join userinfo on userinfo.did = depart.id   5
"""

# 3. MySQL数据库引擎以及区别？
"""
        a. 常见innodb、mysiam
        b. 区别：
            - innodb：
                - 支持事务（原子性、一致性、隔离性、持久性）
                - 表锁
                - 行锁
            - mysiam
                - 不支持事务
                - 表锁
                - 全文索引
                - 速度快
                
        补充：
            原生SQL
                begin;
                
                select * from xxx  for update;
                
                update ...
                
                commit;
            
            django:
                    
                with trancation.automic:
                    User.objects.filter().select_for_update()
                    
        应用场景：商品数据计数。  根据表锁实现
            
"""


# 4. 索引
"""
    作用：
        - 加速查找
        - 约束
    种类：
        - 索引：随便写
        - 唯一索引：允许Null + 不重复
        - 主键索引：不允许Null + 不重复
        
        - 联合索引：多列组成一个索引
        - 联合唯一索引：多列组成一个索引 + 唯一
            例如：
                name  email  pwd 
                
                命中索引遵循最左前缀的原则： name、name  email、name pwd、name  email  pwd 
                
    
    补充：
        - 覆盖索引，当查找数据时候在索引表中就可以获取数据，无需去数据表中查找。
                    select name from user where name='xxx'
        - 索引合并, 使用多个单列索引进行查找。
                    select * from user where name='xx' email='xx'
                    
    
    为什么索引快？
        因为在索引结构中讲述按照B+来进行存放的数据。

"""


# 5. 优化方案
"""
    a. 索引。
    b. 固定长度的字段写在前面。
            id  name  age < id  age name
    c. 对于固定选择的内容：性别，可以将其对应关系保存在内存中。
    d. 分表
            - 垂直分分，将数据分割到N张表。
            - 水平分分，将列分到到N种表。
    e. 分库 
    f. 读写分离（主从复制）
        主：读写
        从：读        
            
        
        django：
            models.Users.objects.filter(id=2).using('default')
            models.Users.objects.filter(id=2).using('db1')
    g. limit 
        select * from tb where name='alex' limit 1;
        
    h. 缓存
        将常用数据读取到redis中（缓存），读取速度快。
        
         
    char和varchar的区别。

"""


# 6. 知识点
"""
    a. 视图
    b. 触发器
    c. 存储过程
    d. 函数
"""

# 7. 慢日志查询

# 8. 创建了索引之后一定要命中索引
"""
    - like '%xx'
        select * from tb1 where name like '%cn';
    - 使用函数
        select * from tb1 where reverse(name) = 'wupeiqi';
    - or
        select * from tb1 where nid = 1 or email = 'seven@live.com';
        特别的：当or条件中有未建立索引的列才失效，以下会走索引
                select * from tb1 where nid = 1 or name = 'seven';
                select * from tb1 where nid = 1 or email = 'seven@live.com' and name = 'alex'
    - 类型不一致
        如果列是字符串类型，传入条件是必须用引号引起来，不然...
        select * from tb1 where name = 999;
    - !=
        select * from tb1 where name != 'alex'
        特别的：如果是主键，则还是会走索引
            select * from tb1 where nid != 123
    - >
        select * from tb1 where name > 'alex'
        特别的：如果是主键或索引是整数类型，则还是会走索引
            select * from tb1 where nid > 123
            select * from tb1 where num > 123
    - order by
        select email from tb1 order by name desc;
        当根据索引排序时候，选择的映射如果不是索引，则不走索引
        特别的：如果对主键排序，则还是走索引：
            select * from tb1 order by nid desc;
     
    - 组合索引最左前缀
        如果组合索引为：(name,email)
        name and email       -- 使用索引
        name                 -- 使用索引
        email                -- 不使用索引

"""


# 9. 数据库对比
"""
    文件：MySQL、SQLite、mongodb、SQLServer、access、oracle、db2 
    
    内存：redis、memcached

"""

# 10. redis和memcached的区别？
"""
    相同点：都是将数据保存到内存，存取速度都比较快。 自己想：在内存中存在一个大字典，你对字典进行操作。
    不同点：
            - 数据类型：
                - redis，5大数据类型
                    {
                        k1:v1,
                        k2:[11,22],
                        k3:{
                            kk1:vv1,
                            kk2:vv2,
                        },
                        k4: {1,2,3},
                        k5: {('alex',8),('oldboy',5)}
                        
                    }
                - memcached，1中类型：字符串
                    {
                        k1:v1,
                    }
            - 持久化
                - redis，支持持久化
                - memcached，不支持。
            - 集群架构
                - redis，支持
                - memcached，不支持。
            - 自动过期策略
                - redis，支持
                    voltile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰

                    volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰
                    
                    volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰
                    
                    allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰
                    
                    allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰
                    
                    no-enviction（驱逐）：禁止驱逐数据
                - memcached，不支持。
                
"""


# 11. redis持久化的两种方式
"""
    - AOF,记录下用户所有执行的命令。
    - RDB,定时持久化。
"""

# 12. redis默认支持主从复制
"""
slaveof 主IP
"""

# 13. redis的高可用（sentinel）
"""
自动检测主服务器是否正常
"""

# 14. redis分布式（cluster）
"""
    - redis cluster
    - codis 
    - Twemproxy
"""

# 15. redis分布式锁
"""
    redlock
    
    老狗：连接所有的redis服务器，在服务器上设置 k1 = 随机字符串； 成功一半以上，表示获得锁。
    其他：其他人来，也会设置，但是设置时会成功 < 一半； 表示未获取锁，等待。
    
    
    # 超时，老狗锁自动释放。
    
    老狗：释放锁；连接所有服务器删除 k1=原来设置的随机字符串 ；
    
    from redlock import Redlock
    dlm = Redlock(
        [
            {"host": "1.1.1.1", "port": 6379, "db": 0},
            {"host": "1.1.1.2", "port": 6379, "db": 0},
            {"host": "1.1.1.2", "port": 6379, "db": 0},
        ]
    )
    my_lock = dlm.lock("k1",5000)
    dlm.unlock(my_lock)

"""


# 赠送：负载均衡















































