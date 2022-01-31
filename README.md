# Webscrapping

## Tools 
---
* WSL (Ubuntu 20.04)
* Vscode (Remote Wsl, Python Extension, Html Preview)
* Python (Beautiful Soup, lxml, requests)
* Chrome Ispection Tool

## Steps
---
1) Create python environment (.venv files should be good inside the project folder)
    ```
    sudo apt install python3-virtualenv
    virtualenv scrapEnv
    ```

2) Activate python environment
    ``` 
    source scrapEnv/bin/activate

3) Change in vscode the interpreter to the python inside scrapEnv/bin/python3.8 
   1) This way you can run the .py with the extension RUN button with the env activated.
   2) Otherwise, you'll have to run it like `python3 fileName.py` and the env activated.
   
4) Install Beautiful Soup
   ```
   pip install beautifulsoup4
   ```
5) Install Beautiful Soup - Parser
   ```
   pip install lxml
   ```
6) Install Request Library
   ```
   pip install requests
   ```
## Resources
---
[Web Scrapping CrashCourse - FreeCodeCamp](https://www.youtube.com/watch?v=XVv6mJpFOb0)
