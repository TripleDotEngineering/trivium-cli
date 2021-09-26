"""

Copyright 2021 Triple Dot Engineering LLC

"""

from abc import ABC, abstractmethod

class Command(ABC):
    """The Command abstract class"""

    @abstractmethod
    def __run__(self, args):
        """All Commands will implement this run method"""
        raise Exception('Run command not defined.')
