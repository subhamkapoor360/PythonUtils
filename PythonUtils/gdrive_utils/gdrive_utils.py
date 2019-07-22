def download_file_from_google_drive(id, destination):
	'''
	file_id_map = {
		"train_identity.csv.zip":"12PbACvaeU7htbS5jjdBM_gB0z_S7Kjnb",
		"train_transaction.csv.zip":"1OdGYi4Z4JKhx2aMjcB2ugQx8OiXp-ZoI",
		"test_transaction.csv.zip":"1LtM_49Y2QEjSBdpmODMvJmbZhX4-MOQc",
		"test_identity.csv.zip":"1QxyUrDv_ZPlkLw7Ohqech1CaYKaOKuER",
		"sample_submission.csv.zip":"1kh7clvggqpIKtKWAJn5d9xe1RCG1A3nE",   
		}
	for destination ,file_id in file_id_map.items():
		download_file_from_google_drive(file_id, destination)

	'''

	def get_confirm_token(response):
		for key, value in response.cookies.items():
			if key.startswith('download_warning'):
				return value

		return None

	def save_response_content(response, destination):
		CHUNK_SIZE = 32768

		with open(destination, "wb") as f:
			for chunk in response.iter_content(CHUNK_SIZE):
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)

	URL = "https://docs.google.com/uc?export=download"

	session = requests.Session()

	response = session.get(URL, params = { 'id' : id }, stream = True)
	token = get_confirm_token(response)

	if token:
		params = { 'id' : id, 'confirm' : token }
		response = session.get(URL, params = params, stream = True)

	save_response_content(response, destination)    

