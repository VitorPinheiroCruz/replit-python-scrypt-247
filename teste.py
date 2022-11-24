from twilio.rest import Client
import time, os, smtplib, requests
from email.message import Message
from variable import *
import yfinance as yf
from dotenv import load_dotenv
_ = load_dotenv()
#
#
# class Color:
#     def bluered(self, valorPorcentagem, indice):
#         self.valorPorcentagem = valorPorcentagem
#         self.indice = indice
#         if valorPorcentagem >= indice:
#             return 'blue'
#         elif valorPorcentagem < -indice:
#             return 'red'
#
# class CotacaoB3:
#     # yFinance yahoo finance, API
#     minutePenalidade = 10
#     def mglu(self):
#         global requestsPenalidadeMGLU
#         if requestsPenalidadeMGLU == 0 or requestsPenalidadeMGLU + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 mglu = yf.Ticker("MGLU3.SA")
#                 percentMGLU = ((mglu.info['currentPrice'] / mglu.info['previousClose']) - 1) * 100
#                 currentPriceMGLU = mglu.info['currentPrice']
#                 return {'percentMGLU': percentMGLU, 'currentPriceMGLU': currentPriceMGLU}
#             except Exception as error:
#                 print('Erro na Função mglu, Penalidade aplicada')
#                 requestsPenalidadeMGLU = time.time()
#                 print(mglu.info)
#                 print(error)
#                 return {'percentMGLU': 0, 'currentPriceMGLU': 0}
#
#     def oibr(self):
#         global requestsPenalidadeOI
#         if requestsPenalidadeOI == 0 or requestsPenalidadeOI + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 oibr = yf.Ticker("OIBR3.SA")
#                 percentOIBR = ((oibr.info['currentPrice'] / oibr.info['previousClose']) - 1) * 100
#                 currentPriceOIBR = oibr.info['currentPrice']
#                 return {'percentOIBR': percentOIBR, 'currentPriceOIBR': currentPriceOIBR}
#             except Exception as error:
#                 print('Erro na Função oi, Penalidade aplicada')
#                 requestsPenalidadeOI = time.time()
#                 print(oibr.info)
#                 print(error)
#                 return {'percentOIBR': 0, 'currentPriceOIBR': 0}
#
#
# class Cotacao:
#     minutePenalidade = 10
#     def btc(self):
#         global requestsPenalidadeBTC
#         if requestsPenalidadeBTC == 0 or requestsPenalidadeBTC + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação BTC
#                 link_btc = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_change=true'
#                 cotacao_btc = requests.get(link_btc, timeout=15)
#                 cotacao_dic_btc = cotacao_btc.json()['bitcoin']
#                 btc_usd = cotacao_dic_btc['usd']
#                 btc_marketCap = cotacao_dic_btc['usd_market_cap']
#                 btc_usd_24h_change = cotacao_dic_btc['usd_24h_change']
#                 return {'btc_usd': btc_usd, 'btc_marketCap': btc_marketCap, 'btc_usd_24h_change': btc_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função btc, Penalidade aplicada')
#                 requestsPenalidadeBTC = time.time()
#                 print(error)
#                 return {'btc_usd': 0, 'btc_marketCap': 0, 'btc_usd_24h_change': 0}
#
#     def busd(self):
#         global requestsPenalidadeBUSD
#         if requestsPenalidadeBUSD == 0 or requestsPenalidadeBUSD + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # link_busd = 'https://api.coingecko.com/api/v3/simple/price?ids=busd&vs_currencies=brl'
#                 link_usd = "https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=brl&include_24hr_change=true"
#                 cotacao_busd = requests.get(link_usd, timeout=15)
#                 cotacao_dic_busd = cotacao_busd.json()
#                 usd_brl = cotacao_dic_busd['usd']['brl']
#                 usd_brl_24h_change = cotacao_dic_busd['usd']['brl_24h_change']
#                 return {'usd_brl': usd_brl, 'usd_brl_24h_change': usd_brl_24h_change}
#             except Exception as error:
#                 print('Erro na Função busd, Penalidade aplicada')
#                 requestsPenalidadeBUSD = time.time()
#                 print(error)
#                 return {'usd_brl': 0, 'usd_brl_24h_change': 0}
#
#     def cake(self):
#         global requestsPenalidadeCAKE
#         if requestsPenalidadeCAKE == 0 or requestsPenalidadeCAKE + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação CAKE
#                 link_cake = 'https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=usd&include_24hr_change=true'
#                 cotacao_cake = requests.get(link_cake, timeout=15)
#                 cotacao_dic_cake = cotacao_cake.json()
#                 cake_usd = cotacao_dic_cake['pancakeswap-token']['usd']
#                 cake_usd_24h_change = cotacao_dic_cake['pancakeswap-token']['usd_24h_change']
#                 return {'cake_usd': cake_usd, 'cake_usd_24h_change': cake_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função cake, Penalidade aplicada')
#                 requestsPenalidadeCAKE = time.time()
#                 print(error)
#                 return {'cake_usd': 0, 'cake_usd_24h_change': 0}
#
#     def bnb(self):
#         global requestsPenalidadeBNB
#         if requestsPenalidadeBNB == 0 or requestsPenalidadeBNB + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação BNB
#                 link_bnb = 'https://api.coingecko.com/api/v3/simple/price?ids=binance-coin-wormhole&vs_currencies=usd&include_24hr_change=true'
#                 cotacao_bnb = requests.get(link_bnb, timeout=15)
#                 cotacao_dic_bnb = cotacao_bnb.json()
#                 bnb_usd = cotacao_dic_bnb['binance-coin-wormhole']['usd']
#                 bnb_usd_24h_change = cotacao_dic_bnb['binance-coin-wormhole']['usd_24h_change']
#                 return {'bnb_usd': bnb_usd, 'bnb_usd_24h_change': bnb_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função bnb, Penalidade aplicada')
#                 requestsPenalidadeBNB = time.time()
#                 print(error)
#                 return {'bnb_usd': 0, 'bnb_usd_24h_change': 0}
#
#     def icp(self):
#         global requestsPenalidadeICP
#         if requestsPenalidadeICP == 0 or requestsPenalidadeICP + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação ICP
#                 link_icp = 'https://api.coingecko.com/api/v3/simple/price?ids=internet-computer&vs_currencies=usd&include_24hr_change=true'
#                 cotacao_icp = requests.get(link_icp, timeout=15)
#                 cotacao_dic_icp = cotacao_icp.json()
#                 icp_usd = cotacao_dic_icp['internet-computer']['usd']
#                 icp_usd_24h_change = cotacao_dic_icp['internet-computer']['usd_24h_change']
#                 return {'icp_usd': icp_usd, 'icp_usd_24h_change': icp_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função icp, Penalidade aplicada')
#                 requestsPenalidadeICP = time.time()
#                 print(error)
#                 return {'icp_usd': 0, 'icp_usd_24h_change': 0}
#
#     def theta(self):
#         global requestsPenalidadeTHETA
#         if requestsPenalidadeTHETA == 0 or requestsPenalidadeTHETA + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação THETA
#                 link_theta = 'https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=usd&include_24hr_change=true'
#                 cotacao_theta = requests.get(link_theta, timeout=15)
#                 cotacao_dic_theta = cotacao_theta.json()
#                 theta_usd = cotacao_dic_theta['theta-token']['usd']
#                 theta_usd_24h_change = cotacao_dic_theta['theta-token']['usd_24h_change']
#                 return {'theta_usd': theta_usd, 'theta_usd_24h_change': theta_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função theta, Penalidade aplicada')
#                 requestsPenalidadeTHETA = time.time()
#                 print(error)
#                 return {'theta_usd': 0, 'theta_usd_24h_change': 0}
#
#     def ada(self):
#         global requestsPenalidadeADA
#         if requestsPenalidadeADA == 0 or requestsPenalidadeADA + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação ADA
#                 link_ada = 'https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_24hr_change=true'
#                 cotacao_ada = requests.get(link_ada, timeout=15)
#                 cotacao_dic_ada = cotacao_ada.json()['cardano']
#                 ada_usd = cotacao_dic_ada['usd']
#                 ada_usd_24h_change = cotacao_dic_ada['usd_24h_change']
#                 return {'ada_usd': ada_usd, 'ada_usd_24h_change': ada_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função ada, Penalidade aplicada')
#                 requestsPenalidadeADA = time.time()
#                 print(error)
#                 return {'ada_usd': 0, 'ada_usd_24h_change': 0}
#
#     def btt(self):
#         global requestsPenalidadeBTT
#         if requestsPenalidadeBTT == 0 or requestsPenalidadeBTT + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação BTT
#                 link_btt = 'https://api.coingecko.com/api/v3/simple/price?ids=bittorrent&vs_currencies=usd&include_24hr_change=true'
#                 cotacao_btt = requests.get(link_btt, timeout=15)
#                 cotacao_dic_btt = cotacao_btt.json()['bittorrent']
#                 btt_usd = cotacao_dic_btt['usd'] * 100000
#                 btt_usd_24h_change = cotacao_dic_btt['usd_24h_change']
#                 return {'btt_usd': btt_usd, 'btt_usd_24h_change': btt_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função btt, Penalidade aplicada')
#                 requestsPenalidadeBTT = time.time()
#                 print(error)
#                 return {'btt_usd': 0, 'btt_usd_24h_change': 0}
#
#     def quick(self):
#         global requestsPenalidadeQUICK
#         if requestsPenalidadeQUICK == 0 or requestsPenalidadeQUICK + (60 * self.minutePenalidade) <= time.time():
#             try:
#                 # API Coingecko, Cotação QUICK
#                 link_quick = 'https://api.coingecko.com/api/v3/simple/price?ids=quick&vs_currencies=usd&include_24hr_change=true'
#                 cotacao_quick = requests.get(link_quick, timeout=15)
#                 cotacao_dic_quick = cotacao_quick.json()['quick']
#                 quick_usd = cotacao_dic_quick['usd']
#                 quick_usd_24h_change = cotacao_dic_quick['usd_24h_change']
#                 return {'quick_usd': quick_usd, 'quick_usd_24h_change': quick_usd_24h_change}
#             except Exception as error:
#                 print('Erro na Função quick, Penalidade aplicada')
#                 requestsPenalidadeQUICK = time.time()
#                 print(error)
#                 return {'quick_usd': 0, 'quick_usd_24h_change': 0}
#
#
# class Send_email:
#     # É possível utilizar as marcações do HTML
#     email_address = os.environ.get('email_address')
#     email_password = os.environ.get('email_password')
#
#     def email(self, title, message):
#         try:
#             msg = Message()
#             msg['Subject'] = title
#             msg['From'] = self.email_address
#             msg['To'] = os.environ.get('email_destino')
#             msg.add_header('Content-Type', 'text/html')
#             msg.set_payload(message)
#
#             s = smtplib.SMTP('smtp.gmail.com: 587')
#             s.starttls()
#             # Login Credentials for sending the mail
#             s.login(msg['From'], self.email_password)
#             s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
#             print('Email Enviado')
#
#         except Exception as error:
#             print('Erro na função email')
#             print(error)
#
#
#
# renovarBTC = True
# renovarUSD = True
# renovarCAKE = True
# renovarBNB = True
# renovarICP = True
# renovarTHETA = True
# renovarADA = True
# renovarBTT = True
# renovarQUICK = True
# renovarOI = True
# renovarMGLU = True
# erroBTC = True
# erroUSD = True
# erroOI = True
# erroMGLU = True
# erroBNB = True
# erroCAKE = True
# erroTHETA = True
# erroICP = True
# erroADA = True
# erroBTT = True
# erroQUICK = True
#
# # gatilho da mensagem agendada
# gatilho = []
#
# # Aplicando penalidade aos Requests não concluído
# requestsPenalidadeBTC = 0
# requestsPenalidadeBUSD = 0
# requestsPenalidadeCAKE = 0
# requestsPenalidadeBNB = 0
# requestsPenalidadeICP = 0
# requestsPenalidadeTHETA = 0
# requestsPenalidadeADA = 0
# requestsPenalidadeBTT = 0
# requestsPenalidadeQUICK = 0
# requestsPenalidadeMGLU = 0
# requestsPenalidadeOI = 0
# envioAgendamentoPenalidade = 0
#
# # Aplicando penalides aos trigger
# triggerPenalidadeBTC = 0
# triggerPenalidadeBUSD = 0
# triggerPenalidadeCAKE = 0
# triggerPenalidadeBNB = 0
# triggerPenalidadeICP = 0
# triggerPenalidadeTHETA = 0
# triggerPenalidadeADA = 0
# triggerPenalidadeBTT = 0
# triggerPenalidadeQUICK = 0
# triggerPenalidadeMGLU = 0
# triggerPenalidadeOI = 0
#
#
#
# # Verificando as cotações BTC
# btc = Cotacao().btc()
# if btc == None:
#     btc = {'btc_usd': 0, 'btc_marketCap': 0, 'btc_usd_24h_change': 0}
# # Verificando as cotações USD
# time.sleep(0.1)
# usd = Cotacao().busd()
# if usd == None:
#     usd = {'usd_brl': 0, 'usd_brl_24h_change': 0}
# # Verificando as cotações BNB
# time.sleep(0.1)
# bnb = Cotacao().bnb()
# if bnb == None:
#     bnb = {'bnb_usd': 0, 'bnb_usd_24h_change': 0}
# # Verificando as cotações CAKE
# time.sleep(0.1)
# cake = Cotacao().cake()
# if cake == None:
#     cake = {'cake_usd': 0, 'cake_usd_24h_change': 0}
# # Verificando as cotações TETHA
# time.sleep(0.1)
# theta = Cotacao().theta()
# if theta == None:
#     theta = {'theta_usd': 0, 'theta_usd_24h_change': 0}
# # Verificando as cotações ICP
# time.sleep(0.1)
# icp = Cotacao().icp()
# if icp == None:
#     icp = {'icp_usd': 0, 'icp_usd_24h_change': 0}
# # Verificando as cotações ADA
# time.sleep(0.1)
# ada = Cotacao().ada()
# if ada == None:
#     ada = {'ada_usd': 0, 'ada_usd_24h_change': 0}
# # Verificando as cotações BTT
# time.sleep(0.1)
# btt = Cotacao().btt()
# if btt == None:
#     btt = {'btt_usd': 0, 'btt_usd_24h_change': 0}
# # Verificando as cotações QUICK
# time.sleep(0.1)
# quick = Cotacao().quick()
# if quick == None:
#     quick = {'quick_usd': 0, 'quick_usd_24h_change': 0}
# # Verificando as cotações MGLU3
# time.sleep(0.1)
# mglu = CotacaoB3().mglu()
# if mglu == None:
#     mglu = {'percentMGLU': 0, 'currentPriceMGLU': 0}
# # Verificando as cotações OIBR3
# time.sleep(0.1)
# oibr = CotacaoB3().oibr()
# if oibr == None:
#     oibr = {'percentOIBR': 0, 'currentPriceOIBR': 0}
#
# # Porcentagem para gatilho de cor e renovar
# btcPorcentagem = 5
# usdPorcentagem = 5
# oiPorcentagem = 5
# mgluPorcentagem = 5
# bnbPorcentagem = 8
# cakePorcentagem = 8
# thetaPorcentagem = 8
# icpPorcentagem = 10
# adaPorcentagem = 8
# bttPorcentagem = 10
# quickPorcentagem = 10
#
#
# btcColor = Color().bluered(btc['btc_usd_24h_change'], btcPorcentagem)
# usdColor = Color().bluered(usd['usd_brl_24h_change'], usdPorcentagem)
# oiColor = Color().bluered(oibr['percentOIBR'], oiPorcentagem)
# mgluColor = Color().bluered(mglu['percentMGLU'], mgluPorcentagem)
# bnbColor = Color().bluered(bnb['bnb_usd_24h_change'], bnbPorcentagem)
# cakeColor = Color().bluered(cake['cake_usd_24h_change'], cakePorcentagem)
# thetaColor = Color().bluered(theta['theta_usd_24h_change'], thetaPorcentagem)
# icpColor = Color().bluered(icp['icp_usd_24h_change'], icpPorcentagem)
# adaColor = Color().bluered(ada['ada_usd_24h_change'], adaPorcentagem)
# bttColor = Color().bluered(btt['btt_usd_24h_change'], bttPorcentagem)
# quickColor = Color().bluered(quick['quick_usd_24h_change'], quickPorcentagem)
#
#
# mensagem = f"""
# <p> <b>USD</b> <font color={usdColor}> R$ {usd['usd_brl']} </font>, <b>USD 24h</b> <font color={usdColor}> {usd['usd_brl_24h_change']:.2f}% </font> </p>
# <p> <b>OI</b> <font color={oiColor}> R$ {oibr['currentPriceOIBR']:.2f} </font>, <b>OI 24h</b> <font color={oiColor}> {oibr['percentOIBR']:.2f}% </font> </p>
# <p> <b>MGLU</b> <font color={mgluColor}> R${mglu['currentPriceMGLU']:.2f} </font>, <b>MGLU 24h</b> <font color={mgluColor}> {mglu['percentMGLU']:.2f}% </font> </p>
# <p> <b>BTC</b> <font color={btcColor}> U$ {btc['btc_usd']:,} </font>, <b>BTC 24h</b> <font color={btcColor}> {btc['btc_usd_24h_change']:.2f}% </font> </p>
# <p> <b>BTC MarketCap</b> U$ {int(btc['btc_marketCap'] / 1000000000)} Bilhões </p>
# <p> <b>BNB</b> <font color={bnbColor}> U${bnb['bnb_usd']} </font>, <b>BNB 24h</b> <font color={bnbColor}> {bnb['bnb_usd_24h_change']:.2f}% </font> </p>
# <p> <b>CAKE</b> <font color={cakeColor}> U${cake['cake_usd']} </font>, <b>CAKE 24h</b> <font color={cakeColor}> {cake['cake_usd_24h_change']:.2f}% </font> </p>
# <p> <b>THETA</b> <font color={thetaColor}> U$ {theta['theta_usd']} </font>, <b>THETA 24h</b> <font color={thetaColor}> {theta['theta_usd_24h_change']:.2f}% </font> </p>
# <p> <b>ICP</b> <font color={icpColor}> U$ {icp['icp_usd']} </font>, <b>ICP 24h</b> <font color={icpColor}> {icp['icp_usd_24h_change']:.2f}% </font> </p>
# <p> <b>ADA</b> <font color={adaColor}> U$ {ada['ada_usd']:.2f} </font>, <b>ADA 24h</b> <font color={adaColor}> {ada['ada_usd_24h_change']:.2f}% </font> </p>
# <p> <b>BTT</b> <font color={bttColor}> U$ {btt['btt_usd']:.4f} </font>, <b>BTT 24h</b> <font color={bttColor}> {btt['btt_usd_24h_change']:.2f}% </font> </p>
# <p> <b>QUICK</b> <font color={quickColor}> U$ {quick['quick_usd']} </font>, <b>QUICK 24h</b> <font color={quickColor}> {quick['quick_usd_24h_change']:.2f}% </font> </p>"""
#
# title = "testando"
# Send_email().email(title, mensagem)
#


