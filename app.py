from flask import Flask, jsonify, redirect, render_template, request
from DivisionSplitter import main_menu, get_chosen, split_division
from members_of_commons import *
from datetime import date


# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

billData = None

@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")


@app.route("/get", methods=["GET"])
def get():
    list_num = request.args.get("list_num")
    billData = main_menu(list_num)

    return render_template("results.html", billData=billData)

@app.route("/show", methods=["GET"])
def show():
    chosen_num = request.args.get("chosen_num")
    list_num = request.args.get("from_list")
    billData_1 = main_menu(list_num)
    divisionID = get_chosen(billData_1,chosen_num)
    chosen_bill_data = split_division(divisionID)
    votes=chosen_bill_data['result']['primaryTopic']['vote']
    aye='http://data.parliament.uk/schema/parl#AyeVote'
    no ='http://data.parliament.uk/schema/parl#NoVote'

    labAye = 0
    conAye = 0
    snpAye = 0
    libAye = 0
    pcmAye = 0
    grnAye = 0
    dupAye = 0
    indAye = 0

    for i in range(0,len(votes)):
        if votes[i]['type']==aye:
            if votes[i]['memberParty']=='Labour' or votes[i]['memberParty']=="Labour (Co-op)":
                labAye+=1
            if votes[i]['memberParty']=='Conservative':
                conAye+=1
            if votes[i]['memberParty']=='Scottish National Party':
                snpAye+=1
            if votes[i]['memberParty']=='Liberal Democrat':
                libAye+=1
            if votes[i]['memberParty']=='Plaid Cymru':
                pcmAye+=1
            if votes[i]['memberParty']=='Green Party':
                grnAye+=1
            if votes[i]['memberParty']=='Democratic Unionist Party':
                dupAye+=1
            if votes[i]['memberParty']=='Independent':
                indAye+=1
                
    totAyes={"labAye":labAye,"conAye":conAye,"snpAye":snpAye,"libAye":libAye,"pcmAye":pcmAye,"grnAye":grnAye,"dupAye":dupAye,"indAye":indAye}

    labNo = 0
    conNo = 0
    snpNo = 0
    libNo = 0
    pcmNo = 0
    grnNo = 0
    dupNo = 0
    indNo = 0

    for i in range(0,len(votes)):
        if votes[i]['type']==no:
            if votes[i]['memberParty']=='Labour' or votes[i]['memberParty']=="Labour (Co-op)":
                labNo+=1
                #labNames.append(votes[i]['memberPrinted']['_value'])
            if votes[i]['memberParty']=='Conservative':
                conNo+=1
            if votes[i]['memberParty']=='Scottish National Party':
                snpNo+=1
            if votes[i]['memberParty']=='Liberal Democrat':
                libNo+=1
            if votes[i]['memberParty']=='Plaid Cymru':
                pcmNo+=1
            if votes[i]['memberParty']=='Green Party':
                grnNo+=1
            if votes[i]['memberParty']=='Democratic Unionist Party':
                dupNo+=1
            if votes[i]['memberParty']=='Independent':
                indNo+=1

    totNoes={"labNo":labNo,"conNo":conNo,"snpNo":snpNo,"libNo":libNo,"pcmNo":pcmNo,"grnNo":grnNo,"dupNo":dupNo,"indNo":indNo}

    numCount = return_count_of_members()
    labTellers = 2
    conTellers = 2
    labSpkers  = 2
    conSpkers  = 1

    labAB = numCount[3]-labTellers-labSpkers-(labAye+labNo)
    conAB = numCount[0]-conTellers-conSpkers-(conAye+conNo)
    snpAB = numCount[6]-(snpAye+snpNo)
    libAB = numCount[4]-(libAye+libNo)
    pcmAB = numCount[5]-(pcmAye+pcmNo)
    grnAB = numCount[8]-(grnAye+grnNo)
    dupAB = numCount[1]-(dupAye+dupNo)
    indAB = numCount[2]-(indAye+indNo)

    sumAB = sum([labAB,conAB,snpAB,libAB,pcmAB,grnAB,dupAB,indAB])
    totAB = {"labAB":labAB,"conAB":conAB,"snpAB":snpAB,"libAB":libAB,"pcmAB":pcmAB,"grnAB":grnAB,"dupAB":dupAB,"indAB":indAB,"sumAB":sumAB}
    
    totes = {"totAyes":totAyes,"totNoes":totNoes,"totAB":totAB}

    date_str = chosen_bill_data["result"]["primaryTopic"]["date"]["_value"]

    year,month,day = date_str.split("-")

    _date = date(day=int(day),month=int(month),year=int(year)).strftime('%A %d %B %Y')

    choose = {"chosen_bill_data":chosen_bill_data,"totes":totes,"_date":_date}
    return render_template("choose.html", choose=choose)

