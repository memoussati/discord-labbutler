from abc import ABC, abstractmethod
from enum import Enum


class Command(ABC):
    @abstractmethod
    async def run(self, ctx, args):
        pass


class CommandException(Exception):
    pass


class CommandMessage(object):
    def __init__(self, content=None, embed=None):
        self._content = content
        self._embed = embed

    @property
    def content(self):
        return self._content

    @property
    def embed(self):
        return self._embed
