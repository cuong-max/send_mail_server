import os

MAIL_SERVER = {
    'MAIL_SERVER_IP': 'smtp.viettel.com.vn',
    'MAIL_SERVER_PORT': 465,
    'MAIL_SENDER': os.environ.get('MAIL_SENDER'),
    'MAIL_PASSWORD': os.environ.get('MAIL_PASSWORD'),
    'MAIL_MANAGER': os.environ.get('MAIL_MANAGER')
}
