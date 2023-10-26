import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time
from datetime import date, timedelta

load_dotenv()
user=os.getenv('USER')
password=os.getenv('PASSWORD')

def main():
    driver = webdriver.Chrome()
    url='https://aimharder.com/login'
    driver.get(url)

    username = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID, 'mail')))
    username.clear()
    username.send_keys(user)

    userpass = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.ID, 'pw')))
    userpass.clear()
    userpass.send_keys(password)

    reservas_url = 'https://project96.aimharder.com/schedule'
    driver.get(reservas_url)

    today=date.today()
    offset=timedelta(days=2)
    fecha_reserva=today+offset

    fecha_reserva_str=str(fecha_reserva.day)+'/'+str(fecha_reserva.month)+'/'+str(fecha_reserva.year)+'\n'
    fecha_reserva_str

    select_day = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID, 'selw')))
    select_day.clear()
    select_day.send_keys(fecha_reserva_str)

    book_botton = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, '(//a[text()="Reservar"])[1]')))
    book_botton.click()
    
    time.sleep(3)
    driver.close()

if __name__ == '__main__':
    main()