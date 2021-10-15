import os
from settings import MAIL_SERVER
from mail import verify_send_mail

mail_user = os.environ.get('MAIL_USER')
mail_manager = os.environ.get('MAIL_MANAGER')
receivers = f'{mail_user}, {mail_manager}'
subject = 'The contents of mail'

id = 1
code = 21
lb_type = 'A10'
mgmt_ips = '192.168.1.1'
usr_manager = 'cuongmax'
error_msg = 'Error: Username/Password wrong'

work_dir = os.getcwd()
data = f'{work_dir}/lb.html'

with open(data, 'r') as f:
    content = f.read().format(id=id, code=code,
                              lb_type=lb_type,
                              mgmt_ips=mgmt_ips,
                              usr_manager=usr_manager,
                              error_msg=error_msg)

verify_send_mail(receivers, subject, content)
