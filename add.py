import dataMgr
import datetime
import re

def addData():
    """Add a film to the inventory by following the prompts"""
    item = {}
    temp = dataMgr.loadData('data.json')
    item['title'] = input('Enter the title of the film: ')
    item['length'] = input(f'Enter {item["title"]}\'s length in minutes: ')
    item['rating'] = input(f'Enter {item["title"]}\'s rating: ')
    # need to verify next 2 lines and learn more RegEx
    # if not re.match('[gG][pg][PG][pg\-13][PG\-13][rR]', item['rating']):
    #     item['rating'] = input(f'Your input was incorrect,\nPlease choose between\n"G", "PG", "PG-13", or "R"')
    item['year'] = int(input(f'Enter the year {item["title"]} was released: '))
    if item['year'] < 1900:
        print(f'They weren\'t making movies in {item["year"]}.')
        item['year'] = int(input(f'Re-enter the year {item["title"]} was released: '))
        if item['year'] < 1900:
            print('Take it from the top.')
            addData()
    elif item['year'] > datetime.datetime.now().year:
        print('That year is in the future, try again.')
        item['year'] = int(input(f'Re-enter the year {item["title"]} was released: '))
        if item['year'] > datetime.datetime.now().year:
            print('Take it from the top.')
            addData()
    else:
        temp.append(item)
        dataMgr.writeData('data.json', temp)