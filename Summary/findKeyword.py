import re
import pymysql.cursors

try:                    
    # db = pymysql.connect('localhost','demomrat_mrstaging',"!DyM*ySI%c#;U8",'demomrat_mrattestai_staging',autocommit=True,cursorclass = pymysql.cursors.DictCursor)


    db = pymysql.connect(host='localhost',user='demomrat_mrstaging',password='!DyM*ySI%c#;U8',database ='demomrat_mrattestai_staging', autocommit = True,cursorclass=pymysql.cursors.DictCursor)
    
    # db = pymysql.connect(host="localhost", user="root", passwd="",database='brian',autocommit=True,cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
except pymysql.err.OperationalError as e:
    print(e)

cursor.execute("SELECT summary_keywords FROM mt_summary_keyword WHERE is_valid=1")
Summary_keywords=cursor.fetchall()
list_of_kewords=[]
for key in Summary_keywords:
    list_of_kewords.append(key['summary_keywords'])

def find_keword(text):


    patterns=[]
    def check_keyword(pattern):


        if pattern.lower() in text.lower():
                    # patterns.append(pattern)
                    return True
        else:
                    return False

    for pattern in list_of_kewords:
        res=check_keyword(pattern)

        if res:
            patterns.append(pattern)
            
        else:
            continue
    return patterns


