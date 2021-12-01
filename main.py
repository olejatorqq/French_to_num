from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import collections

numbers_0_6 = ['zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six']

numbers_0_1 = ['et']

numbers_7_9 = ['sept', 'huit', 'neuf']

numbers_10_16 = ['dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize']

numbers_20_60 = ['vingt', 'trente', 'quarante', 'cinquante', 'soixante']

numbers_100 = ['cent']


def old_Rus():
    ent_old_rus_num.delete(0, END)
    if len(ent_arab_num.get()) != 0:
        i = int(ent_arab_num.get())
        a = []
        while i > 0:
            if i >= 500:
                i -= 500
                a.append("Ф")
                continue
            if i >= 100:
                i -= 100
                a.append("Р")
                continue
            if i >= 30:
                i -= 30
                a.append("Л")
                continue
            if i >= 9:
                i -= 9
                a.append("Д")
                continue
            if i >= 8:
                i -= 8
                a.append("И")
                continue
            if i >= 2:
                i -= 2
                a.append("В")
                continue
            if i >= 1:
                i -= 1
                a.append("А")
                continue
        ent_old_rus_num.insert(0, "".join(a))


def clicked():
    ent_errors.delete(0, END)
    ent_old_rus_num.delete(0, END)
    ent_arab_num.delete(0, END)
    counter = []
    final = 0
    k = 0
    check = (ent_text_num.get()).split(" ")
    check = list(filter(None, check))
    check_len = len(check)
    for m in range(check_len):
        counter.append(check[m])
    ent_arab_num.delete(0)
    ErrorCheck = bool(False)
    ertq = 0

    for i in range(len(counter)):
        if counter[i] not in numbers_0_6 and counter[i] not in numbers_7_9 and counter[i] not in numbers_10_16 and \
                counter[i] not in numbers_20_60 and counter[i] not in numbers_100 and counter[i] not in numbers_0_1:
            ErrorCheck = True
            Error = "Встречено неизвестное слово {}".format(counter[i])
            break


        for j in range(len(numbers_0_6)):
            if counter[i] == numbers_0_6[j]:
                if counter[i] == "zero" and len(counter) > 1:
                    Error = "Zero1 не может использоваться вместе с другими символами"
                    ErrorCheck = True
                    break

                if i > 0:
                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                        Error = "Два2 числа {} и {} единичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                   counter[i])
                        ErrorCheck = True
                        break
                    if counter[i] == 'un' and counter[i - 1] in numbers_20_60:
                        if i > 1:
                            if counter[i] == 'un' and counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre':
                                print("da")
                        else:
                            Error = "un может использоваться только самостоятельно либо с разрядом сотней"
                            ErrorCheck = True
                            break
                    if i > 2:
                        if counter[i] == 'un' and counter[i - 1] == 'et' and counter[i - 2] == 'vingt' and counter[i - 3] == 'quatre':
                            Error = "et un может использоваться только числами 20-70"
                            ErrorCheck = True
                            break

                if len(counter) == 2:
                    if counter[i - 1] in numbers_0_1 and counter[i] == 'un':
                        Error = "Et un может использоваться только с числами 20-60"
                        ErrorCheck = True
                        break



                # if not ((i == 0 and counter[i] == 'un') or (i > 0 and counter[i - 1] in numbers_100)):
                #     if i > 1 and counter[i] == 'un' and counter[i - 1] in numbers_0_1 and counter[i - 2] in numbers_20_60:
                #         print('')
                #         k += 1
                #     if i > 1 and counter[i] == 'un' and counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre':
                #         print('Прикол')
                #     if not(i > 1 and counter[i] == 'un' and counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre'):
                #         print("Че")
                #         Error = "Un может использоваться либо самостоятельно либо с разрядом сотней"
                #         ErrorCheck = True
                #         break

                # if i == 0 and counter[i] == 'un':
                #     print('')
                # if i > 0:
                #     if  counter[i] == 'un' and counter[i - 1] not in numbers_100:
                #         print('')
                # else:
                #     Error = "Un может использоваться либо самостоятельно либо с разрядом сотней"
                #     ErrorCheck = True
                #     break
                # if i > 0:
                #     if counter[i] == 'un' and counter[i - 1] not in numbers_100):
                #         print('daa')

                for j in range(len(numbers_0_6)):
                    if counter[i] == numbers_0_6[j]:
                        final += j

        for j in range(len(numbers_7_9)):
            if counter[i] == numbers_7_9[j]:
                if counter[i] == "zero" and len(counter) > 1:
                    Error = "Zero не может использоваться вместе с другими символами"
                    ErrorCheck = True
                    break
                if i > 0:
                    if counter[i - 1] in numbers_7_9 or counter[i - 1] in numbers_0_6:
                        Error = "Два3 числа {} и {} единичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                   counter[i])
                        ErrorCheck = True
                        break

                for j in range(len(numbers_7_9)):
                    if counter[i] == numbers_7_9[j]:
                        final += 7 + j

        for j in range(len(numbers_10_16)):
            if counter[i] == numbers_10_16[j]:
                if i > 0:
                    if counter[i - 1] in numbers_10_16:
                        Error = "Два4 слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                    counter[i])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_20_60:
                        if counter[i - 1] == 'soixante' and counter[i] in numbers_10_16:
                            print("")
                        elif counter[0] == 'quatre' and len(counter) > 2:
                            if counter[i - 1] == 'vingt':
                                print("")
                        else:
                            Error = "Два5 слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                        counter[i])
                            ErrorCheck = True
                            break
                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                        Error = "Слово6 {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                            counter[i - 1], counter[i])
                        ErrorCheck = True
                        break

                if len(counter) > 2 and counter[i] == 'dix':
                    if counter[i - 1] == 'soixante' and (
                            counter[i + 1] in numbers_0_6 or counter[i + 1] in numbers_7_9):
                        Error = "После7 {} десятичного разряда должно стоять число 11-19".format(counter[i - 1])
                        ErrorCheck = True
                        break
                if len(counter) > 3 and counter[i] == 'dix' and counter[0] == 'quatre':
                    if counter[i - 1] == 'vingt' and (counter[i + 1] in numbers_0_6 or counter[i + 1] in numbers_7_9):
                        Error = "После8 {} десятичного разряда должно стоять число 11-19".format(counter[i - 1])
                        ErrorCheck = True
                        break
                for j in range(len(numbers_10_16)):
                    if counter[i] == numbers_10_16[j]:
                        final += 10 + j

        for j in range(len(numbers_20_60)):
            if counter[i] == numbers_20_60[j]:
                if i > 0:
                    if counter[i - 1] in numbers_20_60:
                        Error = "Два9 слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                    counter[i])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_10_16:
                        Error = "Два10 слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                     counter[i])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_0_6 or numbers_7_9:
                        if counter[i - 1] == 'quatre' and counter[i] == 'vingt':
                            final += 56
                        else:
                            Error = "Слово11 {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                                counter[i - 1], counter[i])
                            ErrorCheck = True
                            break

                for j in range(len(numbers_20_60)):
                    if counter[i] == numbers_20_60[j]:
                        final += (j + 2) * 10

        for j in range(len(numbers_100)):
            if counter[i] == numbers_100[j]:
                if i > 0:
                    if counter[i - 1] in numbers_10_16 or counter[i - 1] in numbers_20_60:
                        Error = "Слово12 {} десятичного разряда стоит перед словом {} разряда сотней".format(
                            counter[i - 1], counter[i])
                        ErrorCheck = True
                        break
                if i > 1:
                    if counter[0] in numbers_10_16 or counter[0] in numbers_20_60:
                        Error = "Слово13 {} десятичного разряда не может стоять раньше слова {} разряда сотней".format(
                            counter[0], counter[i])
                        ErrorCheck = True
                        break

                if counter[0] in numbers_0_6 and counter[1] in numbers_100:
                    for j in range(len(numbers_0_6)):
                        if counter[0] == numbers_0_6[j]:
                            final += j * 100 - j
                elif counter[0] in numbers_7_9 and counter[1] in numbers_100:
                    for j in range(len(numbers_7_9)):
                        if counter[0] == numbers_7_9[j]:
                            final += (j + 7) * 100 - (j + 7)
                if counter[0] in numbers_100:
                    final += 100

    if ErrorCheck:
        ent_old_rus_num.delete(0)
        ent_arab_num.delete(0)
        ent_errors.insert(0, Error)
    if not ErrorCheck:
        ent_arab_num.insert(0, final)
        old_Rus()


