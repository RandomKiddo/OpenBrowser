import time
import datetime

class Logger:
    def __init__(self, name: str = 'Logger'):
        self.items = []
        self.name = name
        self.items.append(f'Logger \"{self.name}\" initialized at {time.time()}\n')
        self.items.append('=> LOGGING ACTIVE\n')
        self.start_time = datetime.datetime.now()

    def log(self, val: str) -> None:
        self.items.append(f'{datetime.datetime.utcnow()} (UTC) | {val}')

    def close(self):
        with open(f'loading_logs/SESSION_{self.start_time}.log', 'w') as f:
            for _ in self.items:
                f.write(_)
        f.close()
        self.items = []