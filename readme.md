# Outlook Email Generator

This Python script automates the process of creating Outlook email accounts using Selenium.

## Description

This script navigates to the Outlook sign-up page, fills in the required information such as email, password, first name, last name, birthdate, and then creates the Outlook email accounts automatically.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies using pip: `pip install -r requirements.txt`
4. Download and install Chrome WebDriver: [Chrome WebDriver Downloads](https://chromedriver.chromium.org/)


## Usage

1. Run the script `main.py`:
2. The script will open a Chrome browser window and start creating Outlook email accounts automatically.
3. After completion, the email and password used for each account will be saved in `accounts.txt`.

## Notes

Outlook may ask for phone number verification after generating a few accounts. The script doesn't support this yet, but i'm working on a solution.

---

**By Overlookk**
