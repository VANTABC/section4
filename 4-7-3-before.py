import pandas_datareader.data as web
import datetime

#조회 시작 & 마감 날짜
start = datetime.datetime(2018,2,1)
end = datetime.datetime(2018,2,15)

#Google 정보 호출
gs = web.DataReader('KRX: 035720', 'google', start, end)
print(gs)
