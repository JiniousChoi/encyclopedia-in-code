#!/usr/bin/env python2
# -*- coding: cp949 -*-
import re
from selenium import webdriver
from time import sleep
from Tkinter import *
from LINKHELPER import *

#to do list: remove the duplicate in hrefList
class App:
    def __init__(self, master):
        ################ FRAME 1 #################
        master.title("BATCH DOWNLOADER")
        master.geometry("700x500")

        self.frame1=Frame(master)
        self.frame1.pack()

        self.label=Label(self.frame1, text="Web Address")
        self.label.pack(side=LEFT)

        self.addrEntry=Entry(self.frame1)
        self.addrEntry.pack(side=LEFT, padx=5)
        self.addrEntry.bind("<Return>", self.event_GO)

        self.addrBtn = Button(self.frame1, text="Go", command=self.GO)
        self.addrBtn.pack(side=LEFT)

        #in-search box
        self.label=Label(self.frame1, text="in-search")
        self.label.pack(side=LEFT)

        self.searchEntry=Entry(self.frame1)
        self.searchEntry.pack(side=LEFT, padx=5)
        self.searchEntry.bind("<Return>", self.event_SEARCH)

        ############### FRAME 2 #################
        self.frame2=Frame(master)
        self.frame2.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.scrollbar = Scrollbar(self.frame2, orient=VERTICAL)
        self.scrollbar.config(command=self.YVIEW)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.showList = Listbox(self.frame2, yscrollcommand=self.scrollbar.set, selectmode=EXTENDED)
        self.showList.pack(side=LEFT, fill=BOTH, expand=1)
        ############### FRAME 3 ####################
        self.frame3=Frame(master)
        self.frame3.pack(side=BOTTOM)
        
        self.getSelBtn = Button(self.frame3, text="Click Selected", command=self.CLICKSELECTED)
        self.getSelBtn.pack(side=LEFT)
        self.clrBtn = Button(self.frame3, text="Clear", command=self.CLEAR)
        self.clrBtn.pack(side=LEFT)
        
        self.getPgSrcBtn = Button(self.frame3, text="Get Page Source", command=self.GETPAGESOURCE)
        self.getPgSrcBtn.pack(side=LEFT)
        ############### INITILIZATION ##############
        self.ie = webdriver.Firefox()

    def YVIEW(self, *arg):
        self.showList.yview(*arg)
        
    def GO(self):
        #self.showList.delete(0,END)
        self.hrefList = []
        self.ie.get(self.addrEntry.get())
        self.cur_html = self.ie.page_source
        ##여기에서 get all links를 해야하는데 음..ㅋㅋ
        #hrefList에는 [,,,'http://...lecture4.mp4']
        self.hrefList = get_all_links( self.cur_html )
        self.resetShowList()

    def setShowList(self):
        #always reset mapshow2href
        self.mapshow2href=[]
        
        #pdb.set_trace()
        #fill the listboxes with hrefList
        for i, show in enumerate(self.hrefList):
            self.showList.insert( i , ' |%-3d | '%(i) + show )
            self.mapshow2href.append(i)

    def resetShowList(self):
        self.showList.delete(0,END)
        self.setShowList()

    def event_GO(self, event):
        #print 'Enter pressed'
        self.GO()

    #only change to showList
    def event_SEARCH(self, event):
        self.SEARCH()

    #change showList here
    def SEARCH(self):
        keywords = self.searchEntry.get().split()
        if not keywords:
            #그냥 빈칸에 엔터를 쳤다면, showList가 리셋된 상태처럼 돌아가게됨.
            self.resetShowList()
            print self.mapshow2href
        else:
            #showList안에서 keyword를 품고 있는 것만 보여주기.
            self.showList.delete(0,END)
            self.mapshow2href=[]
            cnt=0
            for i, show in enumerate(self.hrefList):
                for keyword in keywords:
                    if keyword in show:
                        #search에 부합하는 index만 추려넣기.
                        self.mapshow2href.append(i)
                        #self.showList.insert( cnt , ' |%-3d | '%(i) + show )
                        #insert메소드 특성:1,3,5로 요청해도 0,1,2로 들어간다.
                        self.showList.insert( cnt , ' |%-3d | '%(i) + show )
                        cnt+=1
                        break;
            print self.mapshow2href
                    
                    
                                
    def CLEAR(self):
        #print "Clear!"
        self.showList.delete(0,END)
        self.hrefList = []

    #case1 : inlink to a html, it moves you there.
    #case2 : inlink to a content, it downloads it.
    def CLICKSELECTED(self):
        self.selItems = self.showList.curselection()
        #for bug issue
        self.selItems = map(int, self.selItems)
        print self.selItems
        print self.mapshow2href
        for el in self.selItems:
            print self.hrefList[self.mapshow2href[el]]
            
            self.ie.get(self.hrefList[self.mapshow2href[el]])
            sleep(3)

    def GETPAGESOURCE(self):
        print '-'*30
        print self.cur_html
        print '-'*30
        
if __name__=='__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
