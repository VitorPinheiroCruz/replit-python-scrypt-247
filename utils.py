import os
import requests
import smtplib
import time
from email.message import Message
from variable import *
from dotenv import load_dotenv
_ = load_dotenv()


class Color:
    def bluered(self, valorPorcentagem, indice):
        self.valorPorcentagem = valorPorcentagem
        self.indice = indice
        if valorPorcentagem >= indice:
            return 'green'
        elif valorPorcentagem < -indice:
            return 'red'
        else:
            return 'blue'


class Cotacao:
    minutePenalidade = 10
    def btc(self):
        global requestsPenalidadeBTC
        if requestsPenalidadeBTC == 0 or requestsPenalidadeBTC + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação BTC
                link_btc = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_change=true'
                cotacao_btc = requests.get(link_btc, timeout=15)
                cotacao_dic_btc = cotacao_btc.json()['bitcoin']
                btc_usd = cotacao_dic_btc['usd']
                btc_marketCap = cotacao_dic_btc['usd_market_cap']
                btc_usd_24h_change = cotacao_dic_btc['usd_24h_change']
                return {'btc_usd': btc_usd, 'btc_marketCap': btc_marketCap, 'btc_usd_24h_change': btc_usd_24h_change}
            except Exception as error:
                print('Erro na Função btc, Penalidade aplicada')
                requestsPenalidadeBTC = time.time()
                print(error)
                return {'btc_usd': 0, 'btc_marketCap': 0, 'btc_usd_24h_change': 0}

    def busd(self):
        global requestsPenalidadeBUSD
        if requestsPenalidadeBUSD == 0 or requestsPenalidadeBUSD + (60 * self.minutePenalidade) <= time.time():
            try:
                # link_busd = 'https://api.coingecko.com/api/v3/simple/price?ids=busd&vs_currencies=brl'
                link_usd = "https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=brl&include_24hr_change=true"
                cotacao_busd = requests.get(link_usd, timeout=15)
                cotacao_dic_busd = cotacao_busd.json()
                usd_brl = cotacao_dic_busd['usd']['brl']
                usd_brl_24h_change = cotacao_dic_busd['usd']['brl_24h_change']
                return {'usd_brl': usd_brl, 'usd_brl_24h_change': usd_brl_24h_change}
            except Exception as error:
                print('Erro na Função busd, Penalidade aplicada')
                requestsPenalidadeBUSD = time.time()
                print(error)
                return {'usd_brl': 0, 'usd_brl_24h_change': 0}

    def cake(self):
        global requestsPenalidadeCAKE
        if requestsPenalidadeCAKE == 0 or requestsPenalidadeCAKE + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação CAKE
                link_cake = 'https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=usd&include_24hr_change=true'
                cotacao_cake = requests.get(link_cake, timeout=15)
                cotacao_dic_cake = cotacao_cake.json()
                cake_usd = cotacao_dic_cake['pancakeswap-token']['usd']
                cake_usd_24h_change = cotacao_dic_cake['pancakeswap-token']['usd_24h_change']
                return {'cake_usd': cake_usd, 'cake_usd_24h_change': cake_usd_24h_change}
            except Exception as error:
                print('Erro na Função cake, Penalidade aplicada')
                requestsPenalidadeCAKE = time.time()
                print(error)
                return {'cake_usd': 0, 'cake_usd_24h_change': 0}

    def bnb(self):
        global requestsPenalidadeBNB
        if requestsPenalidadeBNB == 0 or requestsPenalidadeBNB + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação BNB
                link_bnb = 'https://api.coingecko.com/api/v3/simple/price?ids=binance-coin-wormhole&vs_currencies=usd&include_24hr_change=true'
                cotacao_bnb = requests.get(link_bnb, timeout=15)
                cotacao_dic_bnb = cotacao_bnb.json()
                bnb_usd = cotacao_dic_bnb['binance-coin-wormhole']['usd']
                bnb_usd_24h_change = cotacao_dic_bnb['binance-coin-wormhole']['usd_24h_change']
                return {'bnb_usd': bnb_usd, 'bnb_usd_24h_change': bnb_usd_24h_change}
            except Exception as error:
                print('Erro na Função bnb, Penalidade aplicada')
                requestsPenalidadeBNB = time.time()
                print(error)
                return {'bnb_usd': 0, 'bnb_usd_24h_change': 0}

    def icp(self):
        global requestsPenalidadeICP
        if requestsPenalidadeICP == 0 or requestsPenalidadeICP + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação ICP
                link_icp = 'https://api.coingecko.com/api/v3/simple/price?ids=internet-computer&vs_currencies=usd&include_24hr_change=true'
                cotacao_icp = requests.get(link_icp, timeout=15)
                cotacao_dic_icp = cotacao_icp.json()
                icp_usd = cotacao_dic_icp['internet-computer']['usd']
                icp_usd_24h_change = cotacao_dic_icp['internet-computer']['usd_24h_change']
                return {'icp_usd': icp_usd, 'icp_usd_24h_change': icp_usd_24h_change}
            except Exception as error:
                print('Erro na Função icp, Penalidade aplicada')
                requestsPenalidadeICP = time.time()
                print(error)
                return {'icp_usd': 0, 'icp_usd_24h_change': 0}

    def theta(self):
        global requestsPenalidadeTHETA
        if requestsPenalidadeTHETA == 0 or requestsPenalidadeTHETA + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação THETA
                link_theta = 'https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=usd&include_24hr_change=true'
                cotacao_theta = requests.get(link_theta, timeout=15)
                cotacao_dic_theta = cotacao_theta.json()
                theta_usd = cotacao_dic_theta['theta-token']['usd']
                theta_usd_24h_change = cotacao_dic_theta['theta-token']['usd_24h_change']
                return {'theta_usd': theta_usd, 'theta_usd_24h_change': theta_usd_24h_change}
            except Exception as error:
                print('Erro na Função theta, Penalidade aplicada')
                requestsPenalidadeTHETA = time.time()
                print(error)
                return {'theta_usd': 0, 'theta_usd_24h_change': 0}

    def ada(self):
        global requestsPenalidadeADA
        if requestsPenalidadeADA == 0 or requestsPenalidadeADA + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação ADA
                link_ada = 'https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_24hr_change=true'
                cotacao_ada = requests.get(link_ada, timeout=15)
                cotacao_dic_ada = cotacao_ada.json()['cardano']
                ada_usd = cotacao_dic_ada['usd']
                ada_usd_24h_change = cotacao_dic_ada['usd_24h_change']
                return {'ada_usd': ada_usd, 'ada_usd_24h_change': ada_usd_24h_change}
            except Exception as error:
                print('Erro na Função ada, Penalidade aplicada')
                requestsPenalidadeADA = time.time()
                print(error)
                return {'ada_usd': 0, 'ada_usd_24h_change': 0}

    def btt(self):
        global requestsPenalidadeBTT
        if requestsPenalidadeBTT == 0 or requestsPenalidadeBTT + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação BTT
                link_btt = 'https://api.coingecko.com/api/v3/simple/price?ids=bittorrent&vs_currencies=usd&include_24hr_change=true'
                cotacao_btt = requests.get(link_btt, timeout=15)
                cotacao_dic_btt = cotacao_btt.json()['bittorrent']
                btt_usd = cotacao_dic_btt['usd'] * 100000
                btt_usd_24h_change = cotacao_dic_btt['usd_24h_change']
                return {'btt_usd': btt_usd, 'btt_usd_24h_change': btt_usd_24h_change}
            except Exception as error:
                print('Erro na Função btt, Penalidade aplicada')
                requestsPenalidadeBTT = time.time()
                print(error)
                return {'btt_usd': 0, 'btt_usd_24h_change': 0}

    def quick(self):
        global requestsPenalidadeQUICK
        if requestsPenalidadeQUICK == 0 or requestsPenalidadeQUICK + (60 * self.minutePenalidade) <= time.time():
            try:
                # API Coingecko, Cotação QUICK
                link_quick = 'https://api.coingecko.com/api/v3/simple/price?ids=quick&vs_currencies=usd&include_24hr_change=true'
                cotacao_quick = requests.get(link_quick, timeout=15)
                cotacao_dic_quick = cotacao_quick.json()['quick']
                quick_usd = cotacao_dic_quick['usd']
                quick_usd_24h_change = cotacao_dic_quick['usd_24h_change']
                return {'quick_usd': quick_usd, 'quick_usd_24h_change': quick_usd_24h_change}
            except Exception as error:
                print('Erro na Função quick, Penalidade aplicada')
                requestsPenalidadeQUICK = time.time()
                print(error)
                return {'quick_usd': 0, 'quick_usd_24h_change': 0}


class Send_email:
    # É possível utilizar as marcações do HTML
    email_address = os.environ.get('email_address')
    email_password = os.environ.get('email_password')

    def email(self, title, message):
        try:
            msg = Message()
            msg['Subject'] = title
            msg['From'] = self.email_address
            msg['To'] = os.environ.get('email_destino')
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(message)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], self.email_password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

        except Exception as error:
            print('Erro na função email')
            print(error)
