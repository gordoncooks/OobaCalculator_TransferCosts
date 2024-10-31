import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class OobaCalculator:
    def __init__(self, headless=True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)

    def open_calculator(self):
        self.driver.get("https://www.ooba.co.za/home-loan/transfer-cost-calculator/")
        time.sleep(5)  # Wait for page to load completely

    def set_input_value(self, element_id, value):
        try:
            input_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            input_field.clear()
            time.sleep(1)
            input_field.send_keys(value)
        except Exception as e:
            print(f"Error setting value for {element_id}: {e}")

    def select_dropdown_value(self, element_id, option_text):
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            dropdown.click()
            time.sleep(1)
            option = self.driver.find_element(By.XPATH, f"//option[text()='{option_text}']")
            option.click()
            time.sleep(1)
        except Exception as e:
            print(f"Error selecting dropdown option for {element_id}: {e}")

    def submit_ooba(self):
        try:
            calculate_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Calculate') and not(contains(@class, 'disabled'))]"))
            )
            self.driver.execute_script("arguments[0].click();", calculate_button)
        except Exception as e:
            print("Error clicking the Calculate button:", e)

    def get_value_by_id(self, element_id):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            return element.text
        except Exception as e:
            print(f"Error retrieving value for {element_id}: {e}")
            return None

    def calculate_transfer_costs(self, purchase_price, loan_amount, property_type, vat_registered, purchaser_status, retries=3):
        for attempt in range(retries):
            self.open_calculator()

            try:
                # Set input values
                self.set_input_value('input_9_1', purchase_price)
                self.set_input_value('input_9_2', loan_amount)
                self.select_dropdown_value('input_9_3', property_type)
                self.select_dropdown_value('input_9_4', vat_registered)
                self.select_dropdown_value('input_9_5', purchaser_status)

                # Click Calculate
                self.submit_ooba()

                # Wait and attempt to retrieve the total cost
                time.sleep(5)
                total_cost = self.get_value_by_id('totalTransferCosts')
                
                if total_cost and total_cost != "R 0":
                    print("Total Transfer Costs:", total_cost)
                    return total_cost  # Exit loop if a valid result is found
                else:
                    print(f"Attempt {attempt + 1} failed. Retrying...")
            except Exception as e:
                print(f"An error occurred during attempt {attempt + 1}: {e}")
            finally:
                self.driver.quit()

            if attempt == retries - 1 and (not total_cost or total_cost == "R 0"):
                print("Error: Could not retrieve the total transfer costs. Please check the inputs or try again.")
                return None

