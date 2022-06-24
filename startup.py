class Startup:

    def __init__(self, name, desc, loc, acc, tags=None, batch=None):
        self.name = name
        self.description = desc
        self.location = loc
        self.accelerator = acc
        self.tags = tags
        self.batch = batch

    def __repr__(self) -> str:
        text = "{} is located in {}".format(self.name, self.location)
