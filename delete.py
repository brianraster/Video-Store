import dataMgr
import view

def delete():
    """Deletes a film from the inventory"""
    view.viewData()
    newData = []
    temp = dataMgr.loadData('data.json')
    dataLen = len(temp) - 1
    print("Which index would you like to delete?")
    delOption = int(input(f'Select a number 0-{dataLen}: '))
    i = 0
    for entry in temp:
        if i == delOption:
            pass
            i += 1
        else:
            newData.append(entry)
            i += 1
    dataMgr.writeData('data.json', newData)