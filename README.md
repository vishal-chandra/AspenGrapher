# AspenGrapher
An application to track grades posted on Follett Aspen over a period of time

# Install Dependencies
1. `pip install pandas`
2. `pip install selenium`

3. In order for selenium to be able to control Chrome programmatically, the ChromeDriver driver is required. It is available [here](https://chromedriver.storage.googleapis.com/index.html?path=2.44/).
4. Extract the contents of the .zip file and place them into `usr/local/bin` on mac/linux or add the path to the file to PATH on windows
5. In scraper.py, replace `os.getenv('ASPEN_USERNAME')` and `os.getenv('ASPEN_PASSWORD')` with your Aspen username and password, respectively. *
6. That's it! The dependencies are fully installed!

\*Alternatively to step 5, two bash/cmd environment variables named ASPEN_USERNAME and ASPEN_PASSWORD sontaining the account credentials can be set to avoid directly writing them into the code.
