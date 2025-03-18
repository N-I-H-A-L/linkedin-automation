from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import pandas as pd
import os

# Load Excel File
file_path = "companies.xlsx"  # Update with your file name
start_row = 41  # Specify the row number to start from (0-based index)
row_limit = 10  # Set limit for number of rows to process per session

df = pd.read_excel(file_path)
print(df.columns)

companies = df["Startup Name"].dropna().tolist()[start_row:start_row + row_limit]

# LinkedIn Credentials
LINKEDIN_EMAIL = "nihalkumar9749@gmail.com"  # Update with your email
LINKEDIN_PASSWORD = "Nihal@9749"  # Update with your password

# Set up Selenium WebDriver
driver_path = os.path.join(os.getcwd(), "chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get("https://www.linkedin.com/login")
time.sleep(random.uniform(3, 6))  # Random delay

# Log in to LinkedIn
driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
time.sleep(random.uniform(1, 3))  # Human-like delay
driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD, Keys.RETURN)
time.sleep(random.uniform(5, 8))  # Random delay to simulate loading

# Function to follow a company
def follow_company(company_name):
    search_url = f"https://www.linkedin.com/search/results/companies/?keywords={company_name}&origin=GLOBAL_SEARCH_HEADER&sid="
    driver.get(search_url)
    print(f"Opened 'Companies' tab for {company_name}")
    time.sleep(10)

def connect_with_recruiters(company_name):
    search_queries = ["HR", "Recruiter", "Talent Acquisition"]
    for query in search_queries:
        search_url = f"https://www.linkedin.com/search/results/people/?keywords={company_name} {query}&origin=GLOBAL_SEARCH_HEADER&sid="
        driver.get(search_url)
        print(f"Opened 'People' tab for {query} at {company_name}")
        time.sleep(10)  # Wait for search results

# Loop through companies and follow them
for company in companies:
    follow_company(company)
    connect_with_recruiters(company)
    # Introduce session break to avoid detection
    if random.random() < 0.1:  # 10% chance of taking a longer break
        print("Taking a short break of 3 to 6 seconds to avoid detection...")
        time.sleep(random.uniform(3, 6))

# Implement session breaks
print("Session completed. Restart after 10-15 minutes to avoid detection.")
