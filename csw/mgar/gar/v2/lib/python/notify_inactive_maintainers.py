#!/opt/csw/bin/python2.7
# coding: utf-8

import anydbm
import datetime
import dateutil.parser
import jinja2
import json
import logging
import os
import os.path
import requests
import smtplib
import textwrap

from Cheetah import Template
from email.mime.text import MIMEText

from lib.python import activity

EMAIL_OF_PERSON_RUNNING_THIS_SCRIPT = '<please-enter>@opencsw.org'
PERSON_RUNNING_THIS_SCRIPT = 'Firstname Lastname'

EMAIL_TMPL = """If you don't care about OpenCSW packages,
you can stop reading now.

Hi {{ firstname }},

{% if maintainer.pkgs %}
It's been {{ time_ago }} since you last uploaded a package. 
There still are packages in the unstable catalog that are owned by you.
{% else %}
{{ time_ago.capitalize() }} ago, you've signed up to be a package maintainer at
OpenCSW, but I looked in the unstable catalog, and I don't see any packages
from you in there.
{% endif %}

What's the situation on your end, are you still interested in building packages
at OpenCSW? If so, please write back to me. If not, you can ignore this
message, and I will retire your account. This means that I will lock down your
buildfarm access, take away write access to the Subversion repository, and your
@opencsw.org email address will start bouncing messages. I won't delete your
home directory on the buildfarm.

This is all reversible, if you wish to get your access back, write to
board@opencsw.org and your access will be restored.

--Maciej
"""

class Notifier(object):

  def __init__(self):
    filename = os.path.join(os.environ['HOME'],
                            '.checkpkg',
                            'retiring-notifications.db')
    logging.info('Keeping state in %s', filename)
    self.state = anydbm.open(filename, 'c')

  def Notify(self, address, subject, message):
    # logging.info('Would send email to %s', address)
    # print message
    # return
    address = address.encode('utf-8')
    if address in self.state:
      state = json.loads(self.state[address])
      logging.info('%s was already notified on %s', address, state['date'])
      return
    else:
      state = {
          'address': address,
          'subject': subject,
          'message': message,
          'date': datetime.datetime.now(),
      }
    msg = MIMEText(message)
    msg["Subject"] = subject
    from_address = '%s <%s>' % (PERSON_RUNNING_THIS_SCRIPT,
                                EMAIL_OF_PERSON_RUNNING_THIS_SCRIPT)
    msg['From'] = from_address
    msg['To'] = address
    msg['Bcc'] = EMAIL_OF_PERSON_RUNNING_THIS_SCRIPT
    msg['Cc'] = 'OpenCSW board <board@opencsw.org>'
    s = smtplib.SMTP('mail.opencsw.org')
    try:
      logging.info('Sending email to %s', address)
      addresses = [address, 'board@opencsw.org',
                   EMAIL_OF_PERSON_RUNNING_THIS_SCRIPT]
      s.sendmail(from_address,
          addresses,
          msg.as_string())
      logging.debug("E-mail sending finished.")
      self.state[address] = json.dumps(state, cls=activity.DateTimeEncoder)
    except smtplib.SMTPRecipientsRefused as exc:
      logging.warning(
          "Sending email to %s failed: %s.",
          repr(address), exc)
    s.quit()

def main():
  # This data can be generated on the fly, but for now we'll just use
  # previously generated data.
  url = 'http://buildfarm.opencsw.org/obsolete-pkgs/maintainer-activity.json'
  data = requests.get(url).json()
  maintainers = data['maintainers']
  analysis_by_username = data['analysis_by_username']
  notifier = Notifier()
  for username in maintainers:
    if username in activity.MAINTAINER_WHITELIST:
      logging.debug('Skipping %s (is on the whitelist)', username)
      continue
    if not analysis_by_username[username]['to_retire']:
      continue
    maintainer = activity.Maintainer(*maintainers[username])
    logging.debug('to retire: %s / %s', maintainer.username, maintainer.fullname)
    maintainer = maintainer._replace(
        last_activity=dateutil.parser.parse(maintainer.last_activity))
    if maintainer.date_created:
      maintainer = maintainer._replace(
          date_created=dateutil.parser.parse(maintainer.date_created))
    else:
      maintainer = maintainer._replace(
          date_created=dateutil.parser.parse('1970-01-01'))
    activity_date = max(maintainer.date_created, maintainer.last_activity)
    months_ago = int((datetime.datetime.now() - activity_date).days / 30 + 0.5)
    if months_ago > 12 * 20:
      time_ago = 'some time'
    elif months_ago > 12:
      time_ago = 'about %d years' % ((months_ago + 6) / 12)
    else:
      time_ago = 'about %d months' % months_ago

    rendered_paragraphs = []
    assert maintainer.fullname is not None, ('Error in the DB somewhere, '
                                             'check the maintainer table '
                                             'in the CSW database on the '
                                             'website')
    for paragraph in EMAIL_TMPL.split('\n\n'):
      template = jinja2.Template(paragraph)
      rendered = template.render(
          firstname=maintainer.fullname.split(' ')[0],
          maintainer=maintainer,
          time_ago=time_ago,
          status=analysis_by_username[username])
      rendered_paragraphs.append(textwrap.fill(rendered.strip()))
    message = '\n\n'.join(x.encode('utf-8') for x in rendered_paragraphs)
    notifier.Notify('%s@opencsw.org' % username,
                    'Cleanup of inactive maintainer accounts', message)


if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  main()
