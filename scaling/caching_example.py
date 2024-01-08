import requests
import time
from functools import lru_cache, cache
from timeit import repeat

#
# def memoize(func):
# 	cache = {}
#
# 	def wrapper(*args):
# 		if args in cache:
# 			return cache[args]
# 		else:
# 			result = func(*args)
# 			cache[args] = result
# 			return result
#
# 	return wrapper


@cache
def get_html_data_cached(url):
	response = requests.get(url)
	return response.text


setup_code = "from __main__ import get_html_data_cached"
stmt = "get_html_data_cached('https://books.toscrape.com/')"
times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=10)
print(f"Minimum execution time: {min(times)}")
#
#
# def get_html_data(url):
# 	response = requests.get(url)
# 	return response.text
#
#
# start_time = time.time()
# get_html_data('https://books.toscrape.com/')
# print('Time taken (normal function):', time.time() - start_time)
#
# # Get the time it took for a memoized function (manual decorator)
# start_time = time.time()
# get_html_data_cached('https://books.toscrape.com/')
# print('Time taken (memoized function using manual decorator):', time.time() - start_time)


#
# cache = dict()
#
# def get_article_from_server(url):
# 	print("Fetching article from server...")
# 	response = requests.get(url)
# 	return response.text
#
#
# def get_article(url):
# 	print("Getting article...")
# 	if url not in cache:
# 		print(url)
# 		cache[url] = get_article_from_server(url)
# 		# print('url', cache)
# 	return cache[url]
#
#
#
# count = 0
# while count < 4:
# 	get_article("https://realpython.com/sorting-algorithms-python/")
# 	get_article("https://realpython.com/sorting-algorithms-python/")
# 	count += 1

#
# @lru_cache(maxsize=16)
# def steps_to(stair):
# 	if stair == 1:
# 		# You can reach the first stair with only a single step
# 		# from the floor.
# 		return 1
# 	elif stair == 2:
# 		# You can reach the second stair by jumping from the
# 		# floor with a single two-stair hop or by jumping a single
# 		# stair a couple of times.
# 		return 2
# 	elif stair == 3:
# 		# You can reach the third stair using four possible
# 		# combinations:
# 		# 1. Jumping all the way from the floor
# 		# 2. Jumping two stairs, then one
# 		# 3. Jumping one stair, then two
# 		# 4. Jumping one stair three times
# 		return 4
# 	else:
# 		# You can reach your current stair from three different places:
# 		# 1. From three stairs down
# 		# 2. From two stairs down
# 		# 2. From one stair down
# 		#
# 		# If you add up the number of ways of getting to those
# 		# those three positions, then you should have your solution.
# 		return (
# 				steps_to(stair - 3)
# 				+ steps_to(stair - 2)
# 				+ steps_to(stair - 1)
# 		)
#
#
# # setup_code = "from __main__ import steps_to"
# # stmt = "steps_to(30)"
# # times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=10)
# # print(f"Minimum execution time: {min(times)}")
#
# print(steps_to.cache_info())
#
# print(steps_to(30))

# If you need to remove all the entries from the cache, then you can use cache_clear() provided by @lru_cache.
