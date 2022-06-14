from mighty.applications.logger.notify.slack import SlackLogger

class SlackCompany(SlackLogger):
    def __init__(self, company):
        self.company = company

    @property
    def slack_msg_creation(self):
        return [{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": ":office: New company on the platform : %s" % self.company.date_create.strftime('%Y-%m-%d %H:%M'),
				"emoji": True
		}},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<%s| %s :link:>" % (self.url_domain(self.company.admin_change_url), self.company.denomination)
		}},
		{ "type": "divider" }]

    def send_msg_create(self):
        msg = "New company on the platform : %s" % self.company.date_create.strftime('%Y-%m-%d %H:%M')
        self.send_msg(msg, self.slack_msg_creation)
