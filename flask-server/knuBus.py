import mysql.connector
import json
mydb = mysql.connector.connect(
    host="osp-db-server.mysql.database.azure.com",
    user="KSC",
    passwd="1q2w3e4r@@",
    database="knubus"
)
myData = {
    'Grade': '', #학년
    'Gubun': '',  # 전공, 교양, 첨성인**
    'SubjectName': '',  # 과목 명
    'SubjectCode': '',  # 과목 코드
    'ClassCode': '',  # 과목 코드 (분반 포함)
    'ClassDivideNumber': '',  # 분반
    'EstablishedUniversity': '',  # 개설 대학
    'EstablishedDepartment': '',  # 개설 학과
    'SearchUniversity': '',     #검색시 사용할 대학명
    'SearchDepartment': '',  # 검색시 사용할 학과명
    'ProfessorNames': '',  # 교수명 (배열 형식임)
    'Season': '',  # 개설 학기
    'ApplicantsMax': '',  # 수강 총원
    'ApplicantsCurrent': '',  # 수강 인원
    'IsUntact': '',  # 비대면 여부(Y or N)
    'Schedule': '',  # 시간표 (배열 형식임)
    'Credit': '',  # 학점
    'Rate1': '',  # 출석 비중
    'Rate2': '',  # 중간 시험
    'Rate3': '',  # 기말 시험
    'Rate4': '',  # 과제
    'Rate5': '',  # 발표
    'Rate6': '',  # 토론
    'Rate7': '',  # 안전교육
    'Rate8': '',  # 기타
    'Rate9': '',  # ?
    'PriorSubject': '',  # 권장선수과목
    'SubsequentSubject': '',  # 권장후수과
}

myColumns = ['Grade', 'Gubun', 'SubjectName', 'SubjectCode', 'ClassCode', 'ClassDivideNumber', 'EstablishedUniversity', 'EstablishedDepartment', 'SearchUniversity', 'SearchDepartment', 'ProfessorNames', 'Season', 'ApplicantsMax', 'ApplicantsCurrent', 'IsUntact', 'Schedule', 'Credit', 'Rate1', 'Rate2', 'Rate3', 'Rate4', 'Rate5', 'Rate6', 'Rate7', 'Rate8', 'Rate9', 'PriorSubject', 'SubsequentSubject']

def transForm(data):
    tempData = myData
    #tempData['Season'] = data['Season']
    #tempData['SearchDepartment'] = data['SearchDepartment']
    for i in data:
            tempData[i] = data[i]
    if data['Gubun'] == 'GE':
        if data['SearchUniversity'] == '':      tempData['Gubun'] = '첨'
        else:                                   tempData['Gubun'] = data['SearchUniversity']

    elif data['Gubun'] == 'UN':
        tempData['Gubun'] = ''
        tempData['SearchUniversity'] = data['SearchUniversity']
    return tempData


def searchWord(data):
    tempData = transForm(data)
    str = " where"
    cnt = 0
    for word in tempData:
        if tempData[word] == "":
            continue
        if cnt != 0:
            str += ' and'
        cnt = cnt + 1
        str += " {0} like '%{1}%'".format(word, tempData[word])
    return str

def accessDataBase(data):
    str = searchWord(data)
    dataDict = {}
    cursor = mydb.cursor()
    query = ("select * from 강의" + str)
    print(query)
    cursor.execute(query)
    print("Connection established")

    i = 0
    for rows in cursor:
        isavailable = True
        datadict_value = {}
        for word, col in zip(rows, myColumns):
            if col == 'SearchDepartment' and data['SearchDepartment']:       # 전공 분류
                word = word.split(', ')
                if data[col] not in word:
                    isavailable = False
                    continue
                word = data[col]
            datadict_value[col] = word
        if isavailable:
            dataDict[i] = datadict_value
            i += 1
    return dataDict
