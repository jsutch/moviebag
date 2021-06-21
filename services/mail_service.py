from threading import Thread
from flask_mail import Message

from app import app
from app import mail

# errors
from resources.errors import EmailServerUnavailable, InternalServerError


def send_async_email(app, msg):
    """
    unbork the "InternalServerError not defined" error at some point
    """
    with app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise EmailServerUnavailable("[MAIL SERVER] not available")
        # except ConnectionRefusedError:
            # raise InternalServerError("[MAIL SERVER] not available")
        except Exception as e:
            return "send_async_app failed with", e
            

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()