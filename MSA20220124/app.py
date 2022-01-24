from flask import Flask
import json
import requests

app = Flask(__name__)
def FlaskLab(): 
    return "Flask응답"


@app.route("/data1")
def FlaskData():
    keyValue = r"KLeTHn02oaH3%2FgK5dEzGv%2Ba5QOFH2ZAIQYKx7Z4psOghGHlLz2dHDfCXVvYQbWzF42Y3curauI5MmSihyxPH4g%3D%3D"
    keyDeValue = r"KLeTHn02oaH3/gK5dEzGv+a5QOFH2ZAIQYKx7Z4psOghGHlLz2dHDfCXVvYQbWzF42Y3curauI5MmSihyxPH4g=="

    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond=" + "위례동"
    dataURL += "&servicekey=" + "keyValue"

    dataResult = requests.get(dataURL)
    return json.loads(dataResult)

with open("FlaskLab\\HosInfo.json", "rb") as jsonFile:
    tempData = json.load(jsonFile)
    resultData1 = tempData["orgnm"] #기관명
    resultData2 = tempData["orgcd"] #기관코드
    resultData3 = tempData["orgTlno"] #기관전화번호
    resultData4 = tempData["orgZipaddr"] #기관 주소
    resultData5 = tempData["slrYmd"] #기준일자(현재날짜)
    resultData6 = tempData["dywk"] #요일
    resultData6 = tempData["hldyYn"] #휴무여부
    resultData6 = tempData["lunchSttTm"] #점심시간시작
    resultData6 = tempData["lunchEndTm"] #점심시간끝
    resultData6 = tempData["sttTm"] #진료시작시간
    resultData6 = tempData["endTm"] #진료종료시간

jsonData = [
     {
      "dywk": "월요일",
      "endTm": "1800",
      "hldyYn": "N",
      "lunchEndTm": "1400",
      "lunchSttTm": "1300",
      "orgTlno": "031-731-6614",
      "orgZipaddr": "경기도 성남시 수정구 위례동로 147, (창곡동, 위례건아타워) 5층 505호",
      "orgcd": "41352319",
      "orgnm": "365프렌즈내과의원",
      "slrYmd": "20220124",
      "sttTm": "1100"
    },
    {
      "dywk": "월요일",
      "endTm": "2000",
      "hldyYn": "N",
      "lunchEndTm": "1400",
      "lunchSttTm": "1300",
      "orgTlno": "031-8023-5588",
      "orgZipaddr": "경기도 성남시 수정구 위례동로 141, (창곡동) 5층 505호",
      "orgcd": "41354567",
      "orgnm": "위례상쾌한이비인후과의원",
      "slrYmd": "20220124",
      "sttTm": "0900"
    },
    {
      "dywk": "월요일",
      "endTm": "1800",
      "hldyYn": "N",
      "lunchEndTm": "1400",
      "lunchSttTm": "1300",
      "orgTlno": "031-723-0055",
      "orgZipaddr": "경기도 성남시 수정구 위례동로 141, (창곡동) 5층",
      "orgcd": "41354699",
      "orgnm": "라라소아청소년과의원",
      "slrYmd": "20220124",
      "sttTm": "0900"
    },
    {
      "dywk": "월요일",
      "endTm": "1900",
      "hldyYn": "N",
      "lunchEndTm": "1400",
      "lunchSttTm": "1300",
      "orgTlno": "031-722-3777",
      "orgZipaddr": "경기도 성남시 수정구 위례동로 141, (창곡동) 우성메디피아 305호 일부",
      "orgcd": "41355423",
      "orgnm": "두리이비인후과의원",
      "slrYmd": "20220124",
      "sttTm": "0900"
    },
    {
      "dywk": "월요일",
      "endTm": "1800",
      "hldyYn": "N",
      "lunchEndTm": "1400",
      "lunchSttTm": "1300",
      "orgTlno": "031-753-5551",
      "orgZipaddr": "경기도 성남시 수정구 위례동로 153, (창곡동, 에이플타워) 4층 403호",
      "orgcd": "41357914",
      "orgnm": "아산플러스가정의학과의원",
      "slrYmd": "20220124",
      "sttTm": "0900"
    },
    {
      "dywk": "월요일",
      "endTm": "1800",
      "hldyYn": "N",
      "lunchEndTm": "1400",
      "lunchSttTm": "1300",
      "orgTlno": "031-753-5550",
      "orgZipaddr": "경기도 성남시 수정구 위례동로 153, (창곡동, 에이플타워) 4층 403호",
      "orgcd": "41357922",
      "orgnm": "위례플러스이비인후과의원",
      "slrYmd": "20220124",
      "sttTm": "0900"
    },
    {
      "dywk": "월요일",
      "endTm": "1600",
      "hldyYn": "N",
      "lunchEndTm": "1400",
      "lunchSttTm": "1300",
      "orgTlno": "031-722-0055",
      "orgZipaddr": "경기도 성남시 수정구 위례동로 153, (창곡동, 에이플타워) 4층 404호",
      "orgcd": "41357957",
      "orgnm": "365위례연세내과의원",
      "slrYmd": "20220124",
      "sttTm": "1200"
    }
]

with open("FlaskLab\\HosInfo.json", "w", encoding="utf-8") as writeFile:
    json.dump(jsonData, writeFile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run()