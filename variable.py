import pytz
from datetime import datetime, date

# (hora, minuto)
hora_minuto = datetime.now(pytz.timezone('America/Sao_Paulo')).hour, \
              datetime.now(pytz.timezone('America/Sao_Paulo')).minute

DIAS = ['Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo']

data = date.today()
indice_da_semana = data.weekday()   # segunda=0, domingo=6
# Feriados = (mês, dia)
feriados = (10,12), (11,2) ,(11,15), (12,30)
month_day = data.month, data.day


# Aplicando penalides aos trigger
triggerPenalidadeBTC = 0
triggerPenalidadeBUSD = 0
triggerPenalidadeCAKE = 0
triggerPenalidadeBNB = 0
triggerPenalidadeICP = 0
triggerPenalidadeTHETA = 0
triggerPenalidadeADA = 0
triggerPenalidadeBTT = 0
triggerPenalidadeQUICK = 0
triggerPenalidadeMGLU = 0
triggerPenalidadeOI = 0

# Aplicando penalidade aos Requests não concluído
requestsPenalidadeBTC = 0
requestsPenalidadeBUSD = 0
requestsPenalidadeCAKE = 0
requestsPenalidadeBNB = 0
requestsPenalidadeICP = 0
requestsPenalidadeTHETA = 0
requestsPenalidadeADA = 0
requestsPenalidadeBTT = 0
requestsPenalidadeQUICK = 0
requestsPenalidadeMGLU = 0
requestsPenalidadeOI = 0
envioAgendamentoPenalidade = 0

# gatilho da mensagem agendada
gatilho = []

renovarBTC = True
renovarUSD = True
renovarCAKE = True
renovarBNB = True
renovarICP = True
renovarTHETA = True
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

# Porcentagem para gatilho de cor e renovar
btcPorcentagem = 5
usdPorcentagem = 5
oiPorcentagem = 5
mgluPorcentagem = 5
bnbPorcentagem = 8
cakePorcentagem = 8
thetaPorcentagem = 8
icpPorcentagem = 10
adaPorcentagem = 8
bttPorcentagem = 10
quickPorcentagem = 10