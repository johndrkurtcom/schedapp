#encoding: utf-8
from flask import render_template
from . import main
import newRequest as ebd


def stuff(key, cookies, website):
    format = 'json'
    load=ebd.Request(key, format, website)
    
    Monday = ebd.Day('monday', load)
    Tuesday = ebd.Day('tuesday', load)
    Wednesday = ebd.Day('wednesday', load)
    Thursday = ebd.Day('thursday', load)
    Friday = ebd.Day('friday', load)
    
    week={'Monday': Monday, 'Tuesday': Tuesday, 'Wednesday': Wednesday, 
    'Thursday': Thursday, 'Friday': Friday}

    rooms =  {i : ebd.INFO(week.get(i), website, cookie=cookies ).getRooms() for i in week}

    roomEvents = {i : ebd.INFO(week.get(i), website, cookie=cookies).getEventsPerRoom() for i in week}
    
    eventInfo = {i : ebd.INFO(week.get(i), website, cookie=cookies).getEventInfo() for i in week}
    
    return {'week':week, 'rooms':rooms, 'roomEvents':roomEvents, 'eventInfo':eventInfo}
    
key = '93c5b2c7d6a01f93c1fc704e6870ca9d'
cookie = {'token': 's%3A128%3A%22pDL9ntrG9FoabtgR6QCB3haf8aQg2Ah40ovAJvqlESnt4jbdLGtNG17cQEVCvOcJsB3O7MWbAiNCprbpUo52CVReUN8bmna5tmWvDfnk8fOb1QArAKL1wbo02KOD98hn%22%3B'}
website = "http://m3aawg34.sched.org/"
stuff = stuff(key, cookie, website)


@main.route('/')
def index():
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    date = {'Monday': 'June 8', 'Tuesday': 'June 9', 'Wednesday': 
    'June 10', 'Thursday': 'June 11', 'Friday': 'June 12'}
    week = stuff.get('week')
    rooms = stuff.get('rooms')
    roomEvents = stuff.get('roomEvents')
    eventInfo = stuff.get('eventInfo')
    title="M3AAWG35 June 2015"
    
    
    return render_template('/Tmp2/basetmpTable.htm',
                            title=title,
                            days = days,
                            week=week,
                            date=date,
                            roomName=rooms,
                            roomEvents=roomEvents,
                            eventinfo=eventInfo)
    
