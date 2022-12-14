import os
import sys
import time
import pyautogui as pg
import numpy as np
from bs4_code import req_url
from config import chat


# noinspection PyGlobalUndefined
def set_driver_by(d, B):
    global driver
    global By
    driver, By = d, B


def click(click_c=1):
    for i in range(click_c):
        pg.click(389, 777, button='middle')


def split_text_date(td, r):
    try:
        ti = td.index(':')
        date = td[ti - 2:ti + 3]
        text = td[:ti - 2]
        text = text.replace('Пересланное сообщение', '')
        text = text.replace('Данное сообщение удалено', '')
        if text:
            r.write(date + '-' + text + '\n')
    except:
        pass


def taking_sorted_messages(saved_number=0):
    try:
        a = time.time()
        messages = np.array(driver.find_element(
            By.XPATH, '//div[@class="{}"]'.format(chat)). \
                            find_elements(By.XPATH, '//div[@data-id]'))
        sm, smt = np.array([]), np.array([])
        r = open('stuf/sorted_messages_list.txt', 'w', encoding='utf8')
        if saved_number:
            for mes in messages:
                text_date = str(''.join(''.join(mes.text.splitlines())))
                # get_attribute class
                mes_html = mes.get_attribute('innerHTML')
                # mes_html = mes.get_attribute('class')
                if '_3mSPV' not in mes_html:
                    if '_25eIs' not in mes_html:
                        # set message selenium into sm, text into smt
                        sm = np.append(sm, mes)
                        smt = np.append(smt, text_date)
                        if '**' in text_date:
                            text_date = text_date.split('**')[1]
                        if len(text_date.split(':')[0]) > 2:
                            split_text_date(text_date, r)
                else:
                    split_text_date(text_date, r)
            if 'Сообщения защищены сквозным шифрованием.' in sm[0].text:
                sm = np.delete(sm, 0)
                smt = np.delete(smt, 0)
            print('-------------------------------\ntime for tsm: ', time.time() - a,
                  '\n-----------------------------------')
            return sm, smt
        else:
            for mes in messages:
                text_date = str(''.join(''.join(mes.text.splitlines())))
                smt = np.append(smt, text_date)
            return messages, smt
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


def select(xpath, class_name, text='NULL', clicked=0):
    selected_element = driver.find_element(By.XPATH, xpath.format(class_name))
    if clicked == 1:
        selected_element.click()
    time.sleep(0.1)


def write_to_file(message_list):
    r = open('stuf/all_messages.txt', 'w', encoding='utf8')
    for i in range(len(message_list)):
        r.write(message_list[i])
        if i + 1 != len(message_list):
            r.write('\n')
    r.close()


def message_count(flag, saved_number):
    mes_cunt, message_div_sum, message_div_sum2 = 0, 99, 100
    result_repeated = 0
    while result_repeated < 7:
        pg.press('home')
        time.sleep(0.5)
        if mes_cunt % 5 == 0:
            pg.scroll(7)
            pg.scroll(-2)
            message_div_sum2, message_div_sum = message_div_sum, req_url(driver.page_source, flag=flag,
                                                                         saved_number=saved_number)
            print(' - ', message_div_sum)
        else:
            print(".", end='')
        if message_div_sum == message_div_sum2:
            result_repeated += 1
        else:
            result_repeated = 0
        mes_cunt += 1

    write_to_file(req_url(driver.page_source, key=1, flag=flag, saved_number=saved_number))
    return message_div_sum


def sorted_text_list():
    r = open('stuf/all_messages.txt', 'r', encoding='utf8')
    txt_list = []
    for i in r:
        try:
            txt_list.append(str(''.join(i.splitlines())))
        except:
            print('exc136: ', str(''.join(i.splitlines())))
    if 'Сообщения защищены сквозным шифрованием.' in txt_list[0]:
        txt_list.remove(txt_list[0])
    return txt_list
