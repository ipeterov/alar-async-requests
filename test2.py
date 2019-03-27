import concurrent.futures
import json
from urllib.request import urlopen


urls = [
    'http://localhost:8080/source1',
    'http://localhost:8080/source2',
    'http://localhost:8080/source3',
]


def load_url(url, timeout):
    with urlopen(url, timeout=timeout) as conn:
        return json.loads(conn.read())


data = []

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(load_url, url, 2) for url in urls]

    for complete_future in concurrent.futures.as_completed(futures):
        data.extend(complete_future.result())

data.sort(key=lambda x: x['id'])

print(data)
