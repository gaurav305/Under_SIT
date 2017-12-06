attachments = ['test1.txt','test2.txt']

host = 'uksmtp.markit.partners' # specify port, if required, using this notations

fromaddr = 'gaurav.saini@ihsmarkit.com' # must be a vaild 'from' address in your GApps account
toaddr  = 'vikrant.rajoria@ihsmarkit.com'
replyto = fromaddr
msgsubject = 'MIS RFB Checks Complete !'

htmlmsgtext = """<h2>FTRB Ready-For-Business Checks Complete!</h3>
                 <p>\
                 <h4>This is an Automated Mail<h4>
                 Hi Team, </br> \
                 FRTB RFB Checks are complete now.\
                 MIS Status report EOD Jobs have failed and""" +New_Jira.issue+ """has been reported.</br>\
                 Please let me know if any queries.</br></br>\
                 Thanks,</br>\
                 Gaurav Saini                 </p>
                """

######### In normal use nothing changes below this line ###############

import smtplib, os, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from HTMLParser import HTMLParser
import FRTB_MIS.py
import New_Jira


# A snippet - class to strip HTML tags for the text version of the email

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

########################################################################

try:
    # Make text version from HTML - First convert tags that produce a line break to carriage returns
    msgtext = htmlmsgtext.replace('</br>',"\r").replace('<br />',"\r").replace('</p>',"\r")
    # Then strip all the other tags out
    msgtext = strip_tags(msgtext)

    # necessary mimey stuff
    msg = MIMEMultipart()
    msg.preamble = 'This is a multi-part message in MIME format.\n'
    msg.epilogue = ''

    body = MIMEMultipart('alternative')
    body.attach(MIMEText(msgtext))
    body.attach(MIMEText(htmlmsgtext, 'html'))
    msg.attach(body)

    if 'attachments' in globals() and len('attachments') < 0: # are there attachments?
        for filename in attachments:
            f = filename
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(f,"rb").read() )
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)

    msg.add_header('From', fromaddr)
    msg.add_header('To', toaddr)
    msg.add_header('Subject', msgsubject)
    msg.add_header('Reply-To', replyto)

    # The actual email sendy bits
    smtpObj = smtplib.SMTP(host)
    smtpObj.sendmail(fromaddr, toaddr, msg.as_string())
    print "Email sent successfully"
except:
    print ('Email NOT sent to %s successfully. %s ERR: %s %s %s ', str(toaddr), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2]) )
    #just in case