import requests

IDENTIFIER = 'kavule'
csr = 43
lpg = 20
nsr = 10
url = 'http://localhost:8000/upload/'

def start_upload(identifier=IDENTIFIER, url=url, csr=None, lpg=None, nsr=None):
	"""
	`identifier` is a unique identification for the raspberry pi units
	`url` is the URL or link to which a payload is POSTesd
	`csr` is short for carbonmonoxide_sensor_reading
	`lpg` is short for lpg_gas_sensor_reading
	`nsr` is short for nitrogendioxide_sensor_reading
	"""
	payload = {
		"carbonmonoxide_sensor_reading": csr,
		"lpg_gas_sensor_reading": lpg, 
		"nitrogendioxide_sensor_reading": nsr, 
		}   

	payload['identifier'] = IDENTIFIER

	r = requests.post(url, data=payload)
	print r.text

if __name__ == '__main__':
	start_upload(identifier=IDENTIFIER, url=url, csr=csr, lpg=lpg, nsr=nsr)