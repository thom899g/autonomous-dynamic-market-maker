import logging
from datetime import datetime

class Monitor:
    def __init__(self):
        logging.basicConfig(filename='admm_monitor.log', level=logging.INFO)
        self.start_time = None

    def start_tracking(self):
        """Starts the monitoring process."""
        self.start_time = datetime