# except Exception as err:
#    ent_errors.insert(0, "Проверьте корректность ввода, возможно вы пропустили - ")


window = Tk()

about = []
resultat = []
window.geometry("2048x650")

window.title("ConvertToNumFrench")

frm_form = Frame(relief=SUNKEN, borderwidth=3)
frm_form.pack()

text_num = Label(master=frm_form, text="Текстовое представление числа", font=('Times New Roman', 50))
ent_text_num = Entry(master=frm_form, width=95, font=('Times New Roman', 40))
text_num.grid(row=0, column=0, sticky='nwes')
ent_text_num.grid(row=1, column=0, sticky='nwes')

arab_num = Label(master=frm_form, text="Числовое представление (Арабские цифры)", font=('Times New Roman', 50))
ent_arab_num = Entry(master=frm_form, width=95, font=('Times New Roman', 40))
arab_num.grid(row=2, column=0, sticky='nwes')
ent_arab_num.grid(row=3, column=0, sticky='nwes')

old_rus_num = Label(master=frm_form, text="Числовое представление (Страрорусские цифры)", font=('Times New Roman', 50))
ent_old_rus_num = Entry(master=frm_form, width=95, font=('Times New Roman', 40))
old_rus_num.grid(row=4, column=0, sticky='nwes')
ent_old_rus_num.grid(row=5, column=0, sticky='nwes')

errors = Label(master=frm_form, text="Ошибки", font=('Times New Roman', 50))
ent_errors = Entry(master=frm_form, width=95, font=('Times New Roman', 35))
errors.grid(row=6, column=0, sticky='nwes')
ent_errors.grid(row=7, column=0, sticky='nwes')

btn = Button(master=frm_form, text="Convert", command=clicked, width=10)
btn.grid(row=8, column=0)

window.mainloop()
