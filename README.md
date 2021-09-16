# CMSGrabber
![alt text](https://github.com/SecTheBit/CMSGrabber/blob/main/Media/CMSGrabber.png)

## About

CMSGrabber is a python based tool to detect CMS running in an application. It uses ![Python-Wappalyzer](https://github.com/chorsley/python-Wappalyzer) module to detect the contents running in the application and from there it fetches the CMS. A custom User-Agent header is already been added in the code to bypass the WAFs or  Firewalls. 
The tool can detect only those CMS that can be detected by the ![Wappalyzer](https://www.wappalyzer.com/).

## Screenshot
![alt_text](https://github.com/SecTheBit/CMSGrabber/blob/main/Media/tmp.png)

## Usage

It is highly recommended to install ![python-wappalyzer](https://github.com/chorsley/python-Wappalyzer) module  **from their Github Repo not by using Pip** 

1. Clone the Repo 
    ``` git clone https://github.com/SecTheBit/CMSGrabber.git ```
2. Run the tool 
    ``` python3 cmsgrabber.py --file_path urls_list.txt ```

## Creator
1. Twitter: [Divyanshu Diwakar](https://twitter.com/ddiwakr)








