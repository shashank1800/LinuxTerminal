class Terminal:

	def __init__(self):
		self.root = dict()
		self.ref_present = self.root
		self.root_to_pwd = list()
		
	def directory(self,dir_name):
		self.ref_present[dir_name] = dict()
		
	def print_pwd(self):
		s = ""
		for dire in self.root_to_pwd:
			s+="/"+dire
		s += "/"
		print(s)
		
	def commands(self,input_string):
		if input_string.startswith("mkdir"):
			if len(input_string.split())==2:
				dir_name = input_string.split()
				self.directory(dir_name[1])
				
			else:
				print("error:mkdir can have only 1 attribute")

		if input_string =="pwd":
			self.print_pwd()
		
		if input_string.startswith("cd"):
			if len(input_string.split())==2:
				dir_name = input_string.split()
				self.ref_present = self.ref_present[dir_name[1]]
				self.root_to_pwd.append(dir_name[1])
				
			else:
				print("error:cd command can have only 1 attribute")
				
		if input_string =="ls":
			for dire in self.ref_present:
				print(dire)
				

term = Terminal()

while True:
	term.commands(input("$"))
