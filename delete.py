import dataMgr
import view


# def stock0():
#     # TODO: fix this code and have it not leave an empty bracket in data.json
#     # -------- this operation leaves an empty object in the json file ----------
#     # ------------------- need to figure out why and fix it --------------------
#     if entry['stock'] <= 0:
#         print(f"{entry['title']}'s stock is 0, would you like to delete the title?\nY/N?")
#         usrch = input('')
#         if usrch == 'Y' or usrch == 'y':
#             for film in temp:
#                 if i == delOption:
#                     pass
#                     i += 1
#                 else:
#                     newData.append(film)
#                     i += 1
#             # del entry           # does not delete the entry
#             # del entry['title']
#             # del entry['length']
#             # del entry['rating']
#             # del entry['year']
#             # del entry['stock']
#             # for object in temp:
#             #     if object is None:
#             #         pass
#             #     else:
#             #         newData.append(object)
#         else:
#             continue
#     # --------------------------------------------------------------------

def delete():
    """Deletes a film from the inventory"""
    view.viewData()
    newData = []
    temp = dataMgr.loadData('data.json')
    dataLen = len(temp) - 1
    print('Are you deleting:\n1. An entire film\'s stock\n2. A copy of a film')
    choice = int(input(''))
    if choice == 1:
        print('-------------------- W A R N I N G: -------------------------\n'
              ' This action will delete all the stock of the selected film.\n'
              '           Are you sure you want to do this?')
        yn = input('Y/N: ')
        if yn == 'Y' or yn == 'y':
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
        if yn == 'N' or yn == 'n':
            print('Going back to main menu.')
    # TODO: If deleting copy of film past 0, will move to negative numbers
    if choice == 2:
        print('Which index are you removing a copy of?')
        delOption = int(input(f'Select a number 0-{dataLen}: '))
        i = 0
        for entry in temp:
            if i == delOption:
                if entry['stock'] == 1:
                    pass
                    i += 1
                entry['stock'] -= 1
                newData.append(entry)
                i += 1
            else:
                newData.append(entry)
                i += 1

        dataMgr.writeData('data.json', newData)
