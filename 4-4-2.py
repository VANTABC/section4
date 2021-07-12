import simplejson as json
#import json

#Dict(Json)선언
data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul',
    'grade':[95,77,89,91]
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan',
    'grade':[85,67,100,93]
})
data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon',
    'grade':[98,79,99,92]
})

#Json 파일쓰기(dump)
with open('C:\python\\section4\\member.json','w') as outfile:
    json.dump(data, outfile)

with open('C:\python\\section4\\member.json','r') as infile:
    r = json.load(infile)
    print("=====")
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        grade = ''
        for g in p['grade']:
            grade = grade + ' ' + str(g)
        print('Grade:',grade.lstrip())
        print('')
