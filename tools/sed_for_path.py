#!/usr/local/bin/python3
## sed utility for MarkDown files with calc_relative_path.py

from calc_relative_path import calc_rel
import re

GITHUB = "https://github.com"
OPENWHISK = GITHUB + '/openwhisk/example-based-tutorial/blob/master/'

def one_file(mdpath, destpath):
    fp = open(destpath, 'w')
    for line in open(mdpath, 'r'):
        if contains_url(line, GITHUB):
            md_abspath = OPENWHISK + mdpath
            # interactive
            print("found url:", grep_url(line))
            ans = input("(f)ile, (d)ir, (s)kip, (q)uit: ")
            if ans == 'q':
                break
            elif ans == 'f':
                fp.write(new_line(line, md_abspath, file=True))
            elif ans == 'd':
                fp.write(new_line(line, md_abspath, file=False))
            else:
                fp.write(line)
        else:
            fp.write(line)
    fp.close()

def contains_url(s, url):
    return s.find(url) >= 0

def new_line(s, md_abspath, file=True):
    found_url = grep_url(s)
    dest_url = found_url if file else found_url+'/'
    return modify(s, md_abspath, dest_url)

def modify(s, md_abspath, dest_url):
    rel_path = calc_rel(md_abspath, dest_url)
    return s.replace(grep_url(s), rel_path)

def grep_url(line):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2})|/)+', line)
    assert(len(urls) == 1)
    return urls[0]

def trailing(url):
    ''' add a trailing slash in the end if it seems to be a directory '''
    if re.search(r'/issues/(?:[0-9]|[1-9][0-9]+)', url):
        return url
    elif url.endswith('/') or url.split('/')[-1].find('.') != -1:
        return url
    else:
        return url + '/'

def main():
    import sys
    print(sys.argv)
    _, mdpath, destpath = sys.argv
    one_file(mdpath, destpath)

import unittest

class SedTest(unittest.TestCase):
    def test_hello(self):
        self.assertTrue(True)

    def test_rel_path_calc(self):
        path1 = 'https://github.com/openwhisk/openwhisk-package/'
        path2 = 'https://github.com/openwhisk/feeds/hook/README.md'
        actual = calc_rel(path1, path2)
        expected = '../feeds/hook/README.md'
        self.assertEqual(actual, expected)

    def test_grep_url(self):
        s = '메시지를 발송하는 작업도 [Openwhisk 공식 액션](https://github.com/openwhisk/openwhisk-package/)으로 ...'
        actual = grep_url(s)
        expected = 'https://github.com/openwhisk/openwhisk-package/'
        self.assertEqual(actual, expected)

    def test_modify(self):
        s = '메시지를 발송하는 작업도 [Openwhisk 공식 액션](https://github.com/openwhisk/openwhisk-package/)으로 ...'
        md_abspath = 'https://github.com/openwhisk/example-based-tutorial/feeds/hook/README.md'
        dest_url = grep_url(s)
        actual = modify(s, md_abspath, dest_url)
        expected = '메시지를 발송하는 작업도 [Openwhisk 공식 액션](../../../openwhisk-package/)으로 ...'
        self.assertEqual(actual, expected)

    def test_replace_str(self):
        self.assertEqual('apple'.replace('p', 'P'), 'aPPle')
        
    def test_new_line(self):
        s = 'watchtower를 이용해 카카오톡 메시지를 발송하는 작업도 [Openwhisk 공식 액션](https://github.com/openwhisk/openwhisk-package/)으로'
        actual = new_line(s, 'https://github.com/openwhisk/example-based-tutorial/feeds/hook/README.md')
        expected = 'watchtower를 이용해 카카오톡 메시지를 발송하는 작업도 [Openwhisk 공식 액션](../../../openwhisk-package/)으로'
        self.assertEqual(actual, expected)

    def test_trailing(self):
        url1 = 'https://github.com/openwhisk/example-based-tutorial/feeds/hook/hello.js'
        url2 = 'https://github.com/openwhisk/example-based-tutorial/feeds/hook/'
        url3 = 'https://github.com/openwhisk/example-based-tutorial/feeds/hook'

        self.assertEqual(trailing(url1), url1)
        self.assertEqual(trailing(url2), url2)
        self.assertEqual(trailing(url3), url3 + '/')

if __name__ == "__main__":
    # unittest.main()
    main()

