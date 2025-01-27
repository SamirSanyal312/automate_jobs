LinkedIn Job Application Automation
Automate the job application process on LinkedIn using Selenium. This tool logs in, searches for jobs with the "Easy Apply" feature, and submits applications for roles based on specified keywords and locations.

Features
🔐 Automated Login: Logs into LinkedIn using your credentials securely.
🔍 Job Search: Searches for jobs based on keywords and location.
⚡ Easy Apply Automation: Applies to jobs that support the "Easy Apply" feature.
🌐 Pagination Support: Navigates through multiple job listing pages.
🛠️ Error Handling: Manages modals, overlays, and other dynamic content.
Technologies Used
Python: Core programming language.
Selenium: For browser automation.
ChromeDriver: Driver for interacting with the Chrome browser.
Prerequisites
Ensure the following are installed and set up on your system:

Python 3.x: Download Python
Google Chrome Browser: Download Chrome
ChromeDriver:
Download the driver matching your Chrome version from ChromeDriver Downloads.
Place the chromedriver executable in the project directory.
Install Selenium:
bash
Copy
Edit
pip install selenium
Setup Instructions
Follow these steps to set up and run the project:

Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/LinkedIn-Automation.git
cd LinkedIn-Automation
Install Dependencies: Install the required Python packages:

bash
Copy
Edit
pip install selenium
Download ChromeDriver:

Download ChromeDriver compatible with your browser version.
Place it in the project directory or update the PATH environment variable.
Update Credentials: Open the script file (e.g., linkedin_automation.py) and replace the placeholders:

python
Copy
Edit
ACCOUNT_EMAIL = "your_email@example.com"
ACCOUNT_PASSWORD = "your_password"
Run the Script: Execute the script using Python:

bash
Copy
Edit
python linkedin_automation.py
Customizing the Script
Modify Job Search Keywords and Location:
Update the URL in the script to change the job search query:

python
Copy
Edit
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=Software%20Engineer&location=USA")
Adjust Wait Times:
Increase or decrease time.sleep() values or explicit wait durations if elements fail to load or timeout.

Usage
The script will:

Log into LinkedIn.
Navigate to the jobs section.
Search for jobs based on the specified keywords and location.
Apply to jobs with the "Easy Apply" button.
Monitor the terminal for:

Application progress.
Any errors or skipped applications.
Known Issues
⚠️ CAPTCHA
LinkedIn may present a CAPTCHA challenge during login. Manual intervention is required to resolve this.
🔄 Dynamic Content
Some elements may load slowly. Adjust wait times in the script if necessary.
🛑 Modal Dialogs
Blocking modals, such as "Discard Confirmation," may prevent clicks. The script includes logic to handle these cases, but manual handling might still be required occasionally.
Contributing
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as you include the original license.

Disclaimer
This script is for educational purposes only.
Using automation on LinkedIn may violate their Terms of Service. Proceed at your own risk.
