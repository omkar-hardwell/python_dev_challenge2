Python dev challenge #2
=====================================

## Getting Started

This is the Django framework based application to monitor remote host via SSH connection.

### Installation

The installation is very straightforward, but make sure you are using at least
python 3.6.x

Make sure pip installed with python package.

To install dependencies.
```bash
$ pip install -r requirements.txt
```

### Running

When all dependencies have been installed, you can run the application
on your local instance by running:

```bash
$ cd python_dev_challenge2
$ python pc_analytics/manage.py runserver
```

You will have to access this application just by entering following url on browser.
```
URL: http://127.0.0.1:8000/analytics or http://localhost:8000/analytics
```

### Testing

Note: Test cases are pending for this application.

### Updating

To install new dependencies; Add it to requirements.txt then run,

```bash
(env) $ pip install -r requirements.txt
```

### References

1) https://www.djangoproject.com/
2) https://github.com/zix99/sshsysmon
3) https://pypi.python.org/pypi/paramiko/2.0.2
4) https://pypi.python.org/pypi/psutil
5) https://github.com/giampaolo/psutil/issues/336
