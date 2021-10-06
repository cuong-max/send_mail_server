import os
from settings import MAIL_SERVER
from mail import verify_send_mail

mail_user = os.environ.get('MAIL_USER')
mail_manager = os.environ.get('MAIL_MANAGER')
receivers = f'{mail_user}, {mail_manager}'
subject = 'The contents of mail'
content = "This is some test documentation in the function"

verify_send_mail(receivers, subject, content)
