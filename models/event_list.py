from models.event import *



event1 = Event("14th Feb 2021", "Valentines Day", "20", "Bedroom", "Wear Red, Less is Definitely More", True)
event2 = Event("10th July 2021", "Wedding", "200", "The Church", "White Wedding", False)
event3 = Event("25th December 2021", "Christmas", "1000", "The North Pole", "Drunk Elves Rockin' Around The Christmas Tree", False)
event4 = Event("17th March 2021", "St Patricks Day", "500", "Function Hall", "Wear Green", True)
event5 = Event("11th September 2021", "E50 Graduation", "25", "Castle Street, Edinburgh", "Prepare to Celebrate", False)
events = [event1, event2, event3, event4, event5]

def add_new_event(event):
    events.append(event)
