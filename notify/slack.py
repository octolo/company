from company.notify import NotifyBackend
from mighty.applications.messenger import notify_slack

class SlackCompany(NotifyBackend):
    @property
    def slack_self(self):
        return self.company.denomination

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
				"text": "<%s| %s :link:>" % (self.url_domain(self.company.admin_change_url), self.slack_self)
		}},
		{ "type": "divider" }]

    def send_msg_create(self):
        text = "New company on the platform : %s" % self.company.date_create.strftime('%Y-%m-%d %H:%M')
        notify_slack("notifications", text=text, blocks=self.slack_msg_creation)
