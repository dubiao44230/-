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
                    
        应用场景：商品数据计数。
            
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
















































