from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

from extract import ExtractData
import argparse

from extract import ExtractDataNLM


class GetAllUrl:
    def __init__(self, chromedriver_path):
        self.base_url = "https://www.webofscience.com"
        self.driver_path = chromedriver_path
        self.browser = webdriver.Chrome(chromedriver_path)
        self.keyword = [
                    "Enterococci in water",
                    "Fecal Coliform in water",
                    "E.coli in marine water",
                    "Fecal Indicator Bacteria in water",
                    "E coli in water",
                    "Water quality indicators",
                    "Enteric Viruses",
                    "Enteric infections from beaches",
                    "Gastrointestinal Illness and beaches",
                    "Beach water contamination",
                    "Beach outbreaks",
                    "Waterborne infections in divers",
                    "Marine water quality",
                    "Marine water point source pollution",
                    "Quantitative microbial risk assessment and water",
                    "Weather and waterborne illness",
                    "Non cholera vibrio outbreaks",
                    "Pfiesteria infection",
                    "Red tides and illness",
                    "Harmful algal blooms and illness",
                    "Coastal water pollution",
                    "Water salinity and illness",
                    "Water characteristics and illness",
                    "Tides and illness",
                    "Harmful algal blooms"
                ]

    def start_execution(self,):
        for kw in self.keyword:
            self.browser.get(self.base_url)
            all_list = []
            self.browser.find_element(By.CLASS_NAME,'search-criteria-input').clear()
            self.browser.find_element(By.CLASS_NAME,'search-criteria-input').send_keys(kw)
            self.browser.find_element(By.XPATH,'//*[@id="snSearchType"]/div[3]/button[2]').click()

            initial_list = self.get_all_list(all_list)

            final_list = self.browse_next(initial_list)  

            with open("./all_urls.csv", "a") as f:
                writer = csv.writer(f)
                for count, item in enumerate(final_list):
                    url = self.base_url.strip("/wos") + item
                    row = [count, kw, url]
                    writer.writerow(row)

            print("Completed Extracting "  + str(len(final_list)) + " URLs for keyword: " + kw)
            browser1 = webdriver.Chrome(self.driver_path)
            self.browser.close()
            self.browser = browser1

        self.browser.close()


    def get_all_list(self, all_list):
        time.sleep(1)
        # main_view_element = self.browser.find_element(By.CLASS_NAME, 'app-records-list') 
        # soup1 = BeautifulSoup(self.browser.page_source, features="html.parser")

        i=0
        screen_height=0

        while i < 60:
            last_height = screen_height + 250
            view_string = "window.scrollTo("+str(screen_height)+","+str(last_height)+");"
            screen_height = last_height
            self.browser.execute_script(view_string)
            i+=1
            time.sleep(0.5)

        soup = BeautifulSoup(self.browser.page_source, features="html.parser")
        # all_list_elem = soup.find_all('app-record', class_='summary-record')
        all_list_elem = soup.find_all('app-record', class_='ng-star-inserted')
        
        for app_record in all_list_elem:
            if app_record is not None:
                href = app_record.find('a', class_='title-link')
                if href is not None:
                    all_list.append(href['href'])

        
        return all_list


    def browse_next(self, initial_list):
        final_list = initial_list
        
        while True:
            soup = BeautifulSoup(self.browser.page_source, features="html.parser")
            # time.sleep(2)

            next_page = self.get_next_button(soup)

            if next_page is None:
                return final_list

            if next_page.has_attr('disabled'):
                return final_list

            br = self.browser.find_element(By.XPATH,'/html/body/app-wos/div/div/main/div/div[2]/app-input-route/app-base-summary-component/div/div[2]/app-page-controls[2]/div/form/div/button[2]')                      
            br.click()  


            final_list=self.get_all_list(final_list)  
            

        return final_list

    def get_next_button(self,soup):

        pagination = soup.find('form', class_='pagination')
        all_buttons = pagination.find_all("button")

        return all_buttons[1]



