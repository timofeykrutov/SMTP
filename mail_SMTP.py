import smtplib                                      # Импортируем библиотеку по работе с SMTP
#pip install secure-smtplib
# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage              # Изображения

# Функция отправки результатов теста на почтовый ящик gmail
def send_test_results(student_group, student_name, test_result, amount_of_answers):
    # Создание сообщения
    msg = MIMEMultipart()

    to_email = 'to_email@gmail.com'
    message = 'message'

    login = "login@gmail.com"
    password = "password"

    msg['Subject'] = 'Группа: ' + str(student_group) + '. Студент: ' + str(student_name) + '. Результат: ' + str(test_result) + '/' + str(amount_of_answers) + ' баллов.'

    msg.attach(MIMEText(message,'plain'))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # server = smtplib.SMTP('smtp.yandex.ru', 465) 
    server.starttls()
    server.login(login,password)
    server.sendmail(login, login, msg.as_string())
    server.quit()
