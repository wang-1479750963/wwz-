"""
mysql
"""
#读
import  pymysql

#连接数据库
db =pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='123456',
                    database='stu',
                    charset='utf8')
#生成游标对象(操作数据库,执行sql语句,获取结果)
cur=db.cursor()

#读操作
sql ="select name,age,score from student;"
cur.execute(sql)#执行sql语句

#获取结果方法一
# for i in cur:
#     print(i)

#获取结果第二种方法
# one_row =cur.fetchone()#获取一条记录
# print(one_row)

#三
# many_row=cur.fetchmany(3)#获取多条记录
# print(many_row)

#四
all_row=cur.fetchall()#所有记录
print(all_row)

#关闭游标和数据库连接
cur.close()
db.close()