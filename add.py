import dataMgr

def addData():
    item = {}
    temp = dataMgr.loadData('data.json')
    item['title'] = input('Enter the title of the film: ')
    item['length'] = input(f'Enter {item["title"]}\'s length in minutes: ')
    item['rating'] = input(f'Enter {item["title"]}\'s rating: ')
    item['year'] = input(f'Enter the year {item["title"]} was released: ')
    temp.append(item)
    dataMgr.writeData('data.json', temp)