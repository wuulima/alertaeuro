import re
import requests
import smtplib
import email.message

# Consultar a API

requisicao = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['EURBRL']['bid'])
print(cotacao)

# Enviar aviso via E-mail

def enviar_email(cotacao):
    corpo_email = f"""
    <p>Euro está abaixo de R$ 5.30. Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Euro está hoje abaixo de R$5.30"
    msg['From'] = 'empresa.sanithost@gmail.com'
    msg['To'] = 'wuulima@gmail.com'
    password = 'gfqjgnyaijhrrwuc'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais de login para enviar o e-mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.30:
    enviar_email(cotacao)