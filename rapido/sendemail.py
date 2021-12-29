from django.core.mail import EmailMultiAlternatives

def email(request):
    subject, from_email, to = 'hello', 'bookings@rapidotravels.co.in', 'manju24j@gmail.com'
    print "msg1"
    text_content = 'This is an important message.'
    print "msg2"
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    print "msg3"
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    print "msg4"
    msg.attach_alternative(html_content, "text/html")
    print "msg5"
    msg.send()
    print msg
    print "success"
    return " success"

# import smtplib

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# EMAIL_HOST = 'mail.rapidotravels.co.in'

# EMAIL_HOST_USER = 'test@rapidotravels.co.in'

# #Must generate specific password for your app in [gmail settings][1]

# EMAIL_HOST_PASSWORD = 'test123$%'

# EMAIL_PORT = 25


# # server = smtplib.SMTP(host='mail.rapidotravels.co.in', port=25,password='test123$%',user='test@rapidotravels.co.in')
# # me == my email address
# # you == recipient's email address

# # from_email = 'bookings@rapidotravels.co.in'
# # reply_to = ['bookings@rapidotravels.co.in']
# # to = [guest_email,booker_email]

# smtp_server = 'mail.rapidotravels.co.in'
# smtp_user   = 'test@rapidotravels.co.in'
# smtp_pass   = 'test123$%'

# me = "bookings@rapidotravels.co.in"
# you = "manju24j@gmail.com"

# # Create message container - the correct MIME type is multipart/alternative.
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "Link"
# msg['From'] = me
# msg['To'] = you
# print "email1"
# # Create the body of the message (a plain-text and an HTML version).
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
# html = """\
# <html>
#   <head></head>
#   <body>
#     <p>Hi!<br>
#        How are you?<br>
#        Here is the <a href="http://www.python.org">link</a> you wanted.
#     </p>
#   </body>
# </html>
# """
# print "html"

# # Record the MIME types of both parts - text/plain and text/html.
# part1 = MIMEText(text, 'plain')
# part2 = MIMEText(html, 'html')

# print "aaded html content"

# # Attach parts into message container.
# # According to RFC 2046, the last part of a multipart message, in this case
# # the HTML message, is best and preferred.
# msg.attach(part1)
# msg.attach(part2)
# print "aaded html content"


# s = smtplib.SMTP(host='mail.rapidotravels.co.in')
# s.login(smtp_user,smtp_pass)
# s.sendmail(me, you, msg.as_string())
# s.quit()

# # Send the message via local SMTP server.
# # print "attach smtp"
# # s = smtplib.SMTP('localhost')
# # # sendmail function takes 3 arguments: sender's address, recipient's address
# # # and message to send - here it is sent as one string.
# # s.sendmail(me, you, msg.as_string())
# print "email send aytu"
# print s
# s.quit()
# print "stop aytu"