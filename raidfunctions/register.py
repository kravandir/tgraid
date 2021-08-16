from telethon.sync import TelegramClient
from telethon import functions
import datetime


class Register:
    @staticmethod
    def regaccountreg(name):
        try:
            with TelegramClient("tgaccs/" + name, 1236408, '1a96dab32bad4e7cb7d2e28887d59f1f') as client:
                client.connect()
            print('The account has been registered!')
        except Exception as e:
            print(f'Error:\n{e}')

    @staticmethod
    def checkcode(name):
        with TelegramClient("tgaccs/" + name, 1236408, '1a96dab32bad4e7cb7d2e28887d59f1f') as client:
            result = client(functions.messages.GetHistoryRequest(
                peer=777000,
                offset_id=99999999,
                offset_date=datetime.datetime(2018, 6, 27),
                add_offset=0,
                limit=100,
                max_id=0,
                min_id=0,
                hash=0
            ))
            print(result.messages[0].message)

    @staticmethod
    def checkvalidation(acc):
        print("Checking " + acc)
        try:
            with TelegramClient("tgaccs/" + acc, 1236408, '1a96dab32bad4e7cb7d2e28887d59f1f') as client:
                client.connect()
            print('Valid')
            return True
        except Exception as e:
            print(f'Invalid\n{e}')
            return False
