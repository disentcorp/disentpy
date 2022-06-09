import requests
import pandas as pd
import json
import os
import urllib.parse as urllib_parse
import io

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
		apikey = input("Secrets file not found. See docs. Enter your API-Key to continue: ")
		headers = {'Accept': 'application/json','Authorization': f'Api-Key {apikey}'}
		uri_params = urllib_parse.urlencode(uri_dict)
		url = f"{protocol}://{hostname}:{port}/{endpoint}?{uri_params}"
		response = requests.request("GET", url, headers=headers)

		from tqdm import tqdm
		total_size_in_bytes= int(response.headers.get('content-length', 0))
		block_size = 1024 #1 Kibibyte
		progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
		
		b = b''
		for data in response.iter_content(block_size):
			progress_bar.update(len(data))
			b+= data
		progress_bar.close()
		txt = b.decode()
		d = json.loads(txt)
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
