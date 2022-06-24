class Startup:

    def __init__(self, name, desc, loc, acc):
        self.name = name
        self.description = desc
        self.location = loc
        self.accelerator = acc

    def __repr__(self) -> str:
        text = "{} is located in {}".format(self.name, self.location)
