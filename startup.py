class Startup:

    def __init__(self, name, loc, desc, acc, tags=None, batch=None):
        self.name = name
        self.description = desc
        self.location = loc
        self.accelerator = acc
        self.tags = tags
        self.batch = batch

    def __repr__(self) -> str:
        text = "{} {} is located in {} and its tags are {}".format(self.batch ,self.name, self.location, self.tags)
        return text
