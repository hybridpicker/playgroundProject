import re
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


'''
Contact playground
'''
def contact_mail(from_email, subject, message, send_mail=True):
    subject = 'Anfrage: ' + subject
    html_message = render_to_string('templates/mail/answer_mail_template.html', {'context': 'values',
                                                                         'message': message})
    plain_message = strip_tags(html_message)
    to = 'service@blessond.com'

    if send_mail:
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
