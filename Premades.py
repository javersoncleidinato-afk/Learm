class Premades:
    def __init__(self):
        import time
        self.time = time

    def print(self, msg, amount=1):
        for i in range(amount):
            __builtins__.print(msg)

    def wait(self, amount=1):
        self.time.sleep(amount)