# -*- coding:utf-8 -*-
from __future__ import print_function
import sys

from .index import current, search
from .prompt import colored as  c


def runner():
	if len(sys.argv) == 2:
		option, keyword = 'current', sys.argv[1]
	elif len(sys.argv) == 3:
		option, keyword = sys.argv[1], sys.argv[2]
	else:
		print('Usage:', c('pyprice [option: search] keyword', 'sian'))
		raise SystemExit(1)

	if option == 'current':
		try:
			data = current(keyword)
			print(c(data['companyName'], 'magenta'), '/', c(data['keys']['displaySymbol'], 'yellow'))
			print(c('Current Price', 'sian')+':', data['value'], end=' (')
			price_color = 'red' if '-' in data['change'] else 'blue'
			print(c(data['change'], price_color)+',', c(data['pctChange'], price_color)+'%)')
			print(c('Market', 'sian')+':', data['exchange'])
		except ValueError:
			print(c('Can not find keyword.', 'red'), 'Try', c('pynance search '+keyword, 'sian'))

	elif option == 'search':
		results = search(keyword)
		if len(results) == 0:
			print(c('Can not find keyword.', 'red'))
		else:
			for result in results:
				data = result[0]
				print(c('Name', 'sian')+':', c(data['n'], 'magenta'))
				print(c('Keyword', 'sian')+':', c(data['s'], 'yellow'))
				print(c('Market', 'sian')+':', data['e'], '\n')

	else:
		print(c('Not supported option.', 'red'))


if __name__ == '__main__':
	runner()