from selenium import webdriver
option = webdriver.ChromeOptions()
# option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=option)
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSd53vnmBmug3PMOf2knxGaCVhlnlQqoV9TmCu3ASqlHa_sjUA/viewform')


radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
radio_buttons[2].click() # Section-C

for i in range(5,760,4):  
    radio_buttons[i].click() # feedbacks (good)

# browser.find_elements_by_class_name("quantumWizTextinputPapertextareaMainContent exportContent")[0].send_keys(".")
# browser.find_elements_by_class_name("quantumWizTextinputPapertextareaEl modeLight freebirdFormviewerComponentsQuestionTextLong freebirdFormviewerComponentsQuestionTextTextInput freebirdThemedInput")[0].send_keys("..")
# browser.find_elements_by_class_name("quantumWizTextinputPapertextareaMainContent exportContent")[0].send_keys("...")
# browser.find_elements_by_class_name("m2")[0].send_keys("....")
