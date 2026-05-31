class Premades:
    def __init__(self):
        import time, urllib.parse
        self.time = time
        self.urllib = urllib.parse

    def print(self, msg, amount=1):
        for i in range(amount):
            __builtins__.print(msg)

    def wait(self, amount=1):
        self.time.sleep(amount)

    def quote(self, msg):
        return self.urllib.quote(msg)

    def quote_plus(self, msg):
        return self.urllib.quote_plus(msg)