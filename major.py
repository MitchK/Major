import yaml
import imp
import os
from os import listdir
from os.path import isfile, join

stream = file('Majorfile', 'r')
major_file = yaml.load(stream)

context = {}

print(major_file)

for module in major_file:
	for plugin in major_file[module]:
		source = imp.load_source('module.name', os.path.join(os.environ['MAJOR_PATH'], 'modules', module, plugin + '.py'))
		source.plugin(context, major_file[module][plugin])

