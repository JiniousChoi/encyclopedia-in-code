#!/usr/bin/env python2
## generate wget commands for downloading video, subtitle, transcript and slides

from selenium import webdriver
from time import sleep
import sys

COURSERA_HOME = "https://www.coursera.org"
WEEK_TMPL = "https://www.coursera.org/learn/progfun1/home/week/{}"
WEEK_START = 1
WEEK_STOP = 6

def week_links(start, stop):
    ''' [week_link holding links of lectures for the week] '''
    assert start <= stop
    week_links = []
    for i in range(start, stop+1):
        week_link = WEEK_TMPL.format(i)
        week_links.append(week_link)
    return week_links

def inner_html(el):
    ''' return str '''
    return el.text

def css_select(browser, css):
    ''' return FirefoxWebElement '''
    for _ in range(10):
        try:
            return browser.find_element_by_css_selector(css)
        except Exception:
            #waiting for the browser to be fully loaded
            sleep(1)

    sys.stderr.write("[ERR] given css({}) cannot be found\n".format(css))

def location(browser):
    ''' url::str '''
    return browser.current_url

def href(el):
    ''' href::str '''
    res = hrefs(el)
    return res[0]

def hrefs(el):
    ''' [href::str] '''
    el_anchors = el.find_elements_by_tag_name('a')
    return [el_anchor.get_attribute('href') for el_anchor in el_anchors]
    
def lecture_links(browser):
    ''' return [lecture_href::str] '''
    return hrefs(css_select(browser, '.rc-ModuleLessons'))

def click(anchor_el):
    anchor_el.click()

def move_to(browser, href):
    ''' move to absolute url, not by clicking some elements
        @param browser: webdriver instance 
        @param href: url::str '''
    browser.get(href)

def main():
    browser = webdriver.Firefox()
    browser.get(COURSERA_HOME)
    raw_input('Enter anything if authenticated!! :')

    fp = open('./downloader.sh', 'w')

    for week_link in week_links(WEEK_START, WEEK_STOP):
        browser.get(week_link)

        sys.stdout.write('========== starting week_link({}) ==========\n'.format(week_link))

        for lecture_link in lecture_links(browser):

            sys.stdout.write('===== starting lecture_link({}) =====\n'.format(lecture_link))
            browser.get(lecture_link)

            try:
                headline = inner_html(css_select(browser, 'h1.headline-2-text')).replace(' ','')
            except Exception:
                sys.stderr.write("no headline found. Abort this lecture link\n")
                continue

            try:
                subtitle_lnk = href(css_select(browser, '.rc-SubtitleDownloadItem'))
                if subtitle_lnk:
                    fp.write('wget "{}" -O {}.vtt\n'.format(subtitle_lnk, headline))
            except Exception:
                sys.stderr.write("no subtitle link found\n")

            try:
                transcript_lnk = href(css_select(browser, '.rc-TranscriptDownloadItem'))
                if transcript_lnk:
                    fp.write('wget "{}" -O {}.txt\n'.format(transcript_lnk, headline))
            except Exception:
                sys.stderr.write("no transcript link found\n")
            
            try:
                slide_lnk = href(css_select(browser, '.rc-AssetDownloadItem'))
                if slide_lnk:
                    fp.write('wget "{}" -O {}.pdf\n'.format(slide_lnk, headline))
            except Exception:
                sys.stderr.write("no slide link found\n")
            
            try:
                click(css_select(browser, '.rc-LectureDownloadItem\n'))
                video_lnk = browser.current_url
                if video_lnk:
                    fp.write('wget "{}" -O {}.mp4\n'.format(video_lnk, headline))
            except Exception:
                sys.stderr.write("no video link found\n")

            fp.write('\n')
            fp.flush()

            sys.stdout.write('===== end of lecture_link =====\n')
            
    fp.close()

main()
