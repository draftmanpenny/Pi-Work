from packages import *


def indeed_search(): 
    driver.get(INDEED_URL)

for _ in range(25):
    driver.find_element(By. ID, "text-input-what").send_keys(Keys.BACKSPACE) # finds job search box and clears box
driver.find_element(By. ID, "text-input-what").send_keys('python') # inputs desired job 
driver.find_element(By. XPATH, "/html/body/div/div[2]/div/span/div[4]/div[1]/div/div/div/div/form/button").click() # searches for python jobs 
searches = driver.find_elements(By.CLASS_NAME, "resultContent") # finds all job listings through class name 
jobs = 0
for results in searches:
    results.click()
    time.sleep(2)
    print(f'Job Listing {jobs}\n ' + f'{driver.current_url}\n')
    jobs += 1
   
indeed_search()