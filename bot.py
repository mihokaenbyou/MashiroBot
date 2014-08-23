#!/usr/bin/env python2

from __future__ import print_function
import sys
#import ConfigParser
from ConfigParser import ConfigParser, RawConfigParser
from sys import exit
#from datetime import datetime, timedelta

import irc.bot
import irc.client
import irc.modes

__VERSION__ = "1.0-dev"

class MashiroBot(irc.bot.SingleServerIRCBot):
	def __init__(self):
		# read configuration file
		config = RawConfigParser()
		config.read('conf/config.ini')

		# get server information from the configuration file
		self.server = config.get("irc", "server")
		self.port = int(config.get("irc", "port"))
		self.nickname = config.get("irc", "nickname")
		self.realname = config.get("irc", "realname")
		self.nspasswd = config.get("nickserv", "passwd")
		self.channel = config.get("irc", "channel")
		self.reconnection_interval = config.get("misc", "reconnection_interval")

		irc.bot.SingleServerIRCBot.encoding = 'utf-8'
		irc.bot.SingleServerIRCBot.__init__(self, [(self.server, self.port)], self.nickname, self.realname, self.reconnection_interval)

	def on_welcome(self, server, e):
		message = e.arguments[0]
		print(message)
		server.join(self.channel)

if __name__ == '__main__':
    bot = MashiroBot()
    try:
        bot.start()
    except KeyboardInterrupt:
        bot.disconnect()
        exit(1)
