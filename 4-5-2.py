import pandas as pd

#읽기
#csv_s2파일은 ,가 아니라 ;으로 구분되어 있음(sep옵션을 넣어야한다)
df2 = pd.read_csv("C:\python\\section4\\csv_s2.csv", sep=';', skiprows=[0], header=None, names=['Name','Test1','Test2','Test3','Final','Grade'])
#print(df2)

#컬럼 내용 변경(내가 원하는 열은 마치 dict타입처럼 key값으로 가져올 수 있다)
#df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
#print(df2)

#평균 컬럼 추가
#axis=0이 열방향(세로), axis=1이 행방향(가로)
df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)
#print(df2)

#합계 컬럼 추가
df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
print(df2)

#쓰기
#df2.to_csv("C:\python\\section4\\result_s2.csv")
df2.to_csv("C:\python\\section4\\result_s2.csv", index=False)
