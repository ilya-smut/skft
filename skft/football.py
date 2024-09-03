import requests
from bs4 import BeautifulSoup

def get_and_write_to_file():
    # Making a GET request
    r = requests.get('https://www.skysports.com/watch/football-on-sky')

    # check status code for response received
    # success code - 200
    print(r)

    # print content of request
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())
    with open("file.txt", "w") as file:
        file.write(soup.prettify())

def get():
    r = requests.get('https://www.skysports.com/watch/football-on-sky')
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup



def readfile():
    with open ("file.txt", "r") as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        return soup
    

def find_all(target, search_value, attributes):
    found = target.findAll(search_value, attrs=attributes)
    values = []
    for element in found:
        values.append(element.get_text(strip=True))
    return values

    
def process(html_soup):
    soup = BeautifulSoup()
    soup.append(html_soup)
    teams1 = find_all(soup, 'li', 'col1')
    teams2 = find_all(soup, 'li', 'col3')
    times = find_all(soup, 'li', 'col2')
    where = find_all(soup, 'p', 'event-detail')
    date = soup.find('h3', 'text-h4').get_text(strip=True)
    if len(teams1) == len(teams2) == len(times) == len(where):
        structured_data = []
        length = len(teams1)
        for i in range(length):
            structured_data.append({'home' : teams1[i], 'away' : teams2[i], 'time' : times[i], 'date' : date, 'where' : where[i]})
        return structured_data
    else:
        error = Exception()
        error.add_note("Length of parsed items didn't match")
        return error
    

def to_string(structured_data):
    message = ''
    message += '\n-----------------\n'
    message += structured_data[0]['date']
    message += '\n'
    message += '-----------------\n'
    for item in structured_data:
        message += ("{: ^30}".format(item['home']) + item['time'] + "{: ^30}".format(item['away']) + ' | ' +
                    item['where'] + '\n\n')
    return message

def run():
    print(to_string(process(get())))



if __name__ == "__main__":
    print(to_string(process(get())))