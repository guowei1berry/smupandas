import email_sender
import os
import datetime

now = datetime.datetime.now()
current_date = now.date()

from_email = 'oneberrysmucoolschools@gmail.com'
to_email = 'du.guowei@oneberry.com'
subject = f'{current_date} - Daily Data for 2023-SMU001/01'
body = f'{current_date} - Daily Data for 2023-SMU001/01'
folder_path = f'/home/ftpsensor_user/daily_compiled/aggregation/daily_Aggregation/{current_date}'

attachment_folder = os.listdir(folder_path)
attachment_paths = []

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
for f in files:
    # print('f',f)
    attachment_paths.append(f'{folder_path}/{f}')

# print('attachment_paths',attachment_paths)
email_sender.send_email(from_email, to_email, subject, body,attachment_paths, smtp_server='smtp.gmail.com', smtp_port=587)

