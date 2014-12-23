# from automa.api import *
import json 
import pprint
from os import listdir
from os.path import isfile, join

# Load the commands YAML
def load_commands():
  path = "./app_commands/"
  app_commands = {}
  app_command_files = [ f for f in listdir(path) if isfile(join(path, f)) ]
  for app_command_file in app_command_files:
    file_handle = open(join(path, app_command_file))
    app_commands[app_command_file[:app_command_file.index('.')]] = json.load(join(file_handle))
  return(app_commands)

# Start up the apps
def start_apps(app_commands):
  for app_name in app_commands:
    print "Starting " + app_name
 
def handle_command(message, app_commands):
  print(message)
  print "Handling app " + message["App"] + " command " + message["Command"]
  steps = app_commands[message["App"]][message["Command"]]
  for step in steps:
    handle_step(message, step)

def handle_step(message, step):
  print step[step.keys()[0]]
  # Time to implement some of these! http://www.getautoma.com/docs
