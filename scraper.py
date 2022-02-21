## importing libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from os import path, mkdir
from bs4 import BeautifulSoup
import pandas as pd

position = "ruby on rails"
local = "remote"

position = position.replace(' ', "%20")

# select web driver file
def get_driver() -> webdriver.Firefox:
    return webdriver.Firefox(executable_path=path.abspath(path.join(
        path.dirname(__file__), "geckodriver")))

def visit_linkedin_jobs(d: webdriver.Firefox) -> None:
    d.get(f"https://www.linkedin.com/jobs/search/?geoId=103644278&keywords={position}&location={local}")


def gather_jobs():
    disc_list = []
    for page in range(1,41):
        ## click button to change the job list
        get_driver().find_element_by_xpath(f'//button[@aria-label="Page {page}"]').click()
        ## each page show us some jobs, inconsistent number
        jobs_lists = get_driver().find_element_by_class_name('jobs-search-results__list') #here we create a list with jobs
        jobs = jobs_lists.find_elements_by_class_name('jobs-search-results__list-item')#here we select each job to count
        ## waiting load
        time.sleep(1) 
        ## the loop below is for the algorithm to click exactly on the number of jobs that are shown in list
        ## in order to avoid errors that will stop the automation
        for job in range (1, len(jobs)+1):
            ## job click
            get_driver().find_element_by_xpath(f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{job}]/div/div/div[1]/div[2]/div[1]/a').click()
            ## waiting load 
            time.sleep(1)
            ## select job description
            job_desc = get_driver().find_element_by_class_name('jobs-search__right-rail')
            #get text
            soup = BeautifulSoup(job_desc.get_attribute('outerHTML'), 'html.parser')
            ## add text to list
            disc_list.append(soup.text)


def main() -> None:
    with get_driver() as d:
        print("visiting linkedin jobs")
        visit_linkedin_jobs(d)
        time.sleep(2)
        gather_jobs()


if __name__ == "__main__":
    main()