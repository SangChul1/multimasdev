import json

try:
    jsonFile = open("datalab\\mydata.json", "rb") 
    tempData = json.load(jsonFile)
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]

except NameError as error1:
    print("네임 에러", error1)
except UnicodeError as error2:
    print("유니코드 에러", error2)
except Exception as error3:
    print("오류", error3)

else:
    jsonFile.close()
    print("jsonFile 이상 없음.")

jasonData1 ={
        "empid": 12345678,
        "name" : "박상철,
        "info" : [
            {
                "date1": "2022-01-21,
                "home": "하남시"
            },
            {
                "dep": "개발",
                "E-mail address": "aaa@aaa.co.kr"
            }
        ]
    }
try:
    writeFile = open("datalab\\mydata2.json", "w")
    json.dump(jasonData1, writeFile)
except UnicodeError as error2:
    print("유니코드 에러", error2)
except Exception as error3:
    print("오류", error3)

try:
    writeFile = open("datalab\\mydata3.json", "w", encoding="utf-8")
    json.dump(jasonData1, writeFile, ensure_ascii=False)
except UnicodeError as error2:
    print("유니코드 에러", error2)
except Exception as error3:
    print("오류", error3)

try:
    writeFile = open("datalab\\mydata4.json", "w")
    json.dump(jasonData1, writeFile, ensure_ascii=False, indent=4)
except UnicodeError as error2:
    print("유니코드 에러", error2)
except Exception as error3:
    print("오류", error3)

try:
    writeFile = open("datalab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jasonData1, writeFile, ensure_ascii=False, indent=4)
except UnicodeError as error2:
    print("유니코드 에러", error2)
except Exception as error3:
    print("오류", error3)

else:
    writeFile.close()
    print("writeFile 이상 없음.")

temp=0
