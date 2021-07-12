import pandas as pd

#csv파일 기본 읽기
#df = pd.read_csv("C:\python\\section4\\csv_s1.csv")
#print(df)

#행 스킵
#df = pd.read_csv("C:\python\\section4\\csv_s1.csv", skiprows=[0,1])
#print(df)

#행 스킵, 헤더 생략
#df = pd.read_csv("C:\python\\section4\\csv_s1.csv", skiprows=[0], header = None)
#print(df)

#헤더 정의
#df = pd.read_csv("C:\python\\section4\\csv_s1.csv", skiprows=[0], header = None, names=["Month",2013,2014,2015])
#print(df)

#인덱스 컬럼 정의
#df = pd.read_csv("C:\python\\section4\\csv_s1.csv", skiprows=[0], header = None, names=["Month",2013,2014,2015], index_col=[0])
#print(df)

#특정 값 치환
#df = pd.read_csv("C:\python\\section4\\csv_s1.csv", skiprows=[0], header = None, names=["Month",2013,2014,2015], index_col=[0], na_values=['JAN'])
#print(pd.isnull(df))
#print(df)

#실습 정리 및 인덱스 재정의
#df1 = pd.read_csv("C:\python\\section4\\csv_s1.csv", skiprows=[0], header = None, names=["Month",2013,2014,2015])
#print(df1.index)     #RangeIndex(start=0, stop=12, step=1)
#print(list(df1.index))       #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#print(df1.index.values)      #[ 0  1  2  3  4  5  6  7  8  9 10 11]
#print(df1.index.values.tolist())     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#print(df1.rename(index={0:'aa', 1:'bb', 2:'cc'}))        #불편하게 언제 이렇게 다 바꾸고 앉아있니
#print(df1.rename(index=lambda x:x+1))        #람다함수로 인덱스를 재설정하는게 편함
