#!/usr/bin/env python2


import urllib2 as u
import json
import time
import threading as t
import random


class Observer(object):
    """ The oberver here works like an event dispatcher,
        executing the callbacks in the order they were registered """

    def __init__(self):
        self.callback_list = []
        
    def register(self,callback,post_id):
        self.callback_list.append( (callback, post_id) )
        
    def trigger(self, current_id, result):
        for callback, associated_id in self.callback_list:
            if current_id == associated_id:
                callback(result) 
            

def get_data(post_id):
    def __get_data():
        time.sleep(random.randint(1,10))
        site= "http://jsonplaceholder.typicode.com/posts/" + str(post_id)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = u.Request(site,headers=hdr)
        raw_data = u.urlopen(req).read()
        data = json.loads(raw_data)
        print "data received -- " + str(post_id)
        observer.trigger(post_id, data['title'])
        
    my_thread = t.Thread(target=__get_data)
    my_thread.start()
  

def async_function_1(callback):
    if callback is not None:
        observer.register(callback,1)

    get_data(1)
        

def async_function_2(callback):
    if callback is not None:
        observer.register(callback,2)

    get_data(2)
              

def driver():
    def call_back_1(res):
        print "processed data - 1, Here is the data retreived : {0}".format(res)
        
        def call_back_2(res):
            print "processed data - 2, Here is the data retreived : {0}".format(res)

        async_function_2(call_back_2)

    async_function_1(call_back_1)
      

def boss_thread():
    driver()

    while True :
        print "processing"
        time.sleep(2)
    

observer = Observer()


if __name__ == '__main__':
    boss_thread()

