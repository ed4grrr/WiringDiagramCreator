from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL, basicConfig


class Logger:
    def __init__(self, name, level=DEBUG):
        self.logger = getLogger(name)
        self.logger.setLevel(level)
        self.formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler = StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        basicConfig(filename=f"{name}.log", level=level)

    def addMessage(self, message,
                   level=DEBUG):
        self.logger.log(level, "\n"+message+"\n")