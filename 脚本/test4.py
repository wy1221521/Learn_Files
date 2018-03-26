#coding=utf-8
import requests
import datetime
import re
import json
from django.http import HttpResponse,HttpResponseRedirect
import hashlib

pwd=hashlib.sha256()
pwd.update('WZwz123456'.encode('UTF-8'))




# url ="https://api.zwjk.com/export/ui/appointment/style_1_9_5"
url ="https://api.zwjk.com/export/ui/branch/list_1_1_1?executionId=&pageFormKey=1-1-1&ucUiFlowId=98db3dd2-b2d2-11e6-a249-525400644ee2&stepId=F_1-1-5"
url3 ="https://open.zwjk.com/api/exec/f649e0f8-b33d-4e4d-865a-7753335cf6f8.htm"
url4 ="https://open.zwjk.com/export/scyUsers/744138ad-be16-4107-bf6c-8f0e25c48a0f/patientVisits"
url5 ="https://yhzx.zwjk.com/userCenterUCMED/user/login"
url7 ="https://yhzx.zwjk.com/userCenterUCMED/user/userInfo"
url6 ="https://yhzx.zwjk.com/userCenterUCMED/user/setPermission"
url8 ="https://yhzx.zwjk.com/userCenterUCMED/user/registration"
url9 ="https://yhzx.zwjk.com/userCenterUCMED/user/logout"
url10 ="https://apigatewaystg.zwjk.com/APP/User/LoginByApp"
url11 ="http://jthyapitest.zwjk.com/API/Common/GetRegionOptions"
url12 ="https://apigatewaystg.zwjk.com/JTHY/APP/Common/GetRegions?preCode=&url="
url13 ="https://apigatewaystg.zwjk.com/JTHY/APP/User/LoginByApp"
url14 ="https://apigatewaystg.zwjk.com/JTHY/API/BannerNews/GetList?displayPosition=4&page=1&url=&rows=10"
url15 ="https://apigatewaystg.zwjk.com/JTHY/APP/User/GetCurrentUserInfo"
url16 ="https://apigatewaystg.zwjk.com/JTHY/APP/Doctor/UpdateDoctorInfo"

params = {'executionId':'',
           'pageFormKey':'1-1-1',
            'ucUiFlowId':'98db3dd2-b2d2-11e6-a249-525400644ee2',
            'stepId	F':'F_1-1-5',
            }
headers1 ={"Host":"api.zwjk.com",
"Connection":"keep-alive",
"Pragma":"no-cache",
"Cache-Control":"no-cache",
"Origin":"https://open.zwjk.com",
"noticeStr":"rpmpv7xah0n3ik9",
"User-Agent":"Mozilla/5.0 (Linux; Android 4.4.2; H60-L01 Build/HDH60-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36  termtype/rubikui",
"Accept":"application/json, text/javascript, */*; q=0.01",
"timestamp":"1516950869522",
"sign":"cc1cbe6cd0d14a412358f70648784c99",
"Referer":"https://open.zwjk.com/appointment/zjyyAAA?execution=e11s1",
"Accept-Encoding":"gzip,deflate",
"Accept-Language":"zh-CN,en-US;q=0.8",
"X-Requested-With":"cn.ucmed.beidakouqiangyiyuan.patient"}

headers2={
"noticeStr":"ybbjb8bewgmk7qfr",
"timestamp":"1516953030216",
"sign":"1bd3b4116e184d6619789f4f23129d97"}
headers3={"K":"1234567",
"Accept":"application/xml",
"Referer":"https://open.zwjk.com/api/exec/f649e0f8-b33d-4e4d-865a-7753335cf6f8.htm",
"Content-Type":"application/x-www-form-urlencoded;charset=utf-8",
"Content-Length":"174",
"Host":"open.zwjk.com",
"Connection":"Keep-Alive",
"Accept-Encoding":"gzip",
"User-Agent":"okhttp/3.2.0"}

headers5={"accept": "application/x-www-form-urlencoded"}
headers11={"Accept": "application/json"}
headers12={"Accept": "application/json","Token": "89a802fda5a8446499b7dcaa5bf413ce"}
headers13={  "Content - Type": "application / json"}
headers14={"Content - Type": "application / json",'token': '044cc8ced2984b499c01aac0ed606073'}
headers15={'Content - Type': 'application / json', 'Token': '0f043dadf2d0408ba6561e4e80d6396f'}
headers16={'Content - Type': 'application / json', 'Token': 'e0ca2d667139452da46b071b96278e66'}

