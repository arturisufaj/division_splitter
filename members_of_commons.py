from xml.dom import minidom
import urllib.request



xmldoc = minidom.parse(urllib.request.urlopen("http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house=Commons/"))
#xmldoc = minidom.parse('members.xml')
itemlist = xmldoc.getElementsByTagName('Member')
partyList = xmldoc.getElementsByTagName('Party')

conCount=0
dupCount=0
indCount=0
labCount=0
libCount=0
pcmCount=0
snpCount=0
snfCount=0
grnCount=0
spkCount=0

for element in partyList:
        if element.getAttribute('Id') == "4": # id = 4 is Conservative
                conCount+=1
        if element.getAttribute('Id') == "7": # id = 7 is DUP
                dupCount+=1
        if element.getAttribute('Id') == "8": # id = 7 is Independent
                indCount+=1
        if element.getAttribute('Id') == "15": # id = 15 is Labour
                labCount+=1
        if element.getAttribute('Id') == "17": # id = 17 is Liberal Democrat
                libCount+=1
        if element.getAttribute('Id') == "22": # id = 22 is Plaid Cymru
                pcmCount+=1
        if element.getAttribute('Id') == "29": # id = 29 is SNP
                snpCount+=1
        if element.getAttribute('Id') == "30": # id = 30 is Sinn Féin
                snfCount+=1
        if element.getAttribute('Id') == "44": # id = 44 is Green
                grnCount+=1
        if element.getAttribute('Id') == "47": # id = 47 is Speaker
                spkCount+=1


totalMembersList=['Total Members of Conservative: ' + str(conCount),
                  'Total Members of DUP: ' + str(dupCount),
                  'Total Members of Independent: ' + str(indCount),
                  'Total Members of Labour: ' + str(labCount),
                  'Total Members of Liberal Democrat: ' + str(libCount),
                  'Total Members of Plaid Cymru: ' + str(pcmCount),
                  'Total Members of SNP: ' + str(snpCount),
                  'Total Members of Sinn Féin: ' + str(snfCount),
                  'Total Members of Green: ' + str(grnCount),
                  'Speaker: ' + str(spkCount),]

numbersOnly = [conCount,
               dupCount,
               indCount,
               labCount,
               libCount,
               pcmCount,
               snpCount,
               snfCount,
               grnCount,
               spkCount]


def print_members_of_each_party():
        sortedIndex = sorted(range(len(numbersOnly)), key=lambda k: numbersOnly[k], reverse=True)
        for i in sortedIndex:
                print(totalMembersList[i])
def return_count_of_members():
        return numbersOnly
