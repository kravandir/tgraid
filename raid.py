import os
from sys import platform
from raidfunctions import register, tgraid, additional
menu = \
    'Return to main menu [ENTER]'\
    '\nChange function:\n\n'\
    '0.Register accounts\n'\
    '1.Lauch spam attack to chat\n'\
    '2.Join a chat\n'\
    '3.Launch spam attack to user\n'\
    '4.More\n'

if platform in ('linux', 'linux2'):
    os.system('rm tgaccs/*.session-journal')
elif platform == 'win32':
    os.system('cd tgaccs & del *.session-journal')


def start_spam(raidconn):
    tg_accounts = os.listdir('tgaccs')
    if not raidconn:
        q = True
        chat = 0
    else:
        bs = input('Type chat link:\n')
        f = int(input('Spam speed:\n1.Fast\n2.Slow\n'))
        chat = tgraid.ConfJoin(tg_accounts, bs, f).join()
        q = False
    answ = tgraid.PrepareRaid().questions(qtype=q)
    if answ[2] == 1:
        msg_type = int(input('1.Spamming with random words from args.txt\n2.Spamming with repeating text from message.txt\n\n'))
        for i in tg_accounts:
            print("Spam has been launched from the {0} account!".format(i))
            ms_type = tgraid.PrepareRaid().msgs_type(msg_tp=msg_type)
            tgraid.TgBot(i, answ[2], '', ms_type, answ[0], msg_type, answ[1], chat).start()
    if answ[2] == 2:
        print('It will be spamming using files from raidfiles')
        fl = os.listdir('raidfiles')
        for i in tg_accounts:
            print("Spam has been launched from the {0} account!".format(i))
            tgraid.TgBot(i, answ[2], fl, [], answ[0], 0, answ[1], chat).start()
    print(f'Bots has been activated!\nSend the command "{answ[0]}" for launching them!')


while True:
    try:
        a = int(input(menu))
        if a == 0:
            while True:
                print(
                    '1)Enter an account\n'
                    '2)Find a code for access in telegram app using a session file\n'
                    "3)Check accounts' validation\n"
                    '4)Exit from registration\n\n')
                b = int(input())
                if b == 1:
                    name = input("Type bot's phone:\n")
                    register.Register().regaccountreg(name)
                elif b == 2:
                    print("Type bot's phone\n")
                    name = input()
                    register.Register().checkcode(name)
                elif b == 3:
                    accounts = os.listdir('tgaccs')
                    for x in accounts:
                        try:
                            res = register.Register().checkvalidation(x)
                            if not res:
                                print("Invalid account {0}".format(x))
                        except:
                            pass
                elif b == 4:
                    break
        elif a == 1:
            start_spam(False)
        elif a == 2:
            start_spam(True)
        elif a == 3:
            idtg = input("Enter person's username\n")
            spam_type = int(input("1.Spam via the text\n2.Spam via the files\n"))
            if spam_type == 1:
                msg_tp = int(input("1.Spam via random worlds from args.txt\n2.Spam via repeating word from message.txt\n\n"))
                msg = tgraid.PrepareRaid().msgs_type(msg_tp)
            else:
                msg_tp = 0
                msg = os.listdir('raidfiles')
            accs = os.listdir('tgaccs')
            for acc in accs:
                print("Spam has been launched from the {0} account!".format(acc))
                tgraid.LsRaid(idtg, acc, msg_tp, msg, spam_type).start()
        elif a == 4:
            tg_accs = os.listdir('tgaccs')
            set_tg = additional.Set(tg_accs)
            while True:
                print('1.Change BIO to accounts\n'
                      '2.Set avatars to accounts\n')
                try:
                    a = int(input())
                    if a == 1:
                        bio_text = input("Type the text from your bio: ")
                        set_tg.bio(bio_text)
                    if a == 2:
                        set_tg.avatar()
                except:
                    break
    except:
        break
