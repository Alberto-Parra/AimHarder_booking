import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time
from datetime import date, timedelta

#load from .env file the user and password
load_dotenv()

admin=os.getenv('ADMIN')
host=os.getenv('HOST')
password=os.getenv('PASSWORD')
user=admin+'@'+host+'.es'

def main():
    
    # open chrome windows
    driver = webdriver.Chrome()
    
    # login url
    url='https://aimharder.com/login'
    
    # go to this url
    driver.get(url)
    
    # Write the username
    username = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID, 'mail')))
    username.clear()
    username.send_keys(user)

    # Write the user password
    userpass = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID, 'pw')))
    userpass.clear()
    userpass.send_keys(password)
    
    login_botton = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.ID, "loginSubmit")))
    login_botton.click()
    
    # Ones you are logged you can go directly to another part directly using the url easier than doing some clicking.
    reservas_url = 'https://project96.aimharder.com/schedule'
    driver.get(reservas_url)
    

    # To book the spot in two day from now
    today=date.today()
    offset=timedelta(days=2)
    fecha_reserva=today+offset

    fecha_reserva_str=str(fecha_reserva.month)+'/'+str(fecha_reserva.day)+'/'+str(fecha_reserva.year)+'\n'

    # Write the date in the input
    select_day = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, 'selw')))
    select_day.clear()
    select_day.send_keys(fecha_reserva_str)

    # click in book class
    book_botton = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '(//a[text()="Book"])[1]')))
    book_botton.click()
    
    #Close the browser
    time.sleep(5)

    driver.close()

if __name__ == '__main__':
    main()