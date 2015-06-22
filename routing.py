from dijkstra import *
from graph_topo import *

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



def getPort(switch, node):
	return switch.ports[node]

def Ports(path, switches):
	ports = {}
	origem = path[0]
	destino = path[len(path)-1]

	succ = 1
	predecessor = origem
	sucessor = switches[succ].name
	for node in range(0,len(switches)):
		switch = switches[node]
		out_port = getPort(switch,sucessor)
		ports[switch.name] = (destino,out_port)
		predecessor = switch.name

		if succ + 1 < len(switches):
			succ = succ+1
			sucessor = switches[succ].name
		else:
			sucessor = destino

	return ports

def getSwitch(node, switches):
	for s in switches:
		if s.name == node:
			return s

def getAllSwitches(switches,T, P):
	all_switches = []
	for sw in switches:
		x = Switch(sw)
		p = P[sw]
		#p_idx = 1
		for link in p:
			#print p
			x.addPort(link[1],link[0])
			#p_idx = p_idx + 1
		all_switches.append(x)
	return all_switches

def getOrigemDestino(path):
	return (path[0],path[len(path)-1])

def getSwitchesPath(path, hosts,all_switches):
	path_ = []
	for node in path:
		if node not in hosts:
			s = getSwitch(node, all_switches) #obtem os objetos dos switches que fazem parte do caminho, para descobrir a porta
			path_.append(s)
	return path_

#{'s1': ('h5', 6), 's7': ('h5', 5), 's5': ('h5', 4)}
def setRules(rules, all_switches):
	for switch in rules.keys():
		s = getSwitch(switch,all_switches)
		if rules[switch] not in s.rules:
			s.addRule(rules[switch])

def allRules(switches):
	rules = {}
	for switch in switches:
		rules[switch.name] = switch.rules
	return rules

def getMAC(host):
	return MAC[host]

def run(hosts, switches, T, all_switches):
	for origem in hosts:
		for destino in hosts:
			if origem != destino:
				path =  shortestPath(T,origem,destino)
				#all_switches = getAllSwitches(switches,T)
				path_ = getSwitchesPath(path,hosts,all_switches)
				hosts_ = getOrigemDestino(path)
				origem = hosts_[0]
				destino = hosts_[1]
				rulesPath = Ports(path,path_)
				#print rulesPath
				setRules(rulesPath,all_switches)


all_switches = getAllSwitches(switches,T,P)
run(hosts, switches, T, all_switches)
all_rules = allRules(all_switches)

# Dijkstra ja rodado, caminhos definidos, faltam as mensagens

print "Topologia"
for e in switches:
	print e,"=>",T[e]

print "Portas"
for sw in all_switches:
	print sw.name,"=>",sw.ports

print "MACs"
for h in hosts:
	print MAC[h]

print "Regras"
for rule in all_rules.keys():
	print rule,"=>",all_rules[rule]
