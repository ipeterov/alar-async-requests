
import grequests

urls = [
    'http://localhost:8080/source1',
    'http://localhost:8080/source2',
    'http://localhost:8080/source3',
]

rs = (grequests.get(u, timeout=2) for u in urls)

data = []

for answer in grequests.imap(rs, size=3):
	data.extend(answer.json())
    
data.sort(key=lambda x: x['id'])

print(data)