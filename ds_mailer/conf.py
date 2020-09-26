import os

"""
Secret key
ds_mailer.app
"""
key = os.environ['script_key']

"""
Database url
ds_mailer.gamelist
"""
DATABASE_URL = os.environ['DATABASE_URL']

"""
Timezone
ds_mailer.Sender
"""
TIMEZONE = 'Europe/Moscow'

"""
Constants for retries
ds_mailer.Sitescanner
"""
NUMBER_OF_RETRIES = 5
DELAY_BETWEEN_TRIES = 5
