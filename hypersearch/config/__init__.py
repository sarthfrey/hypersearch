import yaml
import os


class ConfigFile():

	def __init__(self, name):
		self.name = name
		self.type = name.split('.')[-1]
		self.top_path = os.path.dirname(__file__)
		self.file_path = os.path.join(self.top_path, name)

	def load(self):
		with open(self.file_path, 'r') as f:
			if self.type == 'yaml':
				return yaml.load(f)
			else:
				raise ValueError('file type not supported')
