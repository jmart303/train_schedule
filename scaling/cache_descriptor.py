import requests
from timeit import repeat


def my_cache(func):
	cache = {}

	def wrapper(*args):
		if args in cache:
			return cache[args]
		else:
			results = func(*args)
			cache[args] = results
			return results

	return wrapper   # return the function


@my_cache
def get_html(url):
	response = requests.get(url)
	return response


	setup_code = "from __main__ import get_html"
	stmt = "get_html('https://books.toscrape.com/')"
	times = repeat(setup=setup_code, stmt=stmt, repeat=2, number=10)
	print(f"Minimum execution time: {min(times)}")
