import urllib.request, json

def main_menu(list_num):
    numberOfBills = list_num
    billURL = 'http://lda.data.parliament.uk/commonsdivisions.json?_view=Commons+Divisions&_pageSize=' + str(numberOfBills) + '&_page=0'

    with urllib.request.urlopen(billURL) as url:
        billData = json.loads(url.read().decode())

    return billData

def get_chosen(billData,chosen_num):
    chosenBill = billData["result"]["items"][int(chosen_num)-1]["_about"]
    divisionID = chosenBill.split('http://data.parliament.uk/resources/',1)[1]
    return divisionID

def split_division(divisionID):
    urlToOpen = 'http://lda.data.parliament.uk/commonsdivisions/id/' + divisionID + '.json'

    with urllib.request.urlopen(urlToOpen) as url:
        chosen_bill_data = json.loads(url.read().decode())
    return chosen_bill_data