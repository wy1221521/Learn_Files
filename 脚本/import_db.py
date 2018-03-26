import xlrd
import csv
import  datetime
import psycopg2

#Test
#conn = psycopg2.connect(database="interfaceTest_db", user="postgres", password="wy1221521", host="127.0.0.1", port="5432")

#Product
conn = psycopg2.connect(database="ProduceAutomationTest", user="postgres", password="yNg%nW0GpJx10Z3", host="192.168.0.25", port="5432")
cur = conn.cursor()
##########################
#测试
##########################
# book = xlrd.open_workbook("importdataTest.xlsx")
# sheet = book.sheet_by_name("importdata")
#
# for r in range(1, sheet.nrows):
#      print((sheet.cell(r, 0).value))
#      print("#######################")
#      print((sheet.cell(r, 1).value))
#      print("#######################")
#      print((sheet.cell(r, 2).value))
#      print("#######################")
#      print((sheet.cell(r, 3).value))
#      print("#######################")
#      print((sheet.cell(r, 4).value))
#      print("#######################")
#      print((sheet.cell(r, 5).value))
#      print("#######################")
#      print((sheet.cell(r, 6).value))
#      print("#######################")
#      break


#############################
#Test
############################

# query ='''CREATE TABLE interface_interface_cases(
#     id INT NOT NULL PRIMARY KEY,
#     case_id  varchar(255) UNIQUE,
#     test_id  varchar(255),
#     method varchar(255),
#     interface_id int,
#     module_id  int,
#     project_id  int,
#     head varchar(255),
#     params varchar(255),
#     data varchar(65535),
#     file varchar(255) ,
#     status int,
#     testcases_createtime  varchar(255),
#     testcases_updatetime  varchar(255),
#     testcases_creator  varchar(255),
#     testcases_updator  varchar(255),
#     comments  varchar(65535),
#     timeout int,
#     expected_contents varchar(65535)
#
#  )'''
# cur.execute(query)
# conn.commit()




##########################
#插入接口
##########################
# query = """INSERT INTO interface_interfaces (interface_id,interface_host,interface_url,project_id) VALUES (%s, %s, %s, %s)"""
#
# book = xlrd.open_workbook("importdata1.xlsx")
# sheet = book.sheet_by_name("inter")
# for r in range(1, sheet.nrows):
#     interface_id=int(sheet.cell(r, 0).value)
#     interface_host=sheet.cell(r, 1).value
#     interface_url=sheet.cell(r, 2).value
#     project_id=sheet.cell(r, 3).value
#
# #
# #
# #
#     values = (interface_id, interface_host,interface_url,project_id)
#     print(values)
#     cur.execute(query, values)
#     conn.commit()




##########################
#插入接口用例
##########################
query = """INSERT INTO interface_interface_cases (id,case_id, test_id, method, interface_id,module_id,project_id,head, params,data, status, testcases_createtime,testcases_creator,timeout,expected_contents ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s)"""

book = xlrd.open_workbook("importdata1.xlsx")
sheet = book.sheet_by_name("new")
for r in range(1, sheet.nrows):
    id=int(sheet.cell(r, 0).value)
    case_id=sheet.cell(r, 1).value
    test_id=sheet.cell(r, 2).value
    method=sheet.cell(r, 3).value
    interface_id=int(sheet.cell(r, 4).value)
    module_id=int(sheet.cell(r, 5).value)
    project_id=int(sheet.cell(r, 6).value)
    head=sheet.cell(r, 7).value
    params=sheet.cell(r, 8).value
    data=sheet.cell(r, 9).value
    expected_contents=sheet.cell(r, 10).value
    status=3
    testcases_creator="王禛"
    timeout=9
    testcases_createtime=str(datetime.datetime.now())
#
#
#
    values = (id, case_id, test_id, method, interface_id, module_id,project_id,head, params,data, status, testcases_createtime,testcases_creator,timeout,expected_contents)
    print(values)
    # values=(33, 'TC_INT_25', 'TC_10', 'GET', 15, 3, 2, '{"Content - Type": "application / json" }', 'none', '{"token":""}', 0, '2018-03-07 13:24:41.560112', '王禛', 9)
    cur.execute(query, values)
    conn.commit()

##########################
#插入功能用例
##########################
# query = """INSERT INTO interface_testcases (id,test_id, topic, steps, expected, type, status, testcases_createtime,testcases_creator,module_id ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#
# book = xlrd.open_workbook("importdata2.xlsx")
# sheet = book.sheet_by_name("new")
# for r in range(1, sheet.nrows):
#     id=int(sheet.cell(r, 0).value)
#     test_id=sheet.cell(r, 1).value
#     topic=sheet.cell(r, 2).value
#     steps=sheet.cell(r, 3).value
#     type=sheet.cell(r, 4).value
#     module_id=sheet.cell(r, 5).value
#     expected=sheet.cell(r, 6).value
#
#     testcases_createtime= str(datetime.datetime.now())
#     testcases_creator="施乐乐"
#     # testcases_creator="王禛"
#     status=0
#
#     values = (id,test_id, topic, steps, expected, type, status, testcases_createtime,testcases_creator,module_id)
#     print(values)
#     cur.execute(query, values)
#     conn.commit()

