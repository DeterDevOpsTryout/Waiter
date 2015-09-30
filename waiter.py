#!/usr/bin/env python3

from bottle import request, route, run, template
import time

@route('/orderPie')
def orderPie():
    print ("Taking order for " + request.query.count + " pies")
    time.sleep(3)
    return request.query.count

print ("Waiter is waiting for customer")
run(host='localhost', port=8080)
