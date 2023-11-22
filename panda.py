# import pandas as pd
# empdata=pd.DataFrame({
#     'name':['joyel','manu'],
#     'age':['25']
# })
# print(empdata)
# change on feature for branch



LIST=[
    {
      "PANEL": "",
      "FILE": 308,
      "NAME": "JAINAMMA KURIAN (WORK PENDING)",
      "MOB": 9400896283,
      "PLACE": "MUKKAM",
      "DISTRICT": "CALICUT",
      "CORDI": "ANIL KUMAR",
    },
    {
      "PANEL": "",
      "FILE": 344,
      "NAME": "AJAYAKUMAR V N (NOT URGENT)",
      "MOB": 9072449789,
      "PLACE": "KOORKENCHERY",
      "DISTRICT": "THRISSUR",
      "CORDI": "AJAY KUMAR",
     
    },
    {
      "PANEL": "",
      "FILE": 344,
      "NAME": "Joyel",
      "MOB": 9072449789,
      "PLACE": "KOORKENCHERY",
      "DISTRICT": "THRISSUR",
      "CORDI": "AJAY KUMAR",
     
    }   
]


for i in LIST:
 
    if i['DISTRICT']=='THRISSUR':
        print(i['NAME'],i['MOB'])
    else:
        print('Not Thissur')
