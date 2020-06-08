# Logging configuration using python

A startup configuration for setting logging for the python project

The configuration file `log.conf` can be updated as per the requirement

`consoleHandler` will handle printing log information to `stdout` console

`fileHandler` will handle writing of log file to dedicated log file.

The log file name and location can be set from either the configurtion file or from the main python file. In the example, the `args` for fileHandler which should take the log file path and name is injected from the main python file based on the directory from where it's run.

So, essentially the value `logfilename` in the `args=('%(logfilename)s',)` is taken from the python file using the below specification.

```python
path = os.path.dirname(os.path.realpath(__file__)) + '/logs/out.log'
logging.config.fileConfig(fname='conf/log.conf',
                          defaults={'logfilename': path},
                          disable_existing_loggers=False)
```
