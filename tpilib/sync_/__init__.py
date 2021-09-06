import requests
import json
import datetime
from jwt_upd import JWtoken

# Получаем токен от аккаунта и наслаждаемся
class User:


	"""
	METHODS_URL = {

		/GET/
		Авторизация: https://edu-tpi.donstu.ru/Account/Login.aspx
		Все сообщения: https://edu-tpi.donstu.ru/api/Mail/InboxMail
		Непрочитанные сообщения: https://edu-tpi.donstu.ru/api/Mail/CheckMail
		Конкретное сообщение: https://edu-tpi.donstu.ru/api/Mail/InboxMail?&id={id}
		Просмотр студентов в группе: https://edu-tpi.donstu.ru/api/Mail/Find/Students?groupID={groupID}
		Поиск студента по ФИО: https://edu-tpi.donstu.ru/api/Mail/Find/Students?fio={fio}
		Поиск преподователя по ФИО: https://edu-tpi.donstu.ru/api/Mail/Find/Prepods?fio={fio}
		Список всех групп в {N-N} учебном году: https://edu-tpi.donstu.ru/api/groups?year={N1}-{N2}
		Информация об аккаунте: https://edu-tpi.donstu.ru/api/tokenauth
		Информация о студенте: https://edu-tpi.donstu.ru/api/UserInfo/Student?studentID=-{studentID}
		Возвращает максимульный/минимальный/текущий день расписания группы GROUP: https://edu-tpi.donstu.ru/api/GetRaspDates?idGroup=GROUP 
		Возвращает расписание группы GROUP с DATE: https://edu-tpi.donstu.ru/api/Rasp?idGroup=GROUP&sdate=DATE

		/POST/
		Отправить сообщение на почту: https://edu-tpi.donstu.ru/api/Mail/InboxMail


	}
	"""

	def __init__(self, token):
		self.authToken = "Bearer {}".format(token)
		self.url_api = "https://edu-tpi.donstu.ru/api/"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36",
			"authorization": self.authToken,
			"Content-Type": "application/json; charset=utf-8"
		}

	def checking_unread_messages(self):
		return requests.get(f"{self.url_api}Mail/CheckMail", headers=self.headers).json()

	def checking_all_mail(self, page: int = 1):
		return requests.get(f"{self.url_api}Mail/InboxMail?page=1&pageEl=15&unreadMessages=false&searchQuery=", headers=self.headers).json()

	def read_mail_message(self, messageID):
		for msg in self.checking_all_mail()['data']['messages']:
			if msg['messageID'] == messageID:
				return requests.get(f"{self.url_api}Mail/InboxMail?id={msg['id']}", headers=self.headers).json()['data']['messages'][0]

	def find_stundent(self, fio):
		return requests.get(f"{self.url_api}Mail/Find/Students?fio={fio}", headers=self.headers).json()


	def find_teacher(self, fio):
		return requests.get(f"{self.url_api}Mail/Find/Prepods?fio={fio}", headers=self.headers).json()

	def all_groups_year(self, year: int = datetime.datetime.now().year):
		return requests.get(f"{self.url_api}groups?year={year}-{year+1}").json()

	def send_message(self, statusID, from_user, title_message, text_message, type_message: int = 1):

		if statusID == 0:
			usertoID = self.find_stundent(fio=from_user)['data']['arrStud']
		elif statusID == 1:
			usertoID = self.find_teacher(fio=from_user)['data']['arrPrep']
		elif statusID == 2:
			pass

		print(usertoID)
		data = {
			"markdownMessage": text_message,
			"htmlMessage": "",
			"message": "",
			"theme": title_message,
			"userToID": usertoID,
			"typeID": type_message,
		}
		req = requests.post(f"{self.url_api}Mail/InboxMail", data=json.dumps(data), headers=self.headers)

	def infoAccount(self):
		return requests.get(f"{self.url_api}tokenauth", headers=self.headers).json()

	def infoStudent(self, studentID):
		return requests.get(f"{self.url_api}UserInfo/Student?studentID={studentID}", headers=self.headers).json()

	def infoRasp(self, groupID, sdate = datetime.datetime.now().strftime("%Y-%m-%d")):
		return requests.get(f"{self.url_api}Rasp?idGroup={groupID}&sdate={sdate}", headers=self.headers).json()
