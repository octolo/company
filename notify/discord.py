from mighty.applications.logger.notify.discord import DiscordLogger

class DiscordCompany(DiscordLogger):
    def __init__(self, company):
        self.company = company

    @property
    def discord_msg_creation(self):
        return {
        "content": ":office: New company on the platform : %s" % self.company.date_create.strftime('%Y-%m-%d %H:%M'),
        "embeds": [{
            "title": ":office: New company on the platform : %s" % self.company.date_create.strftime('%Y-%m-%d %H:%M'),
            "description": "[%s :link:](%s)" % (self.company.denomination, self.url_domain(self.company.admin_change_url))
        }]}

    def send_msg_create(self):
        self.send_msg(self.discord_msg_creation)
