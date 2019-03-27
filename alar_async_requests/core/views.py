import concurrent.futures
import json
from urllib.error import URLError
from urllib.request import urlopen

from django.conf import settings
from django.http import JsonResponse


def index(request):
    def load_url(url, timeout):
        try:
            response = urlopen(url, timeout=timeout)
        except URLError:
            return []

        if response.status != 200:
            return []

        try:
            data = json.loads(response.read())
        except json.JSONDecodeError:
            return []

        return data

    data = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(load_url, url, timeout=2) for url in settings.DATA_URLS]

        for complete_future in concurrent.futures.as_completed(futures):
            data.extend(complete_future.result())

    data.sort(key=lambda entry: entry['id'])

    return JsonResponse(data, safe=False)