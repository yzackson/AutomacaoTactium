from ctypes import sizeof
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'chromedriver.exe')

login = ''
senha = ''
ip = ''

nomes = ['h155', 'h156']
ramais = ['10.246.75.155', '10.246.75.156']
#dominio = '.medsenior.corp'

driver.get('http://' + ip + '/tactiumvoip/ipmonitor')

driver.find_element_by_id('username').send_keys(login)
driver.find_element_by_id('password').send_keys(senha)
driver.find_element_by_id('LoginControl_LoginButton').send_keys(Keys.ENTER)

time.sleep(1)
alerta = driver.switch_to.alert
alerta.accept()

for i  in range(0,len(ramais)):
    #link para criação de ramais
    print(nomes[i])
    driver.get('http://' + ip + '/TactiumVoip/IPMonitor/Register/Station/New')
    driver.find_element_by_xpath('//*[@id="_006"]').send_keys(nomes[i])
    driver.find_element_by_xpath('//*[@id="_007"]').send_keys(ramais[i])
    driver.find_element_by_xpath('//*[@id="_008"]').send_keys(nomes[i])
    driver.find_element_by_xpath('//*[@id="_009_true"]').click()
    driver.find_element_by_xpath('//*[@id="__003_h1"]/a/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="_011_lft"]/option[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="_011_mar"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="_001_save"]').send_keys(Keys.ENTER)
    time.sleep(2)
    print("created...")
    