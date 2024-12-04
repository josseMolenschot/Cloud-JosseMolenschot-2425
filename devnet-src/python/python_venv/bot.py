from webex_bot.webex_bot import WebexBot

import os

webex_token = os.environ["WEBEX_TOKEN"]

bot = WebexBot(webex_token, approved_domains=["student.odisee.be"])

bot.run()