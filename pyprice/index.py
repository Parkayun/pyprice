# -*- coding:utf-8 -*-
import json

import requests


def current(keyword):
	url = ''.join(('http://markets.money.cnn.com/services/api/mobile/companydetails.asp?outputFormat=JSONP&callback=angular.callbacks._0&symb=', keyword))
	return json.loads(requests.get(url).text[28:-2])		


def search( keyword):
	url = ''.join(('http://markets.money.cnn.com/services/mobile/lookup.asp?render=json&jsoncallback=angular.callbacks._a&symb=', keyword))
	return json.loads(requests.get(url).text[27:-3])