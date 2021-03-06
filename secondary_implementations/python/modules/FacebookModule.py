import requests
from AbstractModule import AbstractModule

class FacebookModule(AbstractModule):
	def try_login(self, uname, password):
		headers = { 'user-agent': AbstractModule().user_agent() }
		resp = requests.get("https://www.facebook.com", headers= headers)

		payload = {'email': uname, 'pass': password}
		loginResp = requests.post("https://www.facebook.com/login.php", data= payload, headers= headers, cookies=resp.cookies, allow_redirects=False)
		
		if loginResp.status_code == 302:
			return True
		else:
			return False

facebook = FacebookModule()