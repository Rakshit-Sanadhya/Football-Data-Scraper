# Football-Data-Scraper
This Python program scrapes player data from the football data website fbref.com.
This code uses Selenium to automate a browser, BeautifulSoup to parse HTML content, and pandas to process and save data.
The goal is to scrape player statistics tables from a list of URLs on FBref and save each table as a separate Excel file.

The programme will produce 6 excel files, for standard stats, shooting stats, passing stats, defencive stats, possession stats and miscellaneous stats.
All the stats are arranged and formatted by the website itself.
Also added a row editor which removes the indexes which are added after every 25 rows in the table.

The player data excel files contains the following information for every player that plays in each game played in a given leauge/season:

ALL PLAYERS

Name
Nationality
Position played
Age
Minutes played
Goals scored
Assists
Penalty kicks attempted and scored
Total shots and shots on target
Yellow and red cards
Total touches
Total tackles
Total interceptions
Total blocks
Expected goals scored (XG)
Expected goals scored without penalty kicks
Expected assists
Total passes attempted, completed
Progressive passes
Total carries and progressive carries
Total attacks and successful attacks
and many more.

Prerequisite Software
Python 3 (make sure to add Python to PATH/environment variables when installing)
selenium, pandas, beautifulsoup4, and openpyxl libraries installed
Chrome or Firefox browser with a compatible WebDriver (e.g., ChromeDriver or GeckoDriver)
Updated driver_path in the code to point to the WebDriver
Network and administrator permissions to access and save files
Windows installation
You can install the prerequisites double-clicking install_prerequesites.bat after installing Python 3.

Program Installation
This programme can either be installed by downloading the repository from the GitHub page or by running the following command if git is installed on your machine:

Using the program
You can edit the URLs according to the league/season from the segment of the website you want to scrape, and change the class id by inspecting the page.
I recommend not collecting mutiple seasons/leagues of data at once as the website may block access if you try to access it too many times in a short period of time. The program will then guide you through the rest of the process.

To-Dos
There are a few more things I want to do with this project. The current to-do list is below, but if you think of anything you'd like added, please let me know!

 Support more leagues
 Support squad(team) stats aswell
License
Licensed under MIT.

The data provided is property of https://fbref.com I don't own any of the data
