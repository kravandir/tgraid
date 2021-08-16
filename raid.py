import os
from sys import platform
from raidfunctions import register, tgraid, additional
menu = \
    'Выход в главное меню [ENTER]'\
    '\nВыберите функцию:\n\n'\
    '0.Зарегистрировать аккаунты\n'\
    '1.Запустить спам\n'\
    '2.Зайти в беседу\n'\
    '3.Рейд в лс\n'\
    '4.Дополнительно\n'

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
        bs = input('Введите ссылку на беседу:\n')
        f = int(input('Спамить:\n1.Быстро\n2.Медленно\n'))
        chat = tgraid.ConfJoin(tg_accounts, bs, f).join()
        q = False
    answ = tgraid.PrepareRaid().questions(qtype=q)
    if answ[2] == 1:
        msg_type = int(input('1.Спамить фразами из args.txt\n2.Спамить повторными фразами из message.txt\n\n'))
        for i in tg_accounts:
            print("Спам с {0} акка запущен!".format(i))
            ms_type = tgraid.PrepareRaid().msgs_type(msg_tp=msg_type)
            tgraid.TgBot(i, answ[2], '', ms_type, answ[0], msg_type, answ[1], chat).start()
    if answ[2] == 2:
        print('Будет спамить файлами, которые лежат в raidfiles')
        fl = os.listdir('raidfiles')
        for i in tg_accounts:
            print("Спам с {0} акка запущен!".format(i))
            tgraid.TgBot(i, answ[2], fl, [], answ[0], 0, answ[1], chat).start()
    print(f'Боты активированы!\nОтправьте команду "{answ[0]}" для призыва ботов')


while True:
    try:
        a = int(input(menu))
        if a == 0:
            while True:
                print(
                    '1)Ввести аккаунт\n'
                    '2)Получить код для доступа через сессию\n'
                    '3)Проверить акк на валидность\n'
                    '4)Выйти из реги\n\n')
                b = int(input())
                if b == 1:
                    name = input('Напишите никнейм бота:\n')
                    register.Register().regaccountreg(name)
                elif b == 2:
                    print(
                        'Введите никнейм бота или перетащите файл сессии\n')
                    name = input()
                    register.Register().checkcode(name)
                elif b == 3:
                    accounts = os.listdir('tgaccs')
                    for x in accounts:
                        try:
                            res = register.Register().checkvalidation(x)
                            if not res:
                                print("Удалите файл {0}. Он нерабочий".format(x))
                        except:
                            pass
                elif b == 4:
                    break
        elif a == 1:
            start_spam(False)
        elif a == 2:
            start_spam(True)
        elif a == 3:
            idtg = input("Введи айди телеграм\n")
            spam_type = int(input("1.Спам текстом\n2.Спам файлами\n"))
            if spam_type == 1:
                msg_tp = int(input("1.Спам из args.txt\n2.Спам из message.txt\n\n"))
                msg = tgraid.PrepareRaid().msgs_type(msg_tp)
            else:
                msg_tp = 0
                msg = os.listdir('raidfiles')
            accs = os.listdir('tgaccs')
            for acc in accs:
                print("Спам с {0} акка запущен!".format(acc))
                tgraid.LsRaid(idtg, acc, msg_tp, msg, spam_type).start()
        elif a == 4:
            tg_accs = os.listdir('tgaccs')
            set_tg = additional.Set(tg_accs)
            while True:
                print('1.Установить BIO аккаунтам\n'
                      '2.Установить аватарки аккаунтам\n')
                try:
                    a = int(input())
                    if a == 1:
                        bio_text = input("Введите текст для bio: ")
                        set_tg.bio(bio_text)
                    if a == 2:
                        set_tg.avatar()
                except:
                    break
    except:
        break
