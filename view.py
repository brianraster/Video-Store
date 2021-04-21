import dataMgr

def viewData():
    temp = dataMgr.loadData('data.json')
    i = 0
    for entry in temp:
        title = entry['title']
        length = entry['length']
        rating = entry['rating']
        year = entry['year']
        print(f'Index number: {i}')
        print(f'Title: {title}')
        print(f'Length: {length}')
        print(f'Rating: {rating}')
        print(f'Year of Release: {year}')
        print('\n')
        i += 1