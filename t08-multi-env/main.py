import subprocess
env1 = 'venv1'
env2 = 'venv2'
subprocess.run('conda run -n ' + env1 + ' python script.py', shell=True)
subprocess.run('conda run -n ' + env2 + ' python script.py', shell=True)