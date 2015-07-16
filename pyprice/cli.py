# -*- coding:utf-8 -*-
from __future__ import print_function
import sys

from .index import current, search


def runner():
	if len(sys.argv) == 2:
		option, keyword = 'current', sys.argv[1]
	elif len(sys.argv) == 3:
		option, keyword = sys.argv[1], sys.argv[2]
	else:
		print('Usage: pyprice [option: search] keyword')
		raise SystemExit(1)

	if option == 'current':
		try:
			data = current(keyword)

			print('Keyword:', data['keys']['displaySymbol'])
			print('Value:', data['value'])
			print('Change:', data['change']+',', data['pctChange']+'%')
			print('Market:', data['exchange'])
		except ValueError:
			print('Can not find keyword. Try \'pynance search '+keyword+'\'')

	elif option == 'search':
		results = search(keyword)
		if len(results) == 0:
			print('Can not find keyword.')
		else:
			for result in results:
				data = result[0]
				print('Keyword:', data['s'])
				print('Name:', data['n'], '\n')

	else:
		print('Not supported option.')


if __name__ == '__main__':
	runner()