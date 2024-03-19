import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def generate_random_string(length):
    first_char = random.choice(string.ascii_letters)  # Ensure email starts with a letter
    return first_char + ''.join(random.choices(string.ascii_letters + string.digits, k=length - 1))

def create_outlook_account():
    try:
        # Start a new instance of Chrome browser
        driver = webdriver.Chrome()
        
        # Open the Outlook sign-up page
        driver.get("https://signup.live.com/")
        
        # Wait for the email field to appear
        email_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='MemberName']")))
        
        # Generate a random email address
        email = generate_random_string(10) + "@outlook.com"
        email_input.send_keys(email)
        
        # Click "Next" button
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='iSignupAction']")))
        next_button.click()
        
        # Wait for the password field to appear
        password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='PasswordInput']")))
        
        # Generate a random password
        password = generate_random_string(10) + random.choice("!@#$%^&*()")
        password_input.send_keys(password)
        
        # Click "Next" button
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='iSignupAction']")))
        next_button.click()
        
        # Wait for the page to navigate to the next step
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='FirstName']")))
        
        # Generate random first and last names
        first_name = generate_random_string(6)
        last_name = generate_random_string(6)
        
        # Fill in the first name field
        first_name_input = driver.find_element(By.XPATH, "//input[@id='FirstName']")
        first_name_input.send_keys(first_name)
        
        # Fill in the last name field
        last_name_input = driver.find_element(By.XPATH, "//input[@id='LastName']")
        last_name_input.send_keys(last_name)
        
        # Click "Next" button
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='iSignupAction']")))
        next_button.click()
        
        # Wait for the birth date fields to appear
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@id='BirthMonth']")))
        
        # Select random birth month
        birth_month_input = Select(driver.find_element(By.XPATH, "//select[@id='BirthMonth']"))
        birth_month_input.select_by_index(random.randint(1, 12))
        
        # Select random birth day
        birth_day_input = Select(driver.find_element(By.XPATH, "//select[@id='BirthDay']"))
        birth_day_input.select_by_index(random.randint(1, 28))
        
        # Select random birth year
        birth_year_input = driver.find_element(By.XPATH, "//input[@id='BirthYear']")
        birth_year_input.send_keys(str(random.randint(1960, 2002)))  # Assuming users are between 18 and 60 years old
        
        # Click "Next" button
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='iSignupAction']")))
        next_button.click()
        
        # Wait for user to input CAPTCHA manually
        input("Please complete the CAPTCHA and press Enter to continue...")
        
        # Account created successfully, print email and password
        print("Account created successfully!")
        print("Email:", email)
        print("Password:", password)
        
    finally:
        # Close the browser window
        driver.quit()

# Call the function to create the Outlook account
create_outlook_account()
