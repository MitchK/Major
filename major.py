import yaml
import imp
import os
from os import listdir
from os.path import isfile, join

stream = file('Majorfile', 'r')
modules = yaml.load(stream)

context = {
	'plugins': []
}
for item in modules:
	module_name = item.keys()[0]
	module = item[module_name]
	for plugin_name in module:
		source = imp.load_source('module.name', os.path.join(os.environ['MAJOR_PATH'], 'modules', module_name, plugin_name + '.py'))
		plugin = source.plugin(context, module[plugin_name])
		plugin['name'] = module_name + '/' + plugin_name
		context['plugins'] += [plugin]

print '>>> MAJOR'

for plugin in context['plugins']:
	print 'LOADED ' + plugin['name']

