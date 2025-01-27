from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# LinkedIn Credentials
ACCOUNT_EMAIL = "your_email_address"  # Replace with your email
ACCOUNT_PASSWORD = "your_password"  # Replace with your password

# Chrome Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')  # Uncomment for headless mode

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

def close_blocking_modal():
    """Closes any modal overlay blocking the screen."""
    try:
        blocking_modal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "artdeco-modal__dismiss")))
        blocking_modal.click()
        time.sleep(2)
        print("Closed blocking modal.")
    except:
        print("No blocking modal found.")

try:
    # Open LinkedIn Login Page
    driver.get("https://www.linkedin.com/login")

    # Login to LinkedIn
    email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)

    # Wait for redirect to LinkedIn feed
    time.sleep(5)

    # Navigate to the jobs page
    driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=Cloud%20Engineer&location=usa")
    time.sleep(5)

    # Start applying to jobs
    page = 1
    while page < 3:  # Adjust the number of pages to scrape
        print(f"Processing page {page}...")

        # Get list of job cards
        jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
        for job in jobs_list:
            try:
                # Scroll to the job element
                driver.execute_script("arguments[0].scrollIntoView(true);", job)
                time.sleep(1)
                job.click()
                time.sleep(3)

                # Check for "Easy Apply" button
                apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card")
                if apply_button.text == "Easy Apply":
                    apply_button.click()
                    time.sleep(3)

                    # Submit the application
                    try:
                        submit_button = wait.until(EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, "button[aria-label='Submit application']")
                        ))
                        submit_button.click()
                        time.sleep(2)
                        print("Application submitted successfully!")
                    except:
                        print("Could not submit application. Closing modal if present...")
                        close_blocking_modal()
                else:
                    print("No Easy Apply button for this job.")
            except Exception as e:
                print("Error processing job:", e)
                close_blocking_modal()
                continue

        # Go to the next page
        try:
            next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@aria-label='Page {page + 1}']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
            next_page_button.click()
            time.sleep(5)
            page += 1
        except Exception as e:
            print("No more pages or error navigating:", e)
            break

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
    print("Script completed.")