from datetime import date

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]
class CotacaoB3:
    # yFinance yahoo finance, API
    minutePenalidade = 10
    def mglu(self):
        if True:
            global requestsPenalidadeMGLU
            if requestsPenalidadeMGLU == 0 or requestsPenalidadeMGLU + (60 * self.minutePenalidade) <= time.time():
                try:
                    mglu = yf.Ticker("MGLU3.SA")
                    percentMGLU = ((mglu.info['currentPrice'] / mglu.info['previousClose']) - 1) * 100
                    currentPriceMGLU = mglu.info['currentPrice']
                    return {'percentMGLU': percentMGLU, 'currentPriceMGLU': currentPriceMGLU}
                except Exception as error:
                    print('Erro na Função mglu, Penalidade aplicada')
                    requestsPenalidadeMGLU = time.time()
                    print(error)
                    return {'percentMGLU': 0, 'currentPriceMGLU': 0}


    def oibr(self):
        if (hora_minuto >= (8, 0) and hora_minuto <= (22, 0)) and (indice_da_semana != 4 or indice_da_semana != 3) \
                and (month_day not in feriados):
            # print(hora_minuto)
            # print(indice_da_semana)
            # print(month_day)
            # print(feriados)
            global requestsPenalidadeOI
            if requestsPenalidadeOI == 0 or requestsPenalidadeOI + (60 * self.minutePenalidade) <= time.time():
                try:
                    oibr = yf.Ticker("OIBR.SA")
                    percentOIBR = ((oibr.info['currentPrice'] / oibr.info['previousClose']) - 1) * 100
                    currentPriceOIBR = oibr.info['currentPrice']
                    return {'percentOIBR': percentOIBR, 'currentPriceOIBR': currentPriceOIBR}
                except Exception as error:
                    print('Erro na Função oi, Penalidade aplicada')
                    requestsPenalidadeOI = time.time()
                    print(error)
                    return {'percentOIBR': 0, 'currentPriceOIBR': 0}





# print(CotacaoB3().mglu())
print(CotacaoB3().oibr())




# print(month_day)
# feriados = (10,11), (11,2) ,(11,15), (12,30)

# data2 = date(year=2018, month=6, day=29)
#
# class DiasUteis:
#     DIAS = [
#         'Segunda-feira',
#         'Terça-feira',
#         'Quarta-feira',
#         'Quinta-Feira',
#         'Sexta-feira',
#         'Sábado',
#         'Domingo'
#     ]
#     def days(self):
#         data = date.today()
#         # segunda=0, domingo=6
#         indice_da_semana = data.weekday()
#         # segunda=1, domingo=7
#         # numero_do_dia_da_semana = data.isoweekday()
#         if indice_da_semana == 5 or indice_da_semana == 6:
#             return False
#         dia_da_semana = self.DIAS[indice_da_semana]
#         print(dia_da_semana)
# 10 às 17
# data = date.today()
# month_day = data.month, data.day
# print(month_day)
# feriados = (10,11), (11,2) ,(11,15), (12,30)
# if month_day in feriados:
#     print(True)
# else:
#     print(False)