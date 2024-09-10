from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to the page
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Switch to English
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]")))
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait for the bigCookie element to be present
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "bigCookie")))

cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()
    # Extract cookies count and convert it to integer
    cookies_count_text = driver.find_element(By.ID, 'cookies').text.split(" ")[0].replace(",", "")
    cookies_count = int(cookies_count_text) if cookies_count_text.isdigit() else 0
    
    print(cookies_count)

    # Check each product price and purchase if possible
    for i in range(4):
        product_price_element = driver.find_element(By.ID, f"productPrice{i}")
        product_price = product_price_element.text
        
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        if cookies_count >= product_price:
            product_button = driver.find_element(By.ID, f"product{i}")
            
            # Attempt to scroll to the element
            actions = ActionChains(driver)
            actions.move_to_element(product_button).perform()
            
            # Wait for the element to be clickable
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, f"product{i}")))
            
            # If still not clickable, use JavaScript to force the click
            try:
                product_button.click()
            except Exception as e:
                print(f"Failed to click product {i}: {str(e)}")
                driver.execute_script("arguments[0].click();", product_button)    
            break
