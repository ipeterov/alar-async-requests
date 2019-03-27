import grequests

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
]

rs = (grequests.get(u, timeout=2) for u in urls)

for answer in grequests.imap(rs, size=3):
	print(answer.url)