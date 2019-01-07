#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:44:21 2018

@author: sagar
"""

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from aux_functions import this_weekend
from datetime import datetime, time



# Setup the Calendar API
def instantiate():
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials/credentials.json')
    creds = store.get()
    
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials/client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service

def create_event(service, summary, description, dt, attendees, attendee_type):
    if attendee_type is "M":
        ts = time(9,0,0)
        te = time(13,0,0)
    elif attendee_type is "A":
        ts = time(14,0,0)
        te = time(18,0,0)
    elif attendee_type is "F":
        ts = time(9,0,0)
        te = time(18,0,0)
    else:
        raise "Attendee type mismatch. It should be either 'Mentor' or 'DS'"
    event = {
      'summary': summary,
      'description': description,
      'start': {
      'dateTime': datetime.combine(dt,ts).isoformat(),
        'timeZone': 'Asia/Calcutta',
      },
      'end': {
      'dateTime': datetime.combine(dt,te).isoformat(),
        'timeZone': 'Asia/Calcutta',
      },
      'attendees': attendees
    }
    event = service.events().insert(calendarId='primary', body=event, sendNotifications=True).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    return event.get('id')

