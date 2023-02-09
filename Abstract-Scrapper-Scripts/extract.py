from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
from selenium.webdriver.support.wait import WebDriverWait
import pandas



class ExtractData:
    def __init__(self, chromedriver_path):
        self.base_url = "https://www.webofscience.com"
        self.browser =  webdriver.Chrome(chromedriver_path)
        self.driver_path = chromedriver_path


    def extractURLsFromCSV(self,):
        csvURLDict = {}
        url_list = []

        pd = pandas.read_csv("./all_urls.csv", header = None)
        for row in pd.itertuples():
            if row[1] == 0:
                 url_list = []
            url_list.append(row[3])
            csvURLDict.update({row[2] : url_list})

        for key, value in csvURLDict.items():
            totalURLS = len(value)
            print (totalURLS)
            self.process_data(key, value)
            time.sleep(60)



    def process_data(self, kw, url_list): 
        count = 0
        first_time = True
        for url in url_list:

            if first_time is False and count % 500 == 0:
                browser1 = webdriver.Chrome(self.driver_path)
                try:
                    self.browser.quit()
                except:
                    continue
                print("Close and opened")
                time.sleep(60)
                self.browser = browser1

            self.browser.get(url)
            paragraph = ""
                
            try:
                element = WebDriverWait(self.browser, 10).until(lambda x: x.find_element(By.CLASS_NAME, "abstract--instance"))

                soup = BeautifulSoup(self.browser.page_source, features="html.parser")

                all_abstract = soup.find("div", class_="abstract--instance")
                
                if all_abstract is not None:
                    paragraph = all_abstract.find("p").get_text()

            except Exception as e:
                print("Exception occured for link  "+ url)
                self.browser.refresh()

            filename =  "MarineData/" + kw + "__data.csv"

            with open(filename, "a") as f:
                writer = csv.writer(f)
                row = [count, kw, url, paragraph]
                writer.writerow(row)
            count +=1
            first_time = False

        print("Total URL extracted "+ str(count))
        time.sleep(60)
        

class ExtractDataNLM:
    def __init__(self, chromedriver_path):
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov/"
        self.browser =  webdriver.Chrome(chromedriver_path)
        self.driver_path = chromedriver_path
        
    def extractURLsFromCSV(self,): 
        url_list = []

        pd = pandas.read_csv("nlm_urls.csv", header = None)
        for row in pd.itertuples():
            url_list.append(row[2])


        filename =  "nlmdata.txt"
        count = 1 
        with open(filename, "a") as f:
            for item in url_list:
                data = self.process_data(item)
                f.write(data)
                print(count)
                count+=1
    
            
    def process_data(self,item):
        self.browser.get(item)
        soup = BeautifulSoup(self.browser.page_source, features="html.parser")
        all_abstract = soup.find("div", id="enc-abstract")
        if all_abstract is not None:
            paragraph = ""
            all_elems = all_abstract.findAll('p')
            for elem in all_elems:
                paragraph += elem.get_text()
                return paragraph
            
        return ""
            
            
        
    
    