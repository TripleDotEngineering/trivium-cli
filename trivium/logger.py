"""

Copyright 2021 Triple Dot Engineering LLC

"""


from datetime import datetime
from .util import Colors


def get_logger():
    """Gets the logger"""
    return TriviumLogger.get_logger()


class TriviumLogger:
    """
    The TriviumLogger class is used to provide a common logging capability across
    the Trivium CLI. It provides basic formatting, timestamps, color, and support
    for configured log level.
    """

    # The class is a Singleton - this is the reference to the instance.
    _instance = None


    def __init__(self):
        """
        Init raises an exception to force the caller to use the Singleton getter.
        """
        raise Exception('call TriviumLogger.get_logger() instead.')


    @classmethod
    def get_logger(cls, level='info'):
        """
        This is the singleton getter. If the instance is not yet definied, it
        will initialize it. The instance is returned.
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__initsingleton__(level)
        return cls._instance


    def __initsingleton__(self, level='warn'):
        # pylint: disable=attribute-defined-outside-init
        """
        Initializes the class. This is effectively the constructor for the
        Singleton.
        """
        self.level = level
        self.color_map = {
            'ERROR': Colors.RED,
            'WARN': Colors.YELLOW,
            'INFO': Colors.CYAN,
            'VERBOSE': Colors.BLUE,
            'DEBUG': Colors.GREEN
        }

    def get_levels(self):
         # pylint: disable=no-self-use
        """Returns the available levels"""
        return ['error', 'warn', 'info', 'verbose', 'debug']


    def set_level(self, level):
        # pylint: disable=attribute-defined-outside-init
        """sets the log level"""
        if level.lower() in ['error', 'warn', 'info', 'verbose', 'debug']:
            self.level = level.lower()


    def _log(self, s, level='INFO'):
        """
        The function that actually performs the log operation. It is not
        intended what be called directly.
        """
        now = datetime.now()
        now = str(now).split(' ')[1]
        now = now[:-3]
        ts = f'{Colors.GRAY}{now}{Colors.ENDC}'
        lvl_color = self.color_map[level]
        lvl = f'{lvl_color}{level}{Colors.ENDC}'
        print(f'{ts} [ {lvl} ] {s}')


    def error(self, s):
        """
        If the log level is error or higher, logs an error message.
        """
        if self.level in ['error', 'warn', 'info', 'verbose', 'debug']:
            self._log(s, level='ERROR')


    def warn(self, s):
        """
        If the log level is warn or higher, logs an warning message.
        """
        if self.level in ['warn', 'info', 'verbose', 'debug']:
            self._log(s, level='WARN')


    def info(self, s):
        """
        If the log level is info or higher, logs an info message.
        """
        if self.level in ['info', 'verbose', 'debug']:
            self._log(s, level='INFO')


    def verbose(self, s):
        """
        If the log level is verbose or higher, logs an verbose message.
        """
        if self.level in ['verbose', 'debug']:
            self._log(s, level='VERBOSE')


    def debug(self, s):
        """
        If the log level is debug or higher, logs an debug message.
        """
        if self.level in ['debug']:
            self._log(s, level='DEBUG')
