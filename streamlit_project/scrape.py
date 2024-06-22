from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

def scrape_website(url):
    try:
        options = ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode, no GUI
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)

        # Wait for the page to fully render (adjust wait time as needed)
        driver.implicitly_wait(10)

        # Extract all visible text from the page
        text_content = driver.find_elements()

        return text_content.strip()  # Strip leading and trailing whitespace

    finally:
        driver.quit()
