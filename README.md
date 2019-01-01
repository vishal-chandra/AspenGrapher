# AspenGrapher
An application to track grades posted on Follett Aspen over a period of time. <br />
## How It Works
* AspenGrapher scrapes the Aspen webpage periodically using a set of given login information to collect data. 
* A graph can be created from the collected data at any time and stored as a png image
## Example Output
<img src="gradePlot.png" width=800>

# Install Dependencies
1. `git clone https://github.com/vishal-chandra/AspenGrapher`
2. `cd AspenGrapher`
3. `pip install -r requirements.txt`

# Defining Credentials
## Simple Usage
In scraper.py, replace `os.getenv('ASPEN_USERNAME')` and `os.getenv('ASPEN_PASSWORD')` with your Aspen username and password, respectively. 

## If Contributing
These methods avoid writing the login information into the code so they never appear on GitHub
1. Two bash/cmd environment variables named `ASPEN_USERNAME` and `ASPEN_PASSWORD` containing the account username and password, respectively, can be created. Scraper.py is already setup to handle this

2. Alternatively, a text file called credentials.txt containing the login information can be added to the project folder. Scraper.py has to be modified to read the credentials from this file. "credentials.txt" has already been added to .gitignore

# Chrome WebDriver
Selenium uses Chrome to navigate and login to Apsen. For it to be able to control Chrome, a driver in the form of a binary executable is needed. 

## Troubleshooting
Drivers for both Mac and Windows are provided in the chromedriver folder. If there is a problem or error, the drivers are available [here](https://chromedriver.storage.googleapis.com/index.html?path=2.44/). Extract the executable from the .zip file and place it into the [chromedriver](chromedriver) folder. Then update the file name in [scraper.py](Python/scraper.py) line 20 or 22 (depending on OS).
