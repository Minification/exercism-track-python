from abc import ABC, abstractmethod

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other
        
    def __str__(self):
    	return f"SgfTree( properties={self.properties}, children={self.children} )"
    	
    def __repr__(self):
    	return self.__str__()
        
class Parser(ABC):

	def __init__(self, parent):
		self.parent = parent
		
	@abstractmethod
	def parse(self, the_string: str, index: int) -> None:
		pass
		
class PropertyNameParser(Parser):

	def parse(self, the_string: str, index: int) -> None:
		prop = ""
		current = the_string[index]
		idx = index
		while current != "[":
			if not current.isupper():
				raise ValueError("Property names must be caps!")
			prop += current
			idx += 1
			current = the_string[idx]
		self.parent.advance(idx - index)
		if not prop:
			raise ValueError("Properties must have names!")
		self.parent.foundProperty(prop)
		self.parent.set_parser(ValuesParser(self.parent))
		
class ValuesParser(Parser):

	def parse(self, the_string: str, index: int) -> None:
		value = ""
		values = []
		current = the_string[index]
		idx = index
		escaped = False
		if current != "[":
			raise ValueError("Properties must have values!")
		while current not in "();ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
			# Skip [
			idx += 1
			current = the_string[idx]
			# Read value, i.e., read until unescaped ]
			while current != "]" or escaped:
				if current == "\\":
					escaped = True
					idx += 1
					current = the_string[idx]
					continue
				value += current
				idx += 1
				current = the_string[idx]
				if escaped:
					escaped = False
			# Skip closing ]
			idx += 1
			current = the_string[idx]
			# Record that we had a value and reset
			values.append(value.replace("\t", " "))
			value = ""
		self.parent.advance(idx - index + 1)
		self.parent.foundValues(values)
		if current == ")":
			self.parent.finishNode()
			self.parent.finishTree()
			# Get ready to parse another tree
			self.parent.set_parser(TreeParser(self.parent))
		elif current == "(":
			self.parent.advance(-1)
			# Get ready to parse another tree
			self.parent.set_parser(TreeParser(self.parent))
		elif current == ";":
			self.parent.finishNode()
			# We have to parse a node next
			self.parent.set_parser(NodeParser(self.parent))
		else:
			self.parent.advance(-1)
			self.parent.set_parser(PropertyNameParser(self.parent))
			
class NodeParser(Parser):

	def parse(self, the_string: str, index: int) -> None:
		if the_string[index] != ";":
			raise ValueError("Expected node but not found!")
		idx = index + 1
		self.parent.startNode()
		if the_string[idx] == ")":
			# Skip ), finish node and then we can get ready to read another tree
			idx += 1
			self.parent.set_parser(TreeParser(self.parent))
			self.parent.finishNode()
			self.parent.finishTree()
		else :
			self.parent.set_parser(PropertyNameParser(self.parent))
		self.parent.advance(idx - index)
			
		
class TreeParser(Parser):

	def parse(self, the_string: str, index: int) -> None:
		if the_string[index] not in "()":
			raise ValueError("Tree expected but not found!")
		if the_string[index] == ")":
			self.parent.finishNode()
			self.parent.finishTree()
			return
		self.parent.startTree()
		# Skip (, then prepare to parse node
		self.parent.advance(1)
		self.parent.set_parser(NodeParser(self.parent))
        
class SgfParser:

	def __init__(self, the_string: str):
		self.the_string = the_string
		self.current_parser = TreeParser(self)
		self.index = 0
		self.current_propery = ""
		self.stack = []
		self.root = None
		
	def set_parser(self, parser):
		self.current_parser = parser
	
	def parse(self):
		if self.the_string == "":
			raise ValueError("Empty string not allowed!")
		while self.index < len(self.the_string):
			self.current_parser.parse(self.the_string, self.index)
		print(self.root)
		return self.root
		
	def advance(self, steps: int):
		self.index += steps
		
	def startNode(self):
		print("startNode")
		self.stack.append(SgfTree())
		
	def finishNode(self):
		print(f"finishNode: {', '.join(str(e) for e in self.stack)}")
		if self.stack:
			finished_node = self.stack.pop()
			if self.stack:
				self.stack[-1].children.append(finished_node)
			else:
				self.root = finished_node
		
	def startTree(self):
		pass
		
	def finishTree(self):
		pass
		
	def foundValues(self, values):
		self.stack[-1].properties[self.current_property] = values
		
	def foundProperty(self, prop):
		self.current_property = prop
		


def parse(input_string):
	parser = SgfParser(input_string)
	return parser.parse()
