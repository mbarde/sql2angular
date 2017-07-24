class StringBuilder:

	def __init__(self):
		self.__string = ''
		self.__indentation_level = 0

	def addLine(self, line):
		h = ''
		i = 0
		while i < self.__indentation_level:
			h += '\t'
			i += 1
		self.__string += h + line + '\n'

	def increaseIndentation(self):
		self.__indentation_level += 1

	def decreaseIndentation(self):
		self.__indentation_level += -1

	def setIndentation(self, indentation_level):
		self.__indentation_level = indentation_level

	def getString(self):
		return self.__string
