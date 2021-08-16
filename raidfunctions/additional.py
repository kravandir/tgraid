import random
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import os


class Set:
    def __init__(self, tg_accounts):
        self.tg_accounts = tg_accounts

    def bio(self, bio_text):
        for tg_acc in self.tg_accounts:
            try:
                with TelegramClient("tgaccs/" + tg_acc, 1320038, '6285bb6537008dfd4614a5612e8d0969') as client:
                    client.connect()
                    client(UpdateProfileRequest(about=bio_text))
                print(f'The bio has been updated on {tg_acc}')
            except Exception as e:
                print(f'Error:\n{e}')

    def avatar(self):
        for tg_acc in self.tg_accounts:
            try:
                with TelegramClient("tgaccs/" + tg_acc, 1320038, '6285bb6537008dfd4614a5612e8d0969') as client:
                    client.connect()
                    r_file = 'avatars/'+random.choice(os.listdir('avatars/'))
                    upl = client.upload_file(r_file)
                    client(UploadProfilePhotoRequest(upl))
                    print(f'The avatar has been updated on {tg_acc}')
            except Exception as e:
                print(f'Error:\n{e}')
