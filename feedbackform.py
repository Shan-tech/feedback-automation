from selenium import webdriver
option = webdriver.ChromeOptions()

    # other utilities 
# option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path="<path>", options=option) #example: "C:\\chromedriver\\chromedriver.exe"
browser.get('<formLink>') # paste your form link here <formLink>


radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
# radio_buttons[2].click() # uncomment if u section is asked

for i in range(0,760,3):   # (start,end,review(0,1,2,3))
    radio_buttons[i].click() # feedbacks (good)



# use below code for other refs

# browser.find_elements_by_class_name("quantumWizTextinputPapertextareaMainContent exportContent")[0].send_keys(".")
# browser.find_elements_by_class_name("quantumWizTextinputPapertextareaEl modeLight freebirdFormviewerComponentsQuestionTextLong freebirdFormviewerComponentsQuestionTextTextInput freebirdThemedInput")[0].send_keys("..")
# browser.find_elements_by_class_name("quantumWizTextinputPapertextareaMainContent exportContent")[0].send_keys("...")
# browser.find_elements_by_class_name("m2")[0].send_keys("....")