class GetAllUrlForNLM:
    def __init__(self, chromedriver_path):
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov/?term=35130250%2C35100291%2C35100286%2C34885995%2C34645205%2C34448447%2C34371498%2C34320325%2C34287139%2C34284731%2C33939640%2C33743461%2C33737138%2C33507414%2C33496568%2C33460591%2C33438270%2C33350905%2C33281180%2C33247174%2C33137355%2C33027395%2C32997302%2C32987220%2C32840201%2C32725238%2C32668449%2C32491991%2C32471315%2C32313241%2C32265107%2C32245368%2C32214051%2C32167443%2C32112764%2C31898795%2C31888648%2C31855546%2C31837131%2C31797948%2C31732569%2C31625494%2C31623064%2C31605719%2C31603704%2C31529936%2C31529800%2C31443180%2C31399406%2C31390693%2C31287787%2C31176815%2C31146052%2C31077047%2C31070186%2C30990401%2C30964378%2C30942147%2C30792073%2C30694184%2C30689681%2C30634384%2C30569747%2C30547836%2C30539332%2C30409377%2C30279488%2C30247141%2C30183924%2C30156489%2C30156488%2C30156487%2C30156484%2C30156483%2C30156482%2C30047566%2C30039783%2C30018195%2C29890477%2C29865180%2C29859076%2C29721700%2C29703737%2C29633676%2C29623595%2C29588168%2C29529201%2C29508021%2C29428708%2C29424714%2C29412314%2C29393885%2C29330866%2C29316937%2C29291431%2C29267998%2C29252921%2C29246779%2C29168450%2C29144111%2C29121003%2C29120997%2C29120153%2C29040071%2C29031605%2C29030321%2C29016318%2C29016282%2C28899309%2C28869189%2C28827123%2C28776228%2C28771145%2C28719263%2C28708249%2C28671394%2C28671392%2C28598348%2C28576344%2C28483382%2C28453115%2C28425935%2C28424879%2C28283139%2C28224339%2C28222687%2C28209895%2C28202928%2C28190399%2C28151442%2C28017547%2C27983508%2C27959880%2C27898017%2C27854250%2C27809855%2C27797430%2C27736832%2C27648572%2C27596699%2C27573124%2C27572176%2C27485898%2C27450612%2C27430075%2C27397728%2C27352014%2C27181600%2C27168147%2C27126201%2C27105418%2C27105415%2C27102426%2C27094662%2C27049709%2C27003679%2C26941243%2C26936670%2C26900118%2C26900116%2C26900113%2C26897410%2C26874764%2C26863429%2C26863428%2C26837828%2C26825320%2C26820849%2C26733222%2C26638676%2C26616307%2C26608766%2C26587825%2C26583383%2C26560984%2C26513152%2C26505897%2C26505552%2C26482884%2C26384128%2C26361286%2C26354212%2C26354207%2C26241039%2C26200373%2C26194500%2C26070525%2C26032379%2C26022715%2C25998249%2C25885050%2C25835810%2C25782677%2C25764059%2C25746238%2C25618192%2C25563349%2C25388662%2C25287632%2C24274064"
        self.driver_path = chromedriver_path
        self.browser = webdriver.Chrome(chromedriver_path)
        
    def start_execution(self,):
        all_list = []
        self.browser.get(self.base_url)
        time.sleep(0.5)
        
        initial_list = self.get_all_list(all_list)
        final_list = self.browse_next(initial_list)
        
        website_url = "https://pubmed.ncbi.nlm.nih.gov/"
        with open("nlm_urls.csv", "a") as f:
            writer = csv.writer(f)
            for count, item in enumerate(final_list):
                url = website_url + item
                row = [count, url]
                writer.writerow(row)

            print("Completed Extracting "  + str(len(final_list)) + " URLs")

        self.browser.close()
        
        
    def get_all_list(self,all_list):
        soup = BeautifulSoup(self.browser.page_source, features="html.parser")
        
        all_list_elem = soup.find_all('a', class_='docsum-title')
        for alink in all_list_elem:
            if alink is not None:
                all_list.append(alink['href'])
        
        return all_list

    def browse_next(self, initial_list):  
        final_list = initial_list
        
        while True:
            soup = BeautifulSoup(self.browser.page_source, features="html.parser")

            next_page = self.get_next_button(soup)

            if next_page is None:
                return final_list

            if next_page.has_attr('disabled'):
                return final_list

            br = self.browser.find_element(By.XPATH,'/html/body/main/div[9]/div[2]/div[2]/div[2]/button[3]')                      
            br.click()  


            final_list=self.get_all_list(final_list)  
            

        return final_list

    def get_next_button(self,soup):

        pagination = soup.find('div', class_='top-pagination')
        all_buttons = pagination.find_all("button")

        return all_buttons[2]
        
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("driverpath", help="Full path of your downloaded chrome webdriver.")
    args = parser.parse_args()
    chromedriver_path = args.driverpath
   
    #Extracts abstracts from Web of Science
    GetAllUrl(chromedriver_path).start_execution()
    ExtractData(chromedriver_path).extractURLsFromCSV()
    
    #Comment the above functions and uncomment the below functions if you wish to extract abstracts from National Library of Medicine
    # GetAllUrlForNLM(chromedriver_path).start_execution()
    # ExtractDataNLM(chromedriver_path).extractURLsFromCSV()
    











