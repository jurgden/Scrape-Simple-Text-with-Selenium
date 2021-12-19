from selenium import webdriver
def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(options=options)
  driver.get('https://lolasrapidrelief.com/')
  return driver 

def main():
  driver = get_driver()
  element = driver.find_element(by='xpath', value='//*[@id="home-content"]/div[1]/div/div/div/h1')
  return element.text

print(main())