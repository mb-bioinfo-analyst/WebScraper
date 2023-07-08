[![HitCount](https://hits.dwyl.com/mb-bioinfo-analyst/WebScraper.svg?style=flat-square)](http://hits.dwyl.com/mb-bioinfo-analyst/WebScraper)
 
# Web Scraper for Webserver   
This is a Python web scraper code specifically designed for web servers. It utilizes the Selenium and BeautifulSoup libraries to extract table data from web pages.

## Prerequisites   
Before using this web scraper, make sure you have the following installed:

- Python 3.x
- Selenium
- BeautifulSoup
- ChromeDriver (for using the Chrome browser)



## Installation

1. Clone the repository:   

```python
git clone https://github.com/your-username/web-scraper.git
```

2. Install the required dependencies:   
```python
pip install selenium beautifulsoup4
```
Download and install ChromeDriver from the official website: ChromeDriver - WebDriver for Chrome



## Usage
1. Open the scraper.py file and modify the web page URL to scrape:   

```python

driver.get('http://wintervar.wglab.org/results.pos.php?queryType=position&chr=1&pos=1669648&ref=CT&alt=&build=hg19')
```

2. Run the scraper:  

```python
python scraper.py
```



## Scenarios


### Scenario 1: Submit Button Pressed
In this scenario, the query lands on a results page after pressing the submit button.



### Scenario 2: Direct Query Results
In this scenario, the query lands directly on the results page without pressing the submit button. If there is no data available for the query, the program will display a message and exit. Otherwise, it will extract the table data and display it.



## Contributing
Contributions to this web scraper are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.



## License
This project is licensed under the MIT License.



## Acknowledgements
This web scraper is built using the following libraries:

Selenium
BeautifulSoup



## Disclaimer
Please use this web scraper responsibly and in accordance with the terms and conditions of the websites you scrape. Be mindful of the legal and ethical implications of web scraping.

Feel free to customize the README file further based on your specific needs and include any additional information you think would be relevant or helpful for users.



### Credits
Thanks goes to [mb-bioinfo-analyst](https://github.com/mb-bioinfo-analyst).   
You may visit the following for more;

[Portfolio](https://mb-bioinfo-analyst.github.io/Portfolio/)  

[Publications](https://sites.google.com/view/bilalmustafa/publications?authuser=0)  

[RNA-Seq Analysis: A Beginner’s Guide to Understanding Gene Expression Using R](https://rnaseqanalysis.netlify.app/)  

[Accessing data from SQL using R](https://mb-bioinfo-analyst.github.io/Tutorials/R2SQL.nb.html)  

[Normalization App!](https://bmustafa12.shinyapps.io/Normalization/) 