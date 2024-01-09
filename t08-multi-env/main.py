import dotenv
import subprocess

config = dotenv.dotenv_values(".env")

env1 = config.get('ENV_01_NAME')
env2 = config.get('ENV_02_NAME')

# print(env1)
# print(env2)

subprocess.run('conda run -n ' + env1 + ' python script.py', shell=True)
subprocess.run('conda run -n ' + env2 + ' python script.py', shell=True)