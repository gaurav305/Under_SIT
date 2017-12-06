import sys
import webbrowser as wb
import simplejson as json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from restkit import Resource, BasicAuth, request

def openJIRA(jiraID):
    server_url = 'https://jira.markit.com'
    issue_url = "%s/browse/%s" % (server_url, jiraID)

    if (jiraID != None):
        print "Opening JIRA:", jiraID
        wb.open(issue_url)
    else:
        sys.exit(2)

def createTask(server_base_url, user, password, project, task_summary):
    auth = BasicAuth(user, password)

    resource_name = "issue"
    complete_url = "%s/rest/api/latest/%s/" % (server_base_url, resource_name)
    resource = Resource(complete_url, filters=[auth])

    try:
        data = {
            "fields": {
                "project": {
                    "key": project
                },
                "summary": task_summary,
                "issuetype": {
                    "name": "Task"
                }
            }
        }
        response = resource.post(headers={'Content-Type': 'application/json'}, payload=json.dumps(data))
    except Exception, ex:
        print "EXCEPTION: %s " % ex.msg
        return None

    if response.status_int / 100 != 2:
        print "ERROR: status %s" % response.status_int
        return None

    issue = json.loads(response.body_string())
    print issue

    openJIRA(issue['key'])

    # send_mail(issue['key'])

    return issue

def send_mail(issue):

    # server = smtplib.SMTP('smpt.markit.com', 587)
    # server.login("gaurav.saini", "MotorolaX4153!")
    #
    # msg= "This is an Auto-Generated Mail" \
    #      "Hi Team" \
    #      "There was an error found while performing RFB checks on MIS" +issue +"has been raised." \
    #      "Thanks & Regards" \
    #      "Gaurav Saini"
    #
    # server.sendmail("gaurav.saini@ihsmarkit.com", "vikrant.rajoria@ihsmarkit.com", msg)
    me = "gaurav.saini@ihsmarkit.com"
    you = "gaurav.saini@ihsmarkit.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "FRTB RFB Checks Complete"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "FRTB RFB Checks"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi<br>
           
        There was an error found while performing RFB checks on MIS issue: """+issue['key']+"""has been raised." <br>
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

if __name__ == '__main__':
    project = 'FRTB'
    task_summary = 'Task'

    # if (len(sys.argv) != 3):
    #     print "Usage: %s project task_summary" % sys.argv[0]
    #     sys.exit(1);

    server_url = 'https://jira.markit.com'

    username = "gaurav.saini"
    password = "MotorolaX5477!"

    # project = sys.argv[1]
    # task_summary = sys.argv[2]

    issue = createTask(server_url, username, password, project, task_summary)
    issue_code = issue["key"]
    issue_url = "%s/browse/%s" % (server_url, issue_code)

    send_mail(issue_code)

    if (issue != None):
        print issue
        wb.open(issue_url)
    else:
        sys.exit(2)