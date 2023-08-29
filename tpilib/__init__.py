# pip library by feb

from .sync_ import (User, Account, Journals)
from .async_ import (User)

# ----------------------

"""
	METHODS_URL = {

		/GET/
		Все сообщения: /Mail/InboxMail
		Непрочитанные сообщения: /Mail/CheckMail
		Конкретное сообщение: /Mail/InboxMail?&id={id}
		Просмотр студентов в группе: /Mail/Find/Students?groupID={groupID}
		Поиск студента по ФИО: /Mail/Find/Students?fio={fio}
		Поиск преподователя по ФИО: /Mail/Find/Prepods?fio={fio}
		Список всех групп в {N-N} учебном году: /groups?year={N1}-{N2}
		Информация об аккаунте: /tokenauth
		Информация о студенте: /UserInfo/Student?studentID=-{studentID}
		Возвращает максимульный/минимальный/текущий день расписания группы GROUP: /GetRaspDates?idGroup=GROUP 
		Возвращает расписание группы GROUP с DATE: /Rasp?idGroup=GROUP&sdate=DATE
		Возвращает задолженности студента: /StudentsDebts/list?studentID={studentID}
		Возвращает ленту пользователя: /Feed?userID={userID}&startDate=null
[admin]	Возвращает достижения всех пользователей: /Portfolio/Verifier/ListWorks?year={year}&sem=-1&finished={veref}&type={typeVeref}
[admin] Возвращает все файлы приклеплённые к работе: /Portfolio/FilesList?workID={workID}

		/POST/
		Авторизация: https://edu-tpi.donstu.ru/Account/Login.aspx
		Отправить сообщение на почту: /Mail/InboxMail
[admin]	Создание чата: /Chats/Chat
"""		