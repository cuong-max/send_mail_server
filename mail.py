import smtplib
from email.message import EmailMessage
import logging
from settings import MAIL_SERVER

logger = logging.getLogger(__name__)


def verify_send_mail(receivers, subject, content):
    """
    Send mail warning to receivers with subject and content
    """
    sender = MAIL_SERVER['MAIL_SENDER']
    password = MAIL_SERVER['MAIL_PASSWORD']
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receivers.split(',')
    msg.set_content(content)

    try:
        session = smtplib.SMTP_SSL(MAIL_SERVER['MAIL_SERVER_IP'], MAIL_SERVER['MAIL_SERVER_PORT'])
        session.login(sender, password)
        session.send_message(msg)
        session.quit()
        logger.info(f'Send mail from {sender} to {receivers} successfully')
    except Exception as e:
        logger.warning(f"Can't send mail from {sender} to {receivers}: {e}")
