from ds_mailer.Sender import run_sender
from ds_mailer.tests.test_gamelist import TEST_GAMES


if __name__ == "__main__":
    run_sender(TEST_GAMES)
