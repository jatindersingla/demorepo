from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
while True:
#  Q1.What is the date of your parent`s wedding anniversary? 
    chromeOptions = webdriver.ChromeOptions()
    current_directory = os.path.dirname(os.path.abspath(__file__))

    cservice = Service(r'chromedriver.exe')
    chromeOptions.add_experimental_option('prefs', {
        "download.default_directory": current_directory,  # Change default directory for downloads
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        # "safebrowsing.enabled": True  # To enable safe browsing
    })
    chromeOptions.add_argument('--log-level=1')
    driver = webdriver.Chrome(service=cservice,options=chromeOptions)
    action = ActionChains(driver)
    import time
    driver.get('https://omni.axisbank.co.in/axisretailbanking/')
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(60)
    
    search_bar = driver.find_element(By.XPATH, "//*[@id='custid']")
    search_bar.send_keys("964616190")
    
    driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("Axi@1981")
    
    driver.find_element(By.XPATH,"//*[@id='APLOGIN']").click()
    
    if(len(driver.find_elements(By.XPATH,"//div[contains(text(),'color of your spouse`s eyes')]"))!=0 and driver.find_element(By.XPATH,"//div[contains(text(),'color of your spouse`s eyes')]").is_displayed()):
        driver.find_element(By.XPATH,"//div[contains(text(),'color of your spouse`s eyes')]//input").send_keys("Black")
        driver.find_element(By.XPATH,"//*[contains(text(),'CONFIRM')]").click()
        print("color of your spouse`s eyes")
    elif(len(driver.find_elements(By.XPATH,"//div[contains(text(),'age when you got married')]"))!=0 and driver.find_element(By.XPATH,"//div[contains(text(),'age when you got married')]").is_displayed()):
        driver.find_element(By.XPATH,"//div[contains(text(),'age when you got married')]//input").send_keys("2005")
        driver.find_element(By.XPATH,"//*[contains(text(),'CONFIRM')]").click()
        print("age when you got married")

    elif(len(driver.find_elements(By.XPATH,"//div[contains(text(),' Q1.What is the date of your parent`s wedding anniversary? ')]"))!=0 and driver.find_element(By.XPATH,"//div[contains(text(),' Q1.What is the date of your parent`s wedding anniversary? ')]").is_displayed()):
        driver.find_element(By.XPATH,"//div[contains(text(),' Q1.What is the date of your parent`s wedding anniversary? ')]//input").send_keys("Tommy")
        driver.find_element(By.XPATH,"//*[contains(text(),'CONFIRM')]").click()

    else:
        pass 
    print("Security questions answered")
    time.sleep(5)
    print("Login Successful")
    try:
        action.move_to_element(driver.find_element(By.XPATH,"//*[text()='No thanks']")).click().perform()
        print("No thanks clicked")
        time.sleep(10)
    except:
        pass
    driver.implicitly_wait(60)
    driver.set_page_load_timeout(60)
    driver.find_element(By.XPATH,"//*[contains(text(),'ACCOUNTS')]").click()
    print("Accounts clicked")
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH,"//*[@id='1edit_nick']").click()
    driver.set_page_load_timeout(60)
    driver.find_element(By.XPATH,"(//div//span//span[text()='Select'])[1]").click()
    driver.find_element(By.XPATH,"//span[contains(text(),'CSV')]").click()
    driver.find_element(By.XPATH,"(//a[text()=' GO '])[1]").click()
    while True:
        try:

            driver.find_element(By.XPATH,"//*[contains(text(),'LAST 10 TRANSACTIONS')]").click()
            time.sleep(4)
            driver.find_element(By.XPATH,"//*[contains(text(),'STATEMENTS')]").click()
            time.sleep(4)
            driver.find_element(By.XPATH,"//*[contains(text(),'LAST 10 TRANSACTIONS')]").click()
            driver.find_element(By.XPATH,"(//div//span//span[text()='Select'])[1]").click()
            driver.find_element(By.XPATH,"//span[contains(text(),'CSV')]").click()
            driver.find_element(By.XPATH,"(//a[text()=' GO '])[1]").click()

            time.sleep(10)
        except:
            driver.quit()
            break

        try:
            import os
            import pandas as pd
            # Get list of files in the current directory
            files = os.listdir('.')
            print(files)
            # Filter for CSV files
            csv_files = [file for file in files if file.endswith('.csv')]
            # Get the latest CSV file based on modification time
            latest_csv_file = max(csv_files, key=os.path.getmtime)
            print(latest_csv_file)
            # Rename the CSV file with current datetime
            import datetime
            new_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
            os.rename(latest_csv_file, new_filename)
            print("CSV file renamed to:", new_filename)

            df = pd.read_csv(new_filename)
            # Rest of the code...
            # print(latest_csv_file)
            # df=pd.read_csv(latest_csv_file)
            df.drop(df.index[0:4],inplace=True)
            df.drop(columns=["Unnamed: 0","Unnamed: 1"],axis=1,inplace=True)
            df.rename(columns=df.iloc[0], inplace = True)
            df.drop(df.index[0], inplace = True)
            date=df["Date"][0:10]
            discription=df["Description"][0:10]
            Transactional_Amount = df["Transactional Amount"][0:10]
            date_list = date.tolist()
            discription_list = discription.tolist()
            transactional_amount_list = Transactional_Amount.tolist()
            print(type(date_list))
            print(type(discription_list))
            print(type(transactional_amount_list))
            apilist=[]
            for i in range(len(date_list)):
                print(date_list[i])
                print(discription_list[i])
                print(transactional_amount_list[i])
                apilist.append({"sms_text":f"{date_list[i]} {discription_list[i]} {transactional_amount_list[i]}","sms_sender":"AxisBank"})
            print(apilist)
            import requests
            import os
            url = "https://api.kismapay.com/v1/rowscript/insertrowscript"
            response = requests.post(url, json=apilist)
            print(response.status_code)
            print(response.text)
            time.sleep(4)
            # Get list of files in the current directory
            files = os.listdir('.')
            # Filter for CSV files
            csv_files = [file for file in files if file.endswith('.csv')]
            # Sort the CSV files based on modification time
            csv_files.sort(key=os.path.getmtime, reverse=True)

            # Check if there are at least two CSV files
            if len(csv_files) >= 2:
                # Get the second latest CSV file
                second_latest_csv_file = csv_files[1]
                # Delete the second latest CSV file
                os.remove(second_latest_csv_file)
                print("Deleted second latest CSV file:", second_latest_csv_file)
            else:
                print("There are not enough CSV files to delete the second latest one")
        except:
            driver.quit()
            break
    time.sleep(50)