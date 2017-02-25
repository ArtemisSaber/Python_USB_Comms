import configparser
CONFIG = 'config.txt'
config = configparser.ConfigParser()
config.read(CONFIG)

radius = input(config.get('messages', 'question')+' ')
print(config.get('messages', 'result_header')+' '+str(config.getfloat('numbers', 'pi')*float(radius)**2))
