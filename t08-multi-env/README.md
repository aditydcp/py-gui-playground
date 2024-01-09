# Multi Env Runner

This is an example app that will run 2 different virtual environment on Conda.

For this app to run, make sure you have **Anaconda** or **Miniconda** installed on your system and added to your environment path.

To try this example, ideally you should have 2 different virtual environment installed with different version of Python.
For example, I have virtual enviroment named `venv1` with **Python 3.9**
 and another virtual environment named `venv2` with **Python 3.10**.
*You should change the variable value `env1` and `env2` to match your virtual enviroments name*.
When you run `main.py`, you can expect to see something like this.
```
PS C:\Github\py-gui-playground\t08-multi-env> python main.py
3.9.18 (main, Sep 11 2023, 14:09:26) [MSC v.1916 64 bit (AMD64)]

3.10.13 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:24:38) [MSC v.1916 64 bit (AMD64)]
```

This app has been tested on Windows 11.