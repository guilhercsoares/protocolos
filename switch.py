class Switch(object):
	#
	def __init__(self, name):
		self.name = name
		self.ports = {}
		self.rules = []

	def addPort(self, port_idx, dest):
		self.ports[dest] = port_idx

	def addRule(self, rule):
		self.rules.append(rule)

	def showRules(self):
		print self.name,"=>",self.rules
