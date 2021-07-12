import simplejson as json
#import json

#Dict(Json)선언
data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon'
})

#Dict(Json) -> Str
e = json.dumps(data, indent=4)

#Str -> Dict(Json)
d = json.loads(e)

with open("C:\python\\section4\\member.json",'w') as outfile:
    outfile.write(e)

with open("C:\python\\section4\\member.json",'r') as infile:
    r = json.loads(infile.read())
    print("=====")
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