headers10={"Content-Type": "application/json", "charset":"utf-8",
"Host": "apigatewaystg.zwjk.com",
"Token": "89a802fda5a8446499b7dcaa5bf413ce",
"Content-Length": "204"
}


# params3= {"D":"be1246e69df76ea3","T":"1","TX":"U001014","V":"1.0.2","password":"20f645c703944a0027acf6fad92ec465247842450605c5406b50676ff0dcd5ea","S":"","login_name":"15990128517"}
params3= 'requestData={"D":"be1246e69df76ea3","T":"1","TX":"U001014","V":"1.0.2","password":"20f645c703944a0027acf6fad92ec465247842450605c5406b50676ff0dcd5ea","S":"","login_name":"15990128517"}'
params4= 'requestData={"D":"be1246e69df76ea3","T":"1","page_size":60000,"V":"1.0.2","S":"a82444c6c46a859cdf5abfb07bf8d7ea","TX":"Z013001","page_no":1,"dynamic_func":"02"}'
params5= {'userId':'15990128517','password': '6954b9604fb5b3039ff70f328368c9a98c306b75b602799682713ab02003e7e9','roleName':'掌医患者','appCode':'410'}
# params5= {'userId':'15068169255',
#           'password': '6ccc2c47e0debe51cf31ba71e55c3b3490f58c132ade39b4a4cd12ac97481783',
#           # 'roleName':'掌医患者',
#           'roleName':'掌医患者',
#           'appCode':'429',
#           }
params6= {'userId':'15990128517','roleName':'掌医患者','appCode':'429'}
params7= {'token':'582eea788bd8d43a6d1f495d08d2db72'}
params8= {"userId":"wy1221521@#@","phone":"15821871342","password": "6954b9604fb5b3039ff70f328368c9a98c306b75b602799682713ab02003e7e9","roleName":"掌医患者","appCode":"410"}
params9= {'token':'61232044d7aecf10a94f2577d25184a0'}
params10= {"DeviceToken":"a48cd46b66e2ab614030930c204828e68970077b","DeviceType":2,"PassWord":"25D55AD283AA400AF464C76D713C07AD","UserName":"15168412279","deviceNum":"ffffffff-ba70-a154-017f-bf254d3e976c","url":""}
params13= {"DeviceToken":"a48cd46b66e2ab614030930c204828e68970077b","DeviceType":2,"PassWord":"25D55AD283AA400AF464C76D713C07AD","UserName":"15168412279","deviceNum":"ffffffff-ba70-a154-017f-bf254d3e976c","url":""}
params16= {"DeviceToken":"a48cd46b66e2ab614030930c204828e68970077b","DeviceType":2,"PassWord":"25D55AD283AA400AF464C76D713C07AD","UserName":"15168412279","deviceNum":"ffffffff-ba70-a154-017f-bf254d3e976c","url":""}
# print(headers)
# response = requests.get(url,   headers= headers, timeout=9)
# response = requests.post(url6, headers=headers5, data=params6, timeout=5)

#
# print(response.url)
# print(response.status_code)
# print(response.text)
# start_time=datetime.datetime.now()
# response = requests.post(url13, headers=headers13, data=params13 )
# end_time=datetime.datetime.now()
#
# print(end_time-start_time)
# response = requests.post(url5, headers=headers5, data=params5, timeout=5)
# response = requests.post(url10, headers=headers10, data=params10 )
response = requests.get(url15, headers=headers15,  timeout=5)

# response.encoding="UTF-8"

print(response.url)
print(response.status_code)
print("返回数据",response.text)
# fp=open('result.txt', 'w')
# fp.write(response.text)
# fp.close()
# print(response.text)
# fp=response.text.replace("\\","")
# fp=fp.replace("\"","")
# print(fp)
# fp = re.match('.*token:(\w+),', fp).group(1)
# print("\n匹配到了",fp)


    # 定义get方法
# def get(self):
#     try:
#
#         if self.timeout:
#             response = requests.get(self.url, params=self.params, headers=self.headers, timeout=self.timeout)
#         else:
#             response = requests.get(self.url, params=self.params, headers=self.headers)
#         response.encoding="UTF-8"
#         #response.raise_for_status()
#     except TimeoutError:
#
#         return None
#     else:
#         return response
#
# # 定义post方法
# def post(self):
#     try:
#         print(self.url,self.headers, self.data, self.files, self.timeout)
#         if self.timeout:
#             response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=self.timeout)
#         else:
#             response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files)
#
#         response.encoding = "UTF-8"
#     except TimeoutError:
#         return None
#     else:
#         return response




