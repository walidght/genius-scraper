from selenium import webdriver

def create_a_webdriver():
    # Chrome Browser setup
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    return webdriver.Chrome(options=options)
