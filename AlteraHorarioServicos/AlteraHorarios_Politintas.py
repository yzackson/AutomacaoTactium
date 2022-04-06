from datetime import datetime
from distutils.log import error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver.exe')
logFile = open("_log.log", "a")

servicos = ['5E53C3C7-5A54-480A-8081-11F63A39E494']

time.sleep(3)
print("\n\n")

login = input('Usuario: ')
senha = input('Senha: ')
ip = input('IP do servidor: ')
dia = input('Dias a serem alterados: \n[1] Seg a Sex\n[2] Sáb')
periodo = input('Perídoo a ser alterado: \n[1] Abertura\n[2] Fechamento')
horario = input('Horário(sem dois pontos -> HHMM)')

def alteraHorárioIniSegSex():
    for i in servicos:
        driver.get('http://' + ip + '/TactiumVoip/IPMonitor/Register/Service/Edit/' + i + '#_002-1') #link para acesso ao serviço no modo edição
        driver.find_element_by_xpath('//*[@id="0"]/td[6]/a/img').click() #lápis para editar o serviço
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="__016_018_h1"]/a/span').click() #aba vigencia
        driver.find_element_by_xpath('//*[@id="0"]/td[11]/a/img').click() #lápis para editar a vigência
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_054"]').clear() #limpa campo do horario
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_054"]').send_keys(horario) #altera horario
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045_save"]').send_keys(Keys.ENTER) #salvar horário
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_save"]').send_keys(Keys.ENTER) #salvar ponto de entrada
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_001_save"]').send_keys(Keys.ENTER) #salvar servico
        time.sleep(1)
        logFile.write(f"\nServico: {i}")

def alteraHorárioFimSegSex():
    for i in servicos:
        driver.get('http://' + ip + '/TactiumVoip/IPMonitor/Register/Service/Edit/' + i + '#_002-1') #link para acesso ao serviço no modo edição
        driver.find_element_by_xpath('//*[@id="0"]/td[6]/a/img').click() #lápis para editar o serviço
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="__016_018_h1"]/a/span').click() #aba vigencia
        driver.find_element_by_xpath('//*[@id="0"]/td[11]/a/img').click() #lápis para editar a vigência
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_055"]').clear() #limpa campo do horario
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_055"]').send_keys(horario) #altera horario
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045_save"]').send_keys(Keys.ENTER) #salvar horário
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_save"]').send_keys(Keys.ENTER) #salvar ponto de entrada
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_001_save"]').send_keys(Keys.ENTER) #salvar servico
        time.sleep(1)
        logFile.write(f"\nServico: {i}")

def alteraHorárioIniSab():
    for i in servicos:
        driver.get('http://' + ip + '/TactiumVoip/IPMonitor/Register/Service/Edit/' + i + '#_002-1') #link para acesso ao serviço no modo edição
        driver.find_element_by_xpath('//*[@id="0"]/td[6]/a/img').click() #lápis para editar o serviço
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="__016_018_h1"]/a/span').click() #aba vigencia
        driver.find_element_by_xpath('//*[@id="1"]/td[11]/a/img').click() #lápis para editar a vigência
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_054"]').clear() #limpa campo do horario
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_054"]').send_keys(horario) #altera horario
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045_save"]').send_keys(Keys.ENTER) #salvar horário
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_save"]').send_keys(Keys.ENTER) #salvar ponto de entrada
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_001_save"]').send_keys(Keys.ENTER) #salvar servico
        time.sleep(1)
        logFile.write(f"\nServico: {i}")

def alteraHorárioFimSab():
    for i in servicos:
        driver.get('http://' + ip + '/TactiumVoip/IPMonitor/Register/Service/Edit/' + i + '#_002-1') #link para acesso ao serviço no modo edição
        driver.find_element_by_xpath('//*[@id="0"]/td[6]/a/img').click() #lápis para editar o serviço
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="__016_018_h1"]/a/span').click() #aba vigencia
        driver.find_element_by_xpath('//*[@id="1"]/td[11]/a/img').click() #lápis para editar a vigência
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_055"]').clear() #limpa campo do horario
        driver.find_element_by_xpath('//*[@id="_016_016_045__016_055"]').send_keys(horario) #altera horario
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_016_045_save"]').send_keys(Keys.ENTER) #salvar horário
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_016_save"]').send_keys(Keys.ENTER) #salvar ponto de entrada
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="_001_save"]').send_keys(Keys.ENTER) #salvar servico
        time.sleep(1)
        logFile.write(f"\nServico: {i}")

def abrePagina():
    driver.get('http://' + ip + '/tactiumvoip/ipmonitor')
    driver.find_element_by_id('username').send_keys(login)
    driver.find_element_by_id('password').send_keys(senha)
    driver.find_element_by_id('LoginControl_LoginButton').send_keys(Keys.ENTER)
    alerta = driver.switch_to.alert
    alerta.accept()

abrePagina()

try:
    logFile.write(f"\n--------------\nConfiguracao de execucao - {datetime.now()}\nlogin: {login}\nsenha: {senha}\nIP: {ip}\nDia: {dia}\nPeriodo: {periodo}\nHorario: {horario}")
    if dia == '1':
        if periodo == '1':
            alteraHorárioIniSegSex()
        elif periodo == '2' :
            alteraHorárioFimSegSex()
        else:
            raise ValueError('Período inválido')
    elif dia == '2':
        if periodo == '1':
            alteraHorárioIniSab()
        elif periodo == '2' :
            alteraHorárioFimSab()
        else:
            raise ValueError('Período inválido')
    else:
        raise ValueError('Dia inválido')
    
    logFile.close()
except ValueError:
    print("Deu erro")
    raise
