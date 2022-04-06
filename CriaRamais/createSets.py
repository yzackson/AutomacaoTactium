from ctypes import sizeof
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'chromedriver.exe')

login = 'admin'
senha = 'Gene7790'
ip = '192.168.200.221'

#nomes = ['h155', 'h156']
ramais = ['172.25.128.7', '172.25.128.8', '172.25.128.9', '172.25.128.10', '172.25.128.11', '172.25.128.12', '172.25.128.13', '172.25.128.14', '172.25.128.15', '172.25.128.16', '172.25.128.17', '172.25.128.18', '172.25.128.19', '172.25.128.20', '172.25.128.21', '172.25.128.22', '172.25.128.24', '172.25.128.25', '172.25.128.26', '172.25.128.27', '172.25.128.28', '172.25.128.29', '172.25.128.30', '172.25.128.31', '172.25.128.32', '172.25.128.33', '172.25.128.34', '172.25.128.35', '172.25.128.36', '172.25.128.37', '172.25.128.38', '172.25.128.39', '172.25.128.40', '172.25.128.41', '172.25.128.42', '172.25.128.43', '172.25.128.44', '172.25.128.45', '172.25.128.46', '172.25.128.47', '172.25.128.48', '172.25.128.49', '172.25.128.50', '172.25.128.51', '172.25.128.52', '172.25.128.53', '172.25.128.54', '172.25.128.55', '172.25.128.56', '172.25.128.57', '172.25.128.58', '172.25.128.59', '172.25.128.60', '172.25.128.61', '172.25.128.62', '172.25.128.63', '172.25.128.64', '172.25.128.65', '172.25.128.66', '172.25.128.67', '172.25.128.68', '172.25.128.69', '172.25.128.70', '172.25.128.71', '172.25.128.72', '172.25.128.73', '172.25.128.74', '172.25.128.75', '172.25.128.76', '172.25.128.77', '172.25.128.78', '172.25.128.79', '172.25.128.80', '172.25.128.81', '172.25.128.82', '172.25.128.83', '172.25.128.84', '172.25.128.85', '172.25.128.86', '172.25.128.87', '172.25.128.88', '172.25.128.89', '172.25.128.90', '172.25.128.91', '172.25.128.92', '172.25.128.93', '172.25.128.94', '172.25.128.95', '172.25.128.96', '172.25.128.97', '172.25.128.98', '172.25.128.99', '172.25.128.100', '172.25.128.101', '172.25.128.102', '172.25.128.103', '172.25.128.104', '172.25.128.105', '172.25.128.106', '172.25.128.107', '172.25.128.108', '172.25.128.109', '172.25.128.110', '172.25.128.111', '172.25.128.112', '172.25.128.113', '172.25.128.114', '172.25.128.115', '172.25.128.116', '172.25.128.117', '172.25.128.118', '172.25.128.119', '172.25.128.120', '172.25.128.121', '172.25.128.122', '172.25.128.123', '172.25.128.124', '172.25.128.125', '172.25.128.126', '172.25.128.127', '172.25.128.128', '172.25.128.129', '172.25.128.130', '172.25.128.131', '172.25.128.132', '172.25.128.133', '172.25.128.134', '172.25.128.135', '172.25.128.136', '172.25.128.137', '172.25.128.138', '172.25.128.139', '172.25.128.140', '172.25.128.141', '172.25.128.142', '172.25.128.143', '172.25.128.144', '172.25.128.145', '172.25.128.146', '172.25.128.147', '172.25.128.148', '172.25.128.149', '172.25.128.150', '172.25.128.151', '172.25.128.152', '172.25.128.153', '172.25.128.154', '172.25.128.155', '172.25.128.156', '172.25.128.157', '172.25.128.158', '172.25.128.159', '172.25.128.160', '172.25.128.161', '172.25.128.162', '172.25.128.163', '172.25.128.164', '172.25.128.165', '172.25.128.166', '172.25.128.167', '172.25.128.168', '172.25.128.169', '172.25.128.170', '172.25.128.171', '172.25.128.172', '172.25.128.173', '172.25.128.174', '172.25.128.175', '172.25.128.176', '172.25.128.177', '172.25.128.178', '172.25.128.179', '172.25.128.180', '172.25.128.181', '172.25.128.182', '172.25.128.183', '172.25.128.184', '172.25.128.185', '172.25.128.186', '172.25.128.187', '172.25.128.188', '172.25.128.189', '172.25.128.190', '172.25.128.191', '172.25.128.192', '172.25.128.193', '172.25.128.194', '172.25.128.195', '172.25.128.196', '172.25.128.197', '172.25.128.198', '172.25.128.199', '172.25.128.200', '172.25.128.201', '172.25.128.202', '172.25.128.203', '172.25.128.204', '172.25.128.205', '172.25.128.206', '172.25.128.207', '172.25.128.208', '172.25.128.209', '172.25.128.210', '172.25.128.211', '172.25.128.212', '172.25.128.213', '172.25.128.214', '172.25.128.215', '172.25.128.216', '172.25.128.217', '172.25.128.218', '172.25.128.219', '172.25.128.220', '172.25.128.221', '172.25.128.222', '172.25.128.223', '172.25.128.224', '172.25.128.225', '172.25.128.226', '172.25.128.227', '172.25.128.228', '172.25.128.229', '172.25.128.230', '172.25.128.231', '172.25.128.232', '172.25.128.233', '172.25.128.234', '172.25.128.235', '172.25.128.236', '172.25.128.237', '172.25.128.238', '172.25.128.239', '172.25.128.240', '172.25.128.241', '172.25.128.242', '172.25.128.243', '172.25.128.244', '172.25.128.245', '172.25.128.246', '172.25.128.247', '172.25.128.248', '172.25.128.249', '172.25.128.250', '172.25.128.251', '172.25.128.252', '172.25.128.253', '172.25.128.254', '172.25.129.2', '172.25.129.3', '172.25.129.4', '172.25.129.5', '172.25.129.6', '172.25.129.7', '172.25.129.8', '172.25.129.9', '172.25.129.10', '172.25.129.11', '172.25.129.12', '172.25.129.13', '172.25.129.14', '172.25.129.15', '172.25.129.16', '172.25.129.17', '172.25.129.18', '172.25.129.19', '172.25.129.20', '172.25.129.21', '172.25.129.22', '172.25.129.23', '172.25.129.24', '172.25.129.25', '172.25.129.26', '172.25.129.27', '172.25.129.28', '172.25.129.29', '172.25.129.30', '172.25.129.31', '172.25.129.32', '172.25.129.33', '172.25.129.34', '172.25.129.35', '172.25.129.36', '172.25.129.37', '172.25.129.38', '172.25.129.39', '172.25.129.40', '172.25.129.41', '172.25.129.42', '172.25.129.43', '172.25.129.44', '172.25.129.45', '172.25.129.46', '172.25.129.47', '172.25.129.48', '172.25.129.49', '172.25.129.50', '172.25.129.51', '172.25.129.52', '172.25.129.53', '172.25.129.54', '172.25.129.55', '172.25.129.56', '172.25.129.57', '172.25.129.58', '172.25.129.59', '172.25.129.60', '172.25.129.61', '172.25.129.62', '172.25.129.63', '172.25.129.64', '172.25.129.65', '172.25.129.66', '172.25.129.67', '172.25.129.68', '172.25.129.69', '172.25.129.70', '172.25.129.71', '172.25.129.72', '172.25.129.73', '172.25.129.74', '172.25.129.75', '172.25.129.76', '172.25.129.77', '172.25.129.78', '172.25.129.79', '172.25.129.80', '172.25.129.81', '172.25.129.82', '172.25.129.83', '172.25.129.84', '172.25.129.85', '172.25.129.86', '172.25.129.87', '172.25.129.88', '172.25.129.89', '172.25.129.90', '172.25.129.91', '172.25.129.92', '172.25.129.93', '172.25.129.94', '172.25.129.95', '172.25.129.96', '172.25.129.97', '172.25.129.98', '172.25.129.99', '172.25.129.100', '172.25.129.101', '172.25.129.102', '172.25.129.103', '172.25.129.104', '172.25.129.105', '172.25.129.106', '172.25.129.107', '172.25.129.108', '172.25.129.109', '172.25.129.110', '172.25.129.111', '172.25.129.112', '172.25.129.113', '172.25.129.114', '172.25.129.115', '172.25.129.116', '172.25.129.117', '172.25.129.118', '172.25.129.119', '172.25.129.120', '172.25.129.121', '172.25.129.122', '172.25.129.123', '172.25.129.124', '172.25.129.125', '172.25.129.126', '172.25.129.127', '172.25.129.128', '172.25.129.129', '172.25.129.130',
          '172.25.129.131', '172.25.129.132', '172.25.129.133', '172.25.129.134', '172.25.129.135', '172.25.129.136', '172.25.129.137', '172.25.129.138', '172.25.129.139', '172.25.129.140', '172.25.129.141', '172.25.129.142', '172.25.129.143', '172.25.129.144', '172.25.129.145', '172.25.129.146', '172.25.129.147', '172.25.129.148', '172.25.129.149', '172.25.129.150', '172.25.129.151', '172.25.129.152', '172.25.129.153', '172.25.129.154', '172.25.129.155', '172.25.129.156', '172.25.129.157', '172.25.129.158', '172.25.129.159', '172.25.129.160', '172.25.129.161', '172.25.129.162', '172.25.129.163', '172.25.129.164', '172.25.129.165', '172.25.129.166', '172.25.129.167', '172.25.129.168', '172.25.129.169', '172.25.129.170', '172.25.129.171', '172.25.129.172', '172.25.129.173', '172.25.129.174', '172.25.129.175', '172.25.129.176', '172.25.129.177', '172.25.129.178', '172.25.129.179', '172.25.129.180', '172.25.129.181', '172.25.129.182', '172.25.129.183', '172.25.129.184', '172.25.129.185', '172.25.129.186', '172.25.129.187', '172.25.129.188', '172.25.129.189', '172.25.129.190', '172.25.129.191', '172.25.129.192', '172.25.129.193', '172.25.129.194', '172.25.129.195', '172.25.129.196', '172.25.129.197', '172.25.129.198', '172.25.129.199', '172.25.129.200', '172.25.129.201', '172.25.129.202', '172.25.129.203', '172.25.129.204', '172.25.129.205', '172.25.129.206', '172.25.129.207', '172.25.129.208', '172.25.129.209', '172.25.129.210', '172.25.129.211', '172.25.129.212', '172.25.129.213', '172.25.129.214', '172.25.129.215', '172.25.129.216', '172.25.129.217', '172.25.129.218', '172.25.129.219', '172.25.129.220', '172.25.129.221', '172.25.129.222', '172.25.129.223', '172.25.129.224', '172.25.129.225', '172.25.129.226', '172.25.129.227', '172.25.129.228', '172.25.129.229', '172.25.129.230', '172.25.129.231', '172.25.129.232', '172.25.129.233', '172.25.129.234', '172.25.129.235', '172.25.129.236', '172.25.129.237', '172.25.129.238', '172.25.129.239', '172.25.129.240', '172.25.129.241', '172.25.129.242', '172.25.129.243', '172.25.129.244', '172.25.129.245', '172.25.129.246', '172.25.129.247', '172.25.129.248', '172.25.129.249', '172.25.129.250', '172.25.129.251', '172.25.129.252', '172.25.129.253', '172.25.129.254', '172.25.130.2', '172.25.130.3', '172.25.130.4', '172.25.130.5', '172.25.130.6', '172.25.130.7', '172.25.130.8', '172.25.130.9', '172.25.130.10', '172.25.130.11', '172.25.130.12', '172.25.130.13', '172.25.130.14', '172.25.130.15', '172.25.130.16', '172.25.130.17', '172.25.130.18', '172.25.130.19', '172.25.130.20', '172.25.130.21', '172.25.130.22', '172.25.130.23', '172.25.130.24', '172.25.130.25', '172.25.130.26', '172.25.130.27', '172.25.130.28', '172.25.130.29', '172.25.130.30', '172.25.130.31', '172.25.130.32', '172.25.130.33', '172.25.130.34', '172.25.130.35', '172.25.130.36', '172.25.130.37', '172.25.130.38', '172.25.130.39', '172.25.130.40', '172.25.130.41', '172.25.130.42', '172.25.130.43', '172.25.130.44', '172.25.130.45', '172.25.130.46', '172.25.130.47', '172.25.130.48', '172.25.130.49', '172.25.130.50', '172.25.130.51', '172.25.130.52', '172.25.130.53', '172.25.130.54', '172.25.130.55', '172.25.130.56', '172.25.130.57', '172.25.130.58', '172.25.130.59', '172.25.130.60', '172.25.130.61', '172.25.130.62', '172.25.130.63', '172.25.130.64', '172.25.130.65', '172.25.130.66', '172.25.130.67', '172.25.130.68', '172.25.130.69', '172.25.130.70', '172.25.130.71', '172.25.130.72', '172.25.130.73', '172.25.130.74', '172.25.130.75', '172.25.130.76', '172.25.130.77', '172.25.130.78', '172.25.130.79', '172.25.130.80', '172.25.130.81', '172.25.130.82', '172.25.130.83', '172.25.130.84', '172.25.130.85', '172.25.130.86', '172.25.130.87', '172.25.130.88', '172.25.130.89', '172.25.130.90', '172.25.130.91', '172.25.130.92', '172.25.130.93', '172.25.130.94', '172.25.130.95', '172.25.130.96', '172.25.130.97', '172.25.130.98', '172.25.130.99', '172.25.130.100', '172.25.130.101', '172.25.130.102', '172.25.130.103', '172.25.130.104', '172.25.130.105', '172.25.130.106', '172.25.130.107', '172.25.130.108', '172.25.130.109', '172.25.130.110', '172.25.130.111', '172.25.130.112', '172.25.130.113', '172.25.130.114', '172.25.130.115', '172.25.130.116', '172.25.130.117', '172.25.130.118', '172.25.130.119', '172.25.130.120', '172.25.130.121', '172.25.130.122', '172.25.130.123', '172.25.130.124', '172.25.130.125', '172.25.130.126', '172.25.130.127', '172.25.130.128', '172.25.130.129', '172.25.130.130', '172.25.130.131', '172.25.130.132', '172.25.130.133', '172.25.130.134', '172.25.130.135', '172.25.130.136', '172.25.130.137', '172.25.130.138', '172.25.130.139', '172.25.130.140', '172.25.130.141', '172.25.130.142', '172.25.130.143', '172.25.130.144', '172.25.130.145', '172.25.130.146', '172.25.130.147', '172.25.130.148', '172.25.130.149', '172.25.130.150', '172.25.130.151', '172.25.130.152', '172.25.130.153', '172.25.130.154', '172.25.130.155', '172.25.130.156', '172.25.130.157', '172.25.130.158', '172.25.130.159', '172.25.130.160', '172.25.130.161', '172.25.130.162', '172.25.130.163', '172.25.130.164', '172.25.130.165', '172.25.130.166', '172.25.130.167', '172.25.130.168', '172.25.130.169', '172.25.130.170', '172.25.130.171', '172.25.130.172', '172.25.130.173', '172.25.130.174', '172.25.130.175', '172.25.130.176', '172.25.130.177', '172.25.130.178', '172.25.130.179', '172.25.130.180', '172.25.130.181', '172.25.130.182', '172.25.130.183', '172.25.130.184', '172.25.130.185', '172.25.130.186', '172.25.130.187', '172.25.130.188', '172.25.130.189', '172.25.130.190', '172.25.130.191', '172.25.130.192', '172.25.130.193', '172.25.130.194', '172.25.130.195', '172.25.130.196', '172.25.130.197', '172.25.130.198', '172.25.130.199', '172.25.130.200', '172.25.130.201', '172.25.130.202', '172.25.130.203', '172.25.130.204', '172.25.130.205', '172.25.130.206', '172.25.130.207', '172.25.130.208', '172.25.130.209', '172.25.130.210', '172.25.130.211', '172.25.130.212', '172.25.130.213', '172.25.130.214', '172.25.130.215', '172.25.130.216', '172.25.130.217', '172.25.130.218', '172.25.130.219', '172.25.130.220', '172.25.130.221', '172.25.130.222', '172.25.130.223', '172.25.130.224', '172.25.130.225', '172.25.130.226', '172.25.130.227', '172.25.130.228', '172.25.130.229', '172.25.130.230', '172.25.130.231', '172.25.130.232', '172.25.130.233', '172.25.130.234', '172.25.130.235', '172.25.130.236', '172.25.130.237', '172.25.130.238', '172.25.130.239', '172.25.130.240', '172.25.130.241', '172.25.130.242', '172.25.130.243', '172.25.130.244', '172.25.130.245', '172.25.130.246', '172.25.130.247', '172.25.130.248', '172.25.130.249', '172.25.130.250', '172.25.130.251', '172.25.130.252', '172.25.130.253', '172.25.130.254']
#dominio = '.medsenior.corp'

driver.get('http://' + ip + '/tactiumvoip/ipmonitor')

driver.find_element_by_id('username').send_keys(login)
driver.find_element_by_id('password').send_keys(senha)
driver.find_element_by_id('LoginControl_LoginButton').send_keys(Keys.ENTER)

time.sleep(1)
alerta = driver.switch_to.alert
alerta.accept()

for i in range(0, len(ramais)):
    # link para criação de ramais
    driver.get('http://' + ip + '/TactiumVoip/IPMonitor/Register/Station/New')
    driver.find_element_by_xpath('//*[@id="_006"]').send_keys(ramais[i])
    driver.find_element_by_xpath('//*[@id="_007"]').send_keys(ramais[i])
    driver.find_element_by_xpath('//*[@id="_008"]').send_keys(ramais[i])
    driver.find_element_by_xpath('//*[@id="_009_true"]').click()
    driver.find_element_by_xpath('//*[@id="__003_h1"]/a/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="_011_lft"]/option[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="_011_mar"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="_001_save"]').send_keys(Keys.ENTER)
    time.sleep(2)
    print("created: " + ramais[i])
