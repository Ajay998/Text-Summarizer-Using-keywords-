import pymysql.cursors

try:
    # db = pymysql.connect('localhost','demomrat_mrstaging',"!DyM*ySI%c#;U8",'demomrat_mrattestai_staging',autocommit=True,cursorclass = pymysql.cursors.DictCursor)

    db = pymysql.connect(host='localhost', user='root', password='',
                         database='demomrat_mrattestai_staging', autocommit=True,
                         cursorclass=pymysql.cursors.DictCursor)

    # db = pymysql.connect(host="localhost", user="root", passwd="",database='brian',autocommit=True,cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
except pymysql.err.OperationalError as e:
    print(e)

cursor.execute("SELECT page_content FROM mt_page_file_contents WHERE page_number=18")
file_content = cursor.fetchone()
keys1, values1 = zip(*file_content.items())
current_page_values = ''.join(values1)
print(current_page_values)
cursor.execute("SELECT title FROM mt_title_master")
title_values = cursor.fetchall()
total_titles = [sub['title'] for sub in title_values]
for i in total_titles:
    if i.lower() in current_page_values.lower():
        print(i.title())