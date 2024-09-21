from datetime import datetime

class TTS:
    def __init__(self, time, url):
        self.time = time
        self.url = url

    def is_recernt(self):
        pc_time = datetime.now()
        logic = pc_time - self.time
        if logic <= 300:
            return True
        return False