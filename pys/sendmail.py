# import smtplib

# s = smtplib.SMTP('smtp.gmail.com', 587)

# s.starttls()

# s.login("loharprathmesh2023@gmail.com", "itemvftaejglfial")
# message = "code is"

# s.sendmail("loharprathmesh2023@gmail.com", "loharprathmesh123@gmail.com", message)
# s.quit()

from email.message import EmailMessage
import ssl
import smtplib

sender = 'loharprathmesh2023@gmail.com'
rec = 'loharprathmesh123@gmail.com'
pwd = 'itemvftaejglfial'

subject = "Verification For Sathi"

x = "jssc"


body = "Verification Code :" + x

em = EmailMessage()
em['From'] = sender
em['To'] = rec
em['subject'] = subject
em.set_content(body)

contex = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=contex) as smtp:
    smtp.login(sender,pwd)
    smtp.sendmail(sender,rec,em.as_string())
