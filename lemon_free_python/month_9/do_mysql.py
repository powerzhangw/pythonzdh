import mysql.connector
class DoMysql:
    def do_mysql(self,query_sql):
        #2：链接数据库 调用connect方法 会产生一个链接
        config={'host':'119.23.241.154',
                'user':'root',
                'password':'LemonMNB0934',
                'port':3306 ,
                'database':'lmcanon',
                }
        cnn=mysql.connector.connect(**config) #3:生成一个游标  获取操作数据的权限
        cursor=cnn.cursor()
        cursor.execute(query_sql) #4：利用游标去查询数据
        cursor.execute('commit')
        cursor.close()#6:操作完毕 就要关闭游标
        cnn.close()  #7：断开链接

if __name__ == '__main__':
        query="UPDATE divide_record SET actual_payment_time='2018-06-13',payment_status=1 where sales_record_id =(select id from sales_record where member_id in (select id from member WHERE qq=390169816) and payment_type='2') and term=2"
        result=DoMysql().do_mysql(query)