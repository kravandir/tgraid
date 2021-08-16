from threading import Thread
import asyncio
from telethon.sync import TelegramClient, events
from telethon import functions
import random
import time


class PrepareRaid:
    @staticmethod
    def msgs_type(msg_tp):
        ms = ""
        if msg_tp == 1:
            a = open('args.txt', encoding='utf8')
            ms = a.read().split('\n')
            a.close()
        elif msg_tp == 2:
            a = open('message.txt', encoding='utf8')
            ms = a.read()
            a.close()
        return ms

    @staticmethod
    def questions(qtype):
        answlist = []
        if qtype:
            print('Type the word whitch will launch the bots:')
            answlist.append(input())
        else:
            answlist.append('')
        answlist.append(int(input('Spam mode:\n1.Fast\n2.Slow\n')))
        answlist.append(int(input('1.Spam via the text\n2.Spam via the files\n')))
        return answlist


class LsRaid(Thread):
    def __init__(self, idtg, cli, ms_tp, msgs, spam_type):
        Thread.__init__(self)
        self.idtg = idtg
        self.cli = cli
        self.ms_tp = ms_tp
        self.msgs = msgs
        self.spam_type = spam_type

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient("tgaccs/" + self.cli, 1320038, "6285bb6537008dfd4614a5612e8d0969")
        client.start()
        k = 1
        while True:
            try:
                if self.spam_type == 1:
                    if self.ms_tp == 1:
                        client(
                            functions.messages.SendMessageRequest(peer=self.idtg, message=random.choice(self.msgs)))
                    else:
                        client(functions.messages.SendMessageRequest(peer=self.idtg, message=self.msgs))
                else:
                    client.send_file(self.idtg, "raidfiles/" + random.choice(self.msgs))
                print(f"[LS RAID] Sent {k} times!")
            except Exception as e:
                print(f"[LS RAID] Error:\n{e}")
            k += 1
            time.sleep(0.5)
        client.run_until_disconnected()


class TgBot(Thread):
    def __init__(self, cli, spam_type, file_link, msgs, startmsg, msg_tp, f, chat):
        Thread.__init__(self)
        self.cli = cli
        self.spam_type = spam_type
        self.file_link = file_link
        self.msgs = msgs
        self.startmsg = startmsg
        self.msg_tp = msg_tp
        self.f = f
        self.chat = chat

    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            if self.chat == 0:
                client = TelegramClient("tgaccs/" + self.cli, 1320038, "6285bb6537008dfd4614a5612e8d0969")
                client.connect()

                @client.on(events.NewMessage)
                async def my_event_handler(event):
                    if event.text == self.startmsg:
                        k = 1
                        while True:
                            try:
                                if self.spam_type == 1:
                                    if self.msg_tp == 1:
                                        await client(functions.messages.SendMessageRequest(peer=event.chat_id, message=random.choice(self.msgs)))
                                    else:
                                        await client(functions.messages.SendMessageRequest(peer=event.chat_id, message=self.msgs))
                                else:
                                    await client.send_file(event.chat_id, "raidfiles/" + random.choice(self.file_link))
                                if self.f == 2:
                                    time.sleep(random.randint(1, 3))
                                else:
                                    time.sleep(0.5)
                                print(f"[GROUP RAID] Sent {k} times!")
                            except:
                                print(f"[GROUP RAID] Error!")
                            k += 1
                client.start()
                client.run_until_disconnected()
            client = TelegramClient("tgaccs/" + self.cli, 1320038, "6285bb6537008dfd4614a5612e8d0969")
            client.connect()
            i = 1
            while True:
                try:
                    if self.spam_type == 1:
                        if self.msg_tp == 1:
                            client(functions.messages.SendMessageRequest(peer=self.chat, message=random.choice(self.msgs)))
                        else:
                            client(functions.messages.SendMessageRequest(peer=self.chat, message=self.msgs))
                    else:
                        client.send_file(self.chat, "raidfiles/" + random.choice(self.file_link))
                    if self.f == 2:
                        time.sleep(random.randint(1, 3))
                    else:
                        time.sleep(0.5)
                    print(f"[GROUP RAID] Sent {i} times!")
                except Exception as e:
                    print(f"[GROUP RAID] Error:\n{e}")
                i += 1
            client.start()
            client.run_until_disconnected()
        except Exception as e:
            print(f"Error:\n{e}")


class ConfJoin:
    def __init__(self, accs1, bs, f):
        self.accs1 = accs1
        self.bs = bs
        self.f = f

    def join(self):
        idtg = 0
        for x in range(len(self.accs1)):
            try:
                with TelegramClient("tgaccs/" + self.accs1[x], 1236408, '1a96dab32bad4e7cb7d2e28887d59f1f') as client:
                    client.connect()
                    if self.bs[:1] == '@':
                        a = client.get_entity(self.bs[1:])
                        client(functions.channels.JoinChannelRequest(a.id))
                        idtg = (1000000000000 + a.id) * -1
                    try:
                        if self.bs[:13] == 'https://t.me/':
                            a = client.get_entity(self.bs[13:])
                            client(functions.channels.JoinChannelRequest(a.id))
                            idtg = (1000000000000 + a.id) * -1
                    except:
                        pass
                    if self.bs[13:22] == 'joinchat/':
                        a = client(functions.messages.ImportChatInviteRequest(hash=self.bs[22:]))
                        idtg = -1 * a.updates[1].participants.chat_id
                print("{0} joined the chat!".format(
                    self.accs1[x][:self.accs1[x].find(".")]))
                del client
            except Exception as e:
                print(f"{self.accs1[x]} Error in joining the chat:\n{e}")
            if self.f == 2:
                time.sleep(random.randint(1, 3))
        return idtg
