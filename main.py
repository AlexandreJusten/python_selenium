from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("--log-level=3")
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")#filename="programa.log"

driver = webdriver.Chrome(options=options)

url = 'https://www.reddit.com/'

try:
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)
    logging.info("\033[92mconexao ✔\033[0m")
except:
    logging.error("\033[31mErro na conexao com :\033[0m"+url)
    driver.quit()
    quit()

def click_element(driver, locator, locator_type):
    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((locator_type, locator)))
        action.move_to_element(element).click().perform()
        return element
    except:
        logging.warning(f"\033[33mErro na navegação de página: [{locator}]\033[0m")

    return None

try:
    action = ActionChains(driver)

    menu_principal = click_element(driver, '/html/body/div[1]/div/div[2]/div[2]/div/div[1]', By.XPATH)
    menu_gaming = click_element(driver, 'Gaming', By.PARTIAL_LINK_TEXT)
    menu_valheim = click_element(driver, 'Valheim', By.PARTIAL_LINK_TEXT)
    sub_menu = click_element(driver, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/ul/li/a', By.XPATH)
    sub_menu_2 = click_element(driver, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[3]', By.XPATH)

    if menu_principal and menu_gaming and menu_valheim and sub_menu and sub_menu_2:
        logging.info("\033[92mNavegação de página ✔\033[0m")
        time.sleep(2)
    else:
        raise Exception('Busque pela primeira pagina onde ocorreu o warning')

except Exception as e:
    driver.quit()
    logging.error(f"\033[31mErro na navegação de página: {str(e)}\033[0m")
    quit()
    
try:
    span = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div[4]/div/div/div")))
    texto ="Buscas Relacionadas ao Tema escolhido:\n" + span.text

    with open('lista.csv', 'w') as arquivo:
        arquivo.write(texto + '\n')

    logging.info("\033[92mCSV gerado com sucesso ✔\033[0m")

except Exception as e:
    logging.error("\033[31mErro ao gerar CSV: {}\033[0m".format(e))
finally:
    driver.quit()
    logging.info("\033[92mAplicação finalizada com sucesso\033[0m")
