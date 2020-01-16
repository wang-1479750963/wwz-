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

#打开文件
f=open('dict.txt')

#插入
args_list=[]
for line in f:
    l=cur.findall(r"(\w+)\s+(.*)",line)
    args_list.extend(l)#合并列表
sql="insert into"


#关闭游标和数据库连接
cur.close()
db.close()