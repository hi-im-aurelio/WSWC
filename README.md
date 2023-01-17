## WSWC - Run small data scraping templates to target websites.

- [INSTALLATION](#installation)
- [CONFIGURATION](#configuration)
- [RUNNING](#running)

# INSTALLATION
Clone the repository on your local machine:
~~~bash
# Usando HTTPS
git clone https://github.com/fariosofernando/WSWC.git
~~~
~~~bash
# Or using the GITHUB CLI
gh repo clone fariosofernando/WSWC
~~~

# CONFIGURATION
Assuming you have python installed, with the repository cloned on your machine, go to the root of the project, and run pip to install the necessary packages:
~~~bash
pip install -r requirements.txt
~~~
After having installed the packages, it's time to install the necessary components so that everything runs smoothly.
First we need to download and install the Firefox web driver.

## Windows
To install geckodriver on windows operating system, you need to go to geckodriver repository and download it in [Assets] section <a href="https://github.com/mozilla/geckodriver/releases">Assets Section</a> or click on this link <a href="https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-win32.zip">geckodriver</a>

<ul>
  <li>After installing, on your C: disk, create a folder named **webdrivers** and extract the downloaded file in this folder.</li>
  <li>Copy the full file path, it will be something like 'C:\webdrivers\geckodriver.exe'</li>
  <li>Right-click My Computer or This PC.</li>
  <li>Select Properties.</li>
  <li>Select advanced system settings.</li>
  <li>Click the Environment Variables button.</li>
  <li>Under System Variables, select PATH.</li>
  <li>Click on the Edit button.</li>
  <li>Click on the New button.</li>
  <li>Paste the copied path from the GeckoDriver.</li>
  <li>Save everything and exit.</li>
</ul>

Finally, make sure you have the latest version of Firefox installed on your computer.

##### NOTE: In the future, it will not be necessary to follow the two steps mentioned above, the web drivers, either Firefox's geckodriver, or Chrome's chromedriver will be included in the program along with Firefox and Chrome's executables, so that future errors of versions or related to that , are avoided.

# RUNNING
Currently, to run a given model on, open your terminal in the main project directory (assuming you have everything installed) and call the python installed on your system and the name of the model.
Something like:
~~~bash
python model_name_run.py
~~~
And wait for the scraping to be complete.
It will generate excel files for each category with finished scraping. In the main directory of the program, you will find these documents.

After the scraping is finished, if you want to have all the document information in a single excel document, run the following command in the main project directory:
~~~bash
python create_final_excel.py
~~~

And you will see a new file named final_document.xlsx.

