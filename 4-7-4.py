import matplotlib.pyplot as plt

#리스트 범위(x축)
x = list(range(0, 256))
print(x)

#리스트 범위(y축)
y = [v*v for v in x]
#for v in x:
#    y.append(v*v)
print(y)

#차트 설정(x에 인덱스, y에 컬럼을 넣으면 차트 완성)
plt.plot(x,y,'bo')

#차트 실행
plt.show()
