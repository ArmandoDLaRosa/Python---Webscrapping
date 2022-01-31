from bs4 import BeautifulSoup

# Read File
with open("/home/armando/Github Repos/Python---Webscrapping/test.html", "r") as html_page:
    content = html_page.read()
    
    soup = BeautifulSoup(content, 'lxml') # Use html as soup object
    print(soup.prettify())

    print("\n||Testing Beautiful Soup||\n")
    print("find:\n\t", soup.find('h5'))
   
    print("find all:")
    for el in soup.find_all('h5'):
        print("\t", el.text)

    print("\nfind inside another tag:")
    course_cards = soup.find_all('div', class_ = 'card') #How to Filter the search
    for el in course_cards:
        print("\t",el.h5.text.strip(), "  \t", # Get the name without whitespace at start/End
              el.a.text.split()[-1])   # price(last element)
