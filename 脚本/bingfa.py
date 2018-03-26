#coding=utf-8
import requests
import hashlib

pwd=hashlib.sha256()
pwd.update('WZwz123456'.encode('UTF-8'))




# url ="https://api.zwjk.com/export/ui/appointment/style_1_9_5"
url ="https://www.baidu.com"
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


headers5={"accept": "application/x-www-form-urlencoded"}
response = requests.get(url, headers=headers5,  timeout=5)

# response.encoding="UTF-8"

print(response.url)
print(response.status_code)
print("返回数据",response.text)