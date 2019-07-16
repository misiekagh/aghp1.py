# -*- coding: utf-8 -*-
import os, sys, time
import remi.gui as gui
from remi import start, App
from threading import Timer
import uiuser, uiadmin, uitest
import ssl


class User(gui.Widget):
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.clientID = ''
        self.clientIP = ''
        self.clientTS = ''
        self.cRun = 0

    def api_login(self, ident):
        cookie = '../redir_cache/%s' % ident
        with open(cookie, 'r') as fil:
            self.clientTS, self.clientID, self.clientIP = fil.read().split(':')
        os.remove(cookie)
        headers = {'Content-type': 'text/plain', 'Refresh': '0;url=https://app.aixm.kpgeo.pl'}
        return ['Requested user {} logging in.'.format(self.clientID), headers]


class MyApp(App):
    usrdiff = {'None': 'none'}

    def __init__(self, *args):
        super(MyApp, self).__init__(*args, static_file_path={'res': './res/'})
        # super(MyApp, self).__init__(*args)

    # ----- Tu interfejs usera ---------------
    def build_ui(self, user):
        ui = self.root
        ui.empty()  # usun wszystko z interfejsu
        a = uiuser.UserUI(self)
        ui.append(a.setupUI(user, self.root.clientIP, self.root.clientTS))

    # ----- Tu interfejs test ---------------
    def build_test_ui(self, user):
        ui = self.root
        ui.empty()  # usun wszystko z interfejsu
        a = uitest.TestUI(self)
        ui.append(a.setupUI(user, self.root.clientIP, self.root.clientTS))

    # ------- Interfejs admina ---------------
    def build_admin_ui(self, user):
        global cList
        ui = self.root
        ui.empty()  # usun wszystko z interfejsu
        # for usr in cList.keys():
        #    ui.append(gui.Label('User: {}'.format(usr),width=600,height=20, style = styl_1))
        a = uiadmin.AdminUI(self)
        ui.append(a.setupUI(cList))

    # ------------ Koniec interfejsow
    def dict_check(self, met, pst, nst, exclude=[]):
        result = []
        for k in nst.keys():
            if k not in pst.keys():
                result.append('{} ADDED Key: {} |Value|: {}'.format(met, k, nst[k]))
            elif k not in exclude and nst[k] != pst[k]:
                result.append('{} CHANGED Key: {} |Value|: {} --> {}'.format(met, k, pst[k], nst[k]))
        return result

    def dump_appstate(self, met='None', nst={'None': 'none'}):
        r = self.dict_check(met, self.prevstate, nst, ['prevstate'])
        self.prevstate = nst
        return r

    def idle(self):
        global cList
        if uiuser.clientID != '': self.root.clientID = uiuser.clientID

        try:
            self.tstHang += 1
        except:
            self.tstHang = 1

        try:
            cid = self.root.clientID
        except:
            pass
        else:
            if cid == '' and not self.root.children and self.websockets:
                print('--- Idle -- Brak klienta - przekierowuj na logowanie. {}'.format(self.websockets))
                self.root.append(gui.Link(url='https://aixm.kpgeo.pl/login', text='Zaloguj się', open_new_window=False))
                self.execute_javascript('window.location.replace("https://aixm.kpgeo.pl/login");')


            elif cid != '' and cid not in cList.keys():
                cList[cid] = self.__dict__.copy()  # dodaj klienta do słownika i przypisz aktualny appstate
                print('--- Idle -- Zalogowany klient {}. Tworze interfejs'.format(cid))
                if cid == 'admin':
                    self.build_admin_ui(cid)
                elif cid == 'test':
                    self.build_test_ui(cid)
                else:
                    self.build_ui(cid)
                print('--- Idle -- Klient {}  ma zaalokowany interfejs: {}.'.format(cid, cList[cid]))

            elif cid == '' and self.tstHang > 30 and not self.websockets:
                print('--- Idle -- Brak klienta - Websocket timeout!.')
                self.tstHang = 1
                headers = {'Content-type': 'text/plain', 'Refresh': '0;url=https://aixm.kpgeo.pl/login'}
                return ['Requested user logging in.', headers]

            try:
                cList[cid]['root'].cRun += 1
            except:
                pass

            map(self._log.debug, self.dump_appstate('--- Idle -- ', self.__dict__))

    def main(self):
        print('- MyApp Main ---> ')
        try:
            self.prevstate = {'None': 'none'}
            self.prevclist = {}
            map(self._log.debug, self.dump_appstate('-- Main -- ', self.__dict__))
            if not self.root:
                print('-- Main -- Nowy widget główny')
                return User(width=1000, height=1000, attributes={
                    'id': 'user'})  # gdy zwracany jest adres widgetu serwer automatycznie wpisuje go do self.root
            else:
                print('-- Main -- Widget juz z istnieje: {}'.format(self.root))
                return self.root

        except Exception as e:
            print(e)


if __name__ == '__main__':
    cList = {}
    start(MyApp, title='AIXM', debug=True, multiple_instance=True, address='127.0.0.1', port=8081, start_browser=False)
