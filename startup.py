from time import sleep
from turtle import st


class Startup:

    def __init__(self, name, loc, desc, acc, tags=None, batch=None, status=None, wp=None):
        self.name = name
        self.description = desc
        self.location = loc
        self.accelerator = acc
        self.tags = tags
        self.batch = batch
        self.status = status
        self.webpage = wp

    def __repr__(self) -> str:
        # text = "{} {} is located in {} and its tags are {}".format(self.batch ,self.name, self.location, self.tags)
        text = '{} {} {} {} {} {}'.format(self.batch, self.name, self.location, self.description, self.accelerator, self.status)
        return text
