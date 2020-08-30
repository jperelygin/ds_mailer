import time
from datetime import timedelta

import ds_mailer.Sender as Sender
from ds_mailer.gamelist import GAMES


if __name__ == "__main__":
    Sender.run_sender(GAMES)
    time.sleep(10800)
