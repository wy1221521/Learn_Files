import re


data='{"extra":{"Id":3439,"UserName":"15168412279","CustomUserName":"问问","Phone":"15168412279","UserState":true,"SectionId":8097,"SectionName":"测试科室","DoctorId":21796,"RoleType":1,"UnitId":688,"UnitName":"军校机构","Token":"67df27e227bc408bada9ba8fcf33c3c4","PhotoImage":"/Upload/DoctorPhoto/59327449ba9f4f6899c26f092678a1c1.jpg","PhotoImageUrl":"https://yscjthyums.zwjk.com/Upload/DoctorPhoto/59327449ba9f4f6899c26f092678a1c1.jpg","device_type":2,"device_token":"a48cd46b66e2ab614030930c204828e68970077b","deviceNum":"ffffffff-ba70-a154-017f-bf254d3e976c","Isformal":1,"YunEducationWeb":"\u0026token=67df27e227bc408bada9ba8fcf33c3c4","IsCanPhone":0,"AgencyApplyState":3,"RegisteredDoctorCode":"2018103010116010700","FromAPI":1,"Ticket":null},"suc":true,"mes":null,"code":200,"projectcode":"000000","RequestTime":"2018/3/7 15:04:28"}'

result=re.match('.*\"Token\":\"(\w+)\",',data).group(1)

print(result)