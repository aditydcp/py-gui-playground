import dotenv
import subprocess

# TODO: Implement GUI

config = dotenv.dotenv_values(".env")

# TODO: Change to GUI Input
env1 = config.get('ENV_01_NAME')
env2 = config.get('ENV_02_NAME')

subprocess.run('conda run -n ' + env1 + ' python script.py', shell=True)
subprocess.run('conda run -n ' + env2 + ' python script.py', shell=True)