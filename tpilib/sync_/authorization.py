import requests

# Получаем токен от аккаунта и наслаждаемся
class Account:

	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.auth_url = 'https://edu-tpi.donstu.ru/Account/Login.aspx'

		self.data = {
			"__VIEWSTATE": "/wEPDwULLTE5Njc0MjQ0ODAPZBYCZg9kFgICAw9kFggCAQ88KwAKAgAPFgIeDl8hVXNlVmlld1N0YXRlZ2QGD2QQFgFmFgE8KwAMAQAWBh4EVGV4dAUO0JPQu9Cw0LLQvdCw0Y8eC05hdmlnYXRlVXJsBQ5+L0RlZmF1bHQuYXNweB4OUnVudGltZUNyZWF0ZWRnZGQCCw8WAh4JaW5uZXJodG1sBTrQrdC70LXQutGC0YDQvtC90L3QvtC1INC/0L7RgNGC0YTQvtC70LjQviDRgdGC0YPQtNC10L3RgtCwZAINDzwrAAkCAA8WAh8AZ2QGD2QQFgFmFgE8KwALAQAWCh8BZR4ETmFtZQUCZ2gfAmUeBlRhcmdldGUfA2dkZAIRDzwrAAQBAA8WAh4FVmFsdWUFHTIwMjEgwqkgQ29weXJpZ2h0IGJ5IE1NSVMgTGFiZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFD2N0bDAwJEFTUHhNZW51MQURY3RsMDAkQVNQeE5hdkJhcjEFKmN0bDAwJE1haW5Db250ZW50JHVjTG9naW5Gb3JtUGFnZSRidG5Mb2dpbj6AgDxOZVnZwij5bL/VFy59O/phPxVn2KrrW7LSWHWF", "ctl00$MainContent$ucLoginFormPage$btnLogin": "(unable to decode value)",

			"ctl00$MainContent$ucLoginFormPage$tbUserName$State": "{&quot;rawValue&quot;:&quot;"+self.email+"&quot;,&quot;validationState&quot;:&quot;&quot;}",
			"ctl00$MainContent$ucLoginFormPage$tbPassword$State": "{&quot;rawValue&quot;:&quot;"+self.password+"&quot;,&quot;validationState&quot;:&quot;&quot;}",
			"ctl00$MainContent$ucLoginFormPage$tbUserName": self.email,
			"ctl00$MainContent$ucLoginFormPage$tbPassword": self.password, 
		}


	def auth(self):
		s = requests.Session()
		req = s.post(self.auth_url, data=self.data)
		try:
			if s.cookies.items()[2][1]: 
				authToken = s.cookies.items()[2][1]
				s.cookies.clear()
				return authToken
			else: return False
		except IndexError as e:				
			return False
