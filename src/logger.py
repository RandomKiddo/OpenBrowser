import time
class Logger:
    def __init__(self, name: str = 'Logger'):
        self.items = []
        self.name = name
        self.items.append(f'Logger \"{self.name}\" initialized at {time.time()}\n')
        self.items.append('=> LOGGING ACTIVE\n')
        self.start_time = time.time()

    def log(self, val: str) -> None:
        self.items.append(f'{time.time()} | {val}')

    def close(self):
        with open(f'loading_logs/SESSION_{self.start_time}.log', 'w') as f:
            f.writelines(self.items)
        f.close()
        self.items = []