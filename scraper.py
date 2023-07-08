## second scenario where the query lands directly on results page without pressing the submit button and 
## there is no data found 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# Create an instance of the WebDriver (e.g., using ChromeDriver)
driver = webdriver.Chrome()
# Load the webpage; you may want to automate this by providing required values for the url and call this in a recursive manner
# driver.get('http://wintervar.wglab.org/results.pos.php?queryType=position&chr=1&pos=881918&ref=G&alt=A&build=hg19')
driver.get('http://wintervar.wglab.org/results.pos.php?queryType=position&chr=1&pos=1669648&ref=CT&alt=&build=hg19')
# Find the submit button
submit_button = driver.find_elements(By.CSS_SELECTOR, 'input[name=".submit"]')
if submit_button:
    # Click the submit button
    submit_button[0].click()
    # Wait for the table data to load
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
else:
    # Check if there is data available for the query
    no_data_element = driver.find_elements(By.XPATH, '//td[@class="dataTables_empty" and text()="No data available in table"]')
    if no_data_element:
        print("No data available in table.")
        driver.quit()
        exit()
    else:
        # Get the HTML source without form submission
        html_source = driver.page_source
        # Extract the table data using BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')
        table = soup.find('table')
if table:
    table_soup = BeautifulSoup(table.get_attribute('innerHTML'), 'html.parser')  # Convert the table WebElement to BeautifulSoup object
    rows = table_soup.find_all('tr')
    # Extract the data from each row
    table_data = []
    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        table_data.append(row_data)
    # Print the table data
    for row_data in table_data:
        print(row_data)
else:
    print("No table found.")
# Close the browser
driver.quit()