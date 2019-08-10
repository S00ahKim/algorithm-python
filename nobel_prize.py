'''
투빅스 (3주차 1번)

문제
저명한 데이터 분석가 김대웅은 자신이 가진 방대한 데이터를 근거로 다음과 같은 관계를 밝혀 
라이벌 분석가 정혜인에 대항하여 노벨상 후보에 노미네이트 되었다.
"남자의 IQ 는 키(cm) – 70 로 수렴하고, 여자의 IQ 는 키(cm) – 60 으로 수렴한다."
노벨상 감사 위원회 위원장인 당신은 데이터를 통해 다음과 같은 주장을 검증하려고 한다. 
데이터의 열은 다음과 같이 이루어져 있다.

Name: 영어로 된 이름이 적혀 있다.
Height: 해당 하는 사람의 키가 cm 단위로 적혀있으며, 항상 정수이다.
IQ: 해당하는 사람의 IQ 가 정수로 적혀 있으며, 결측치가 존재한다.
Gender: 해당하는 사람의 성별이 남자는 M, 여자는 F 로 구별되어 적혀있다

입력
CSV 파일의 이름이 표준 입력을 통해 입력이 된다.
데이터의 행은 최소 10개, 최대 100개이다.
이름과 결측치를 제외한 모든 데이터는 자연수로 이루어져있다.

출력
첫 줄에는 내림한 R, E, H를 공백을 구분하여 출력하세요.
다음 줄에는 김대웅이 감사를 통과했다면 GodDaeWoong, 
통과하지 못했다면 GodHyeIn 을 출력하세요.
'''

import pandas as pd
df = pd.read_csv(input())

# R 구하기
tmp = 0
outliers = []

for i in df["IQ"]:
    if str(i).isdigit():
        pass
    else:
        tmp += 1
        outliers.append(i)

R = tmp/len(df.index) * 100


# 결측치 처리
outliers_index = df[df['IQ'].isin(outliers)].index
df_without_outlier = df.drop(outliers_index, 0)
df_without_outlier = df_without_outlier.drop("Height",1)
df_without_outlier["IQ"] = df_without_outlier["IQ"].astype('int')

mean_female = df_without_outlier.groupby(['Gender']).mean().loc["F","IQ"]
mean_male = df_without_outlier.groupby(['Gender']).mean().loc["M","IQ"]

for i in outliers_index:
    if df.loc[i, "Gender"] == "F":
        df.replace(df.loc[i,"IQ"], mean_female, inplace=True)
    else:
        df.replace(df.loc[i,"IQ"], mean_male, inplace=True)


# E 구하기
E = 0

for r in df.index:
    if df.loc[r, "Gender"] == "M":
        E = E + abs(int(df.loc[r,"Height"]-70) - int(df.loc[r, "IQ"]))
    else:
        E = E + abs(int(df.loc[r,"Height"]-60) - int(df.loc[r, "IQ"]))
    
E = E/len(df.index)


# H 구하기
hn = 0
for h in df.index:
    if df.loc[h, "Gender"] == "M":
        if df.loc[h, "Height"] <= 172 and df.loc[h, "Height"] >= 168:
            hn += 1
    else:
        if df.loc[h, "Height"] <= 162 and df.loc[h, "Height"] >= 158:
            hn += 1
            
H = hn/len(df.index) * 100

if R>25 or E>5 or H>50:
    print(int(R), int(E), int(H))
    print("GodHyeIn")
else:
    print(int(R), int(E), int(H))
    print("GodDaeWoong")