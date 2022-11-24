from variable import *
from utils import *
import pytz
from datetime import datetime



print('Estamos entrando no while')
while True:
    time.sleep(30)
    # Verificando as cotações BTC
    btc = Cotacao().btc()
    if btc is None:
        btc = {'btc_usd': 0, 'btc_marketCap': 0, 'btc_usd_24h_change': 0}
    # Verificando as cotações USD
    time.sleep(0.1)
    usd = Cotacao().busd()
    if usd is None:
        usd = {'usd_brl': 0, 'usd_brl_24h_change': 0}
    # Verificando as cotações BNB
    time.sleep(0.1)
    bnb = Cotacao().bnb()
    if bnb is None:
        bnb = {'bnb_usd': 0, 'bnb_usd_24h_change': 0}
    # Verificando as cotações CAKE
    time.sleep(0.1)
    cake = Cotacao().cake()
    if cake is None:
        cake = {'cake_usd': 0, 'cake_usd_24h_change': 0}
    # Verificando as cotações TETHA
    time.sleep(0.1)
    theta = Cotacao().theta()
    if theta is None:
        theta = {'theta_usd': 0, 'theta_usd_24h_change': 0}
    # Verificando as cotações ICP
    time.sleep(0.1)
    icp = Cotacao().icp()
    if icp is None:
        icp = {'icp_usd': 0, 'icp_usd_24h_change': 0}
    # Verificando as cotações ADA
    time.sleep(0.1)
    ada = Cotacao().ada()
    if ada is None:
        ada = {'ada_usd': 0, 'ada_usd_24h_change': 0}
    # Verificando as cotações BTT
    time.sleep(0.1)
    btt = Cotacao().btt()
    if btt is None:
        btt = {'btt_usd': 0, 'btt_usd_24h_change': 0}
    # Verificando as cotações QUICK
    time.sleep(0.1)
    quick = Cotacao().quick()
    if quick is None:
        quick = {'quick_usd': 0, 'quick_usd_24h_change': 0}
    # Verificando as cotações MGLU3
    time.sleep(0.1)
    # mglu = CotacaoB3().mglu()
    # if mglu is None:
    #     mglu = {'percentMGLU': 0, 'currentPriceMGLU': 0}
    # Verificando as cotações OIBR3
    time.sleep(0.1)
    # oibr = CotacaoB3().oibr()
    # if oibr is None:
    #     oibr = {'percentOIBR': 0, 'currentPriceOIBR': 0}

    btcColor = Color().bluered(btc['btc_usd_24h_change'], btcPorcentagem)
    usdColor = Color().bluered(usd['usd_brl_24h_change'], usdPorcentagem)
    bnbColor = Color().bluered(bnb['bnb_usd_24h_change'], bnbPorcentagem)
    cakeColor = Color().bluered(cake['cake_usd_24h_change'], cakePorcentagem)
    thetaColor = Color().bluered(theta['theta_usd_24h_change'], thetaPorcentagem)
    icpColor = Color().bluered(icp['icp_usd_24h_change'], icpPorcentagem)
    adaColor = Color().bluered(ada['ada_usd_24h_change'], adaPorcentagem)
    bttColor = Color().bluered(btt['btt_usd_24h_change'], bttPorcentagem)
    quickColor = Color().bluered(quick['quick_usd_24h_change'], quickPorcentagem)

    # Agendado para às 11:00, 13:00, 16:00, 17:00 e 19:00 (-3utc)
    # agendamento = [(11+3), (13+3), (16+3), (17+3), (19+3)]  # (utc)
    agendamento = [11, 13, 16, 17, 19]  # (utc)
    # hora = time.gmtime().tm_hour
    hora = datetime.now(pytz.timezone('America/Sao_Paulo')).hour
    for horario in agendamento:
        if horario == hora and hora not in gatilho:
            if envioAgendamentoPenalidade == 0 or envioAgendamentoPenalidade + (60 * 10) <= time.time():
                try:
                    mensagem = f"""
<p> <b>USD</b> <font color={usdColor}> R$ {usd['usd_brl']} </font>, <b>USD 24h</b> <font color={usdColor}> {usd['usd_brl_24h_change']:.2f}% </font> </p>
<p> <b>BTC</b> <font color={btcColor}> U$ {btc['btc_usd']:,} </font>, <b>BTC 24h</b> <font color={btcColor}> {btc['btc_usd_24h_change']:.2f}% </font> </p>
<p> <b>BTC MarketCap</b> U$ {int(btc['btc_marketCap'] / 1000000000)} Bilhões </p>
<p> <b>BNB</b> <font color={bnbColor}> U${bnb['bnb_usd']} </font>, <b>BNB 24h</b> <font color={bnbColor}> {bnb['bnb_usd_24h_change']:.2f}% </font> </p>
<p> <b>CAKE</b> <font color={cakeColor}> U${cake['cake_usd']} </font>, <b>CAKE 24h</b> <font color={cakeColor}> {cake['cake_usd_24h_change']:.2f}% </font> </p>
<p> <b>THETA</b> <font color={thetaColor}> U$ {theta['theta_usd']} </font>, <b>THETA 24h</b> <font color={thetaColor}> {theta['theta_usd_24h_change']:.2f}% </font> </p>
<p> <b>ICP</b> <font color={icpColor}> U$ {icp['icp_usd']} </font>, <b>ICP 24h</b> <font color={icpColor}> {icp['icp_usd_24h_change']:.2f}% </font> </p>
<p> <b>ADA</b> <font color={adaColor}> U$ {ada['ada_usd']:.2f} </font>, <b>ADA 24h</b> <font color={adaColor}> {ada['ada_usd_24h_change']:.2f}% </font> </p>
<p> <b>BTT</b> <font color={bttColor}> U$ {btt['btt_usd']:.4f} </font>, <b>BTT 24h</b> <font color={bttColor}> {btt['btt_usd_24h_change']:.2f}% </font> </p>
<p> <b>QUICK</b> <font color={quickColor}> U$ {quick['quick_usd']} </font>, <b>QUICK 24h</b> <font color={quickColor}> {quick['quick_usd_24h_change']:.2f}% </font> </p>"""
                    title = "Cotações"
                    Send_email().email(title, mensagem)
                    print('email enviado, hora agendada')
                    # print(horario-3, hora-3)
                    gatilho.append(horario)
                    time.sleep(45)
                except Exception as erro:
                    envioAgendamentoPenalidade = time.time()
                    print('Houve erro no envio da mensagem, VERIFICAR!')
                    print(erro)

    if hora_minuto == (0, 0) or hora_minuto == (0, 1):
        print('Resetando as condições renovar, hora 0,0')
        renovarBTC = True
        renovarUSD = True
        renovarBNB = True
        renovarCAKE = True
        renovarTHETA = True
        renovarICP = True
        renovarADA = True
        renovarBTT = True
        renovarQUICK = True
        renovarOI = True
        renovarMGLU = True
        erroBTC = True
        erroUSD = True
        erroOI = True
        erroMGLU = True
        erroBNB = True
        erroCAKE = True
        erroTHETA = True
        erroICP = True
        erroADA = True
        erroBTT = True
        erroQUICK = True
        gatilho = []
        time.sleep(130)

    minutesPenalidadeTrigger = 10
    if renovarBTC:
        if triggerPenalidadeBTC == 0 or triggerPenalidadeBTC + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(btc['btc_usd_24h_change']) > btcPorcentagem) or \
                        (float(btc['btc_usd_24h_change']) < -btcPorcentagem):
                    mensagem = f"""<p> BTC <font color={btcColor}> U$ {btc['btc_usd']:,} </font>, BTC 24h <font color={btcColor}> {btc['btc_usd_24h_change']:.2f}% </font> </p>"""
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarBTC')
                    renovarBTC = False
            except Exception as error:
                if erroBTC:
                    message = f"Erro na if renovarBTC ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroBTC = False
                print('Erro na if renovarBTC')
                print(btc)
                print(error)
                triggerPenalidadeBTC = time.time()

    if renovarUSD:
        if triggerPenalidadeBUSD == 0 or triggerPenalidadeBUSD + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(usd['usd_brl_24h_change']) > usdPorcentagem) or \
                        (float(usd['usd_brl_24h_change']) < -usdPorcentagem):
                    mensagem = f"""<p> USD <font color={usdColor}> R$ {usd['usd_brl']} </font>, USD 24h <font color={usdColor}> {usd['usd_brl_24h_change']:.2f}% </font> </p>"""
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarUSD')
                    renovarUSD = False
            except Exception as error:
                if erroUSD:
                    message = f"Erro na if renovarUSD ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroUSD = False
                print('Erro na if renovarUSD')
                print(usd)
                print(error)
                triggerPenalidadeBUSD = time.time()

    if renovarBNB:
        if triggerPenalidadeBNB == 0 or triggerPenalidadeBNB + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(bnb['bnb_usd_24h_change']) > bnbPorcentagem) or \
                        (float(bnb['bnb_usd_24h_change']) < -bnbPorcentagem):
                    mensagem = f"""<p>BNB <font color={bnbColor}> U$ {bnb['bnb_usd']}</font>, BNB 24h <font color={bnbColor}> {bnb['bnb_usd_24h_change']:.2f}% </font> </p>"""
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarBNB')
                    renovarBNB = False
            except Exception as error:
                if erroBNB:
                    message = f"Erro na if renovarBNB ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroBNB = False
                print('Erro na if renovarBNB')
                print(bnb)
                print(error)
                triggerPenalidadeBNB = time.time()

    if renovarCAKE:
        if triggerPenalidadeCAKE == 0 or triggerPenalidadeCAKE + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(cake['cake_usd_24h_change']) > cakePorcentagem) or \
                        (float(cake['cake_usd_24h_change']) < -cakePorcentagem):
                    mensagem = f"""<p>CAKE <font color={cakeColor}> U$ {cake['cake_usd']} </font>, CAKE 24h <font color={cakeColor}> {cake['cake_usd_24h_change']:.2f}% </font></p>"""
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarCAKE')
                    renovarCAKE = False
            except Exception as error:
                if erroCAKE:
                    message = f"Erro na if renovarCAKE ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroCAKE = False
                print('Erro na if renovarCAKE')
                print(cake)
                print(error)
                triggerPenalidadeCAKE = time.time()

    if renovarTHETA:
        if triggerPenalidadeTHETA == 0 or triggerPenalidadeTHETA + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(theta['theta_usd_24h_change']) > thetaPorcentagem) or \
                        (float(theta['theta_usd_24h_change']) < -thetaPorcentagem):
                    mensagem = f"<p>THETA <font color={thetaColor}> U$ {theta['theta_usd']} </font>, THETA 24h <font color={thetaColor}> {theta['theta_usd_24h_change']:.2f}% </font></p>"
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarTHETA')
                    renovarTHETA = False
            except Exception as error:
                if erroTHETA:
                    message = f"Erro na if renovarTHETA ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroTHETA = False
                print('Erro na if renovarTHETA')
                print(theta)
                print(error)
                triggerPenalidadeTHETA = time.time()

    if renovarICP:
        if triggerPenalidadeICP == 0 or triggerPenalidadeICP + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(icp['icp_usd_24h_change']) > icpPorcentagem) or \
                        (float(icp['icp_usd_24h_change']) < -icpPorcentagem):
                    mensagem = f"""<p>ICP <font color={icpColor}> U$ {icp['icp_usd']} </font>, ICP 24h <font color={icpColor}> {icp['icp_usd_24h_change']:.2f}% </font> </p>"""
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarICP')
                    renovarICP = False
            except Exception as error:
                if erroICP:
                    message = f"Erro na if renovarICP ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroICP = False
                print('Erro na if renovarICP')
                print(icp)
                print(error)
                triggerPenalidadeICP = time.time()

    if renovarADA:
        if triggerPenalidadeADA == 0 or triggerPenalidadeADA + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(ada['ada_usd_24h_change']) > adaPorcentagem) or \
                        (float(ada['ada_usd_24h_change']) < -adaPorcentagem):
                    mensagem = f"""<p>ADA <font color={adaColor}> U$ {ada['ada_usd']:.2f} </font>, ADA 24h <font color={adaColor}>{ada['ada_usd_24h_change']:.2f}% </font></p>"""
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarADA')
                    renovarADA = False
            except Exception as error:
                if erroADA:
                    message = f"Erro na if renovarADA ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroADA = False
                print('Erro na if renovarADA')
                print(ada)
                print(error)
                triggerPenalidadeADA = time.time()

    if renovarBTT:
        if triggerPenalidadeBTT == 0 or triggerPenalidadeBTT + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(btt['btt_usd_24h_change']) > bttPorcentagem) or \
                        (float(btt['btt_usd_24h_change']) < -bttPorcentagem):
                    mensagem = f"""<p>BTT <font color={bttColor}> U$ {btt['btt_usd']:.4f} </font>, BTT 24h <font color={bttColor}> {btt['btt_usd_24h_change']:.2f}% </font> </p>"""
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarBTT')
                    renovarBTT = False
            except Exception as error:
                if erroBTT:
                    message = f"Erro na if renovarBTT ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroBTT = False
                print('Erro na if renovarBTT')
                print(btt)
                print(error)
                triggerPenalidadeBTT = time.time()

    if renovarQUICK:
        if triggerPenalidadeQUICK == 0 or triggerPenalidadeQUICK + (60 * minutesPenalidadeTrigger) <= time.time():
            try:
                if (float(quick['quick_usd_24h_change']) > quickPorcentagem) or \
                        (float(quick['quick_usd_24h_change']) < -quickPorcentagem):
                    mensagem = f"<p>QUICK <font color={quickColor}> U$ {quick['quick_usd']} </font>, QUICK 24h <font color={quickColor}> {quick['quick_usd_24h_change']:.2f}% </font> </p>"
                    # Send_whatsapp().whatsapp(mensagem)
                    # Send_sms().sms(mensagem)
                    title = 'renovar'
                    Send_email().email(title, mensagem)
                    print('email enviado renovarQUICk')
                    renovarQUICK = False
            except Exception as error:
                if erroQUICK:
                    message = f"Erro na if renovarQUICK ||| {error}. Penalidade Aplicada"
                    Send_email().email('Erro', message)
                    erroQUICK = False
                print('Erro na if renovarQUICK')
                print(quick)
                print(error)
                triggerPenalidadeQUICK = time.time()