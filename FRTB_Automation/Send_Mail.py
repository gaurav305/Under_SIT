import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "gaurav.saini@ihsmarkit.com"
you = "gaurav.saini@ihsmarkit.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "FRTB RFB Checks Status Report"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       There was an error found while performing RFB checks on MIS issue: has been raised." <br>
          "Thanks & Regards" 
          "Gaurav Saini"
             
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('uksmtp.markit.partners')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()



# import smtplib
# # from smtplib import *

#
# server = smtplib.SMTP('uksmtp.markit.partners')
# server.login("gaurav.saini@ihsmarkit.com", "MotorolaX4153!")
#
# msg= "This is an Auto-Generated Mail" \
#      "Hi Team" \
#      "There was an error found while performing RFB checks on MIS issue has been raised." \
#      "Thanks & Regards" \
#      "Gaurav Saini"
#
# server.sendmail('gaurav.saini@ihsmarkit.com', 'vikrant.rajoria@ihsmarkit.com', msg)