import requests
import pandas as pd
import json
import os
import urllib.parse as urllib_parse

APIKEY_FILENAME = '~/.disent/apikey.json'

def disent(model,kwargs):
	apikey_filename_expanded = os.path.expanduser(APIKEY_FILENAME)
	with open(apikey_filename_expanded) as f:
		d = json.load(f)
		apikey = d.get('Api-Key',None)
		if apikey is None:
			raise 
			Exception('','')

	def disent_get(protocol,hostname,port,endpoint,uri_dict):
		headers = {'Accept': 'application/json','Authorization': f'Api-Key {apikey}'}
		uri_params = urllib_parse.urlencode(uri_dict)
		url = f"{protocol}://{hostname}:{port}/{endpoint}?{uri_params}"
		response = requests.request("GET", url, headers=headers)
		d = json.loads(response.text)
		result = d.get('result',None)
		if result is None:
			print(d)
			raise Exception('','')
		df = pd.DataFrame(result)
		return df
	models = {
		'cache':'api/cache'
	}
	return disent_get('http','localhost',8000,models[model],kwargs)



def unit_test():
	d = {
		"source":"BSPLINE_MODEL",
		"datastorekey":":::snapshots:20220606:211511:market_data_snapshot",
		"ticker":"AAPL",
		"pivot":"YRS,MNY,IV"
	}
	df = disent('cache',d)
	print(df)


if __name__=='__main__':
	unit_test()
