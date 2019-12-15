#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


import re
import unittest

from io import StringIO
from unittest.mock import patch
from html.parser import HTMLParser
from jpylib.jtests import strips, lstrips
from string import ascii_uppercase, digits


class RegexAndParsingTest(unittest.TestCase):


    ######################################
    #### Detect Floating Point Number ####
    ######################################
    def test_detect_floating_point_number(self):
        float_pattern = re.compile(r'^[+-]?([1-9][0-9]+|[0-9])?\.[0-9]+$')
        for subject in ['+4.50', '4.5', '-1.0', '.5', '-.7', '+.4', '12.0']:
            self.assertTrue(bool(re.search(float_pattern, subject)))
        for subject in ['-+4.5', '12.']:
            self.assertFalse(bool(re.search(float_pattern, subject)))
        

    ####################
    #### Re.split() ####
    ####################
    def test_re_split(self):
        self.assertEqual(re.split(r'[.,]+', '100,000,000.000'), ['100', '000', '000', '000'])
            

    #########################################
    #### Group(), Groups() & Groupdict() ####
    #########################################
    def test_group(self):
        m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
        # entire match
        self.assertEqual(m.group(0), 'username@hackerrank.com') 
        # The first parenthesized subgroup.
        self.assertEqual(m.group(1), 'username') 
        # The second parenthesized subgroup.
        self.assertEqual(m.group(2), 'hackerrank') 
        # The third parenthesized subgroup.
        self.assertEqual(m.group(3), 'com') 
        # Multiple arguments give us a tuple.
        self.assertEqual(m.group(1,2,3), ('username', 'hackerrank', 'com'))


    def test_groups(self):
        m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
        self.assertEqual(m.groups(), ('username', 'hackerrank', 'com'))


    def test_groupdict(self):
        m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
        self.assertEqual(m.groupdict(), {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'})


    def test_group_groups_groupdict(self):
        subject = '..12345678910111213141516171820212223'
        m = re.search(r'([0-9A-Za-z])\1', subject)
        self.assertEqual(m.group(1), '1')


    ######################################
    #### Re.findall() & Re.finditer() ####
    ######################################
    def test_findall(self):
        self.assertEqual(re.findall(r'\w','http://www.hackerrank.com/'),
            ['h','t','t','p','w','w','w','h','a','c','k','e','r','r','a','n','k','c','o','m'])


    def test_finditer(self):
        url = 'http://www.hackerrank.com/'
        self.assertTrue(bool(re.finditer(r'\w', url)))
        self.assertEqual(list(map(lambda x: x.group(), re.finditer(r'\w', url))),
            ['h','t','t','p','w','w','w','h','a','c','k','e','r','r','a','n','k','c','o','m'])


    def test_re_findall_and_re_finditer(self):
        def actual(s):
            vowl, cons = 'aeiou', 'qwrtypsdfghjklzxcvbnm'
            pat = re.compile(r'(?<=[%s])([%s]{2,})(?=[%s])' %(cons, vowl, cons), re.I)
            return list(re.findall(pat, s))

        self.assertEqual(actual('rabcdeefgyYhFjkIoomnpOeorteeeeet'), ['ee', 'Ioo', 'Oeo', 'eeeee'])
    

    ###############################
    #### Re.start() & Re.end() ####
    ###############################
    def test_start(self):
        m = re.search(r'\d+', '1234')
        self.assertEqual(m.start(), 0)
        self.assertEqual(m.end(), 4)


    def test_re_start_and_re_end(self):
        def using_regex(s, k):
            pat = re.compile('{}(?={})'.format(k[0], k[1:]))
            if not re.search(pat, s):
                return [(-1,-1)]

            res = []
            for m in re.finditer(pat, s):
                start = m.start()
                end = start + len(k) - 1
                res.append((start, end))
            return res
        
        def using_str_api(s, k):
            start = s.find(k)
            if start == -1:
                return [(-1,-1)]
            
            res = []
            while start != -1:
                res.append((start, start+len(k)-1))
                start = s.find(k, start+1)

            return res

        for method in [using_regex, using_str_api]:
            self.assertEqual(method('aaadaa','aa'), [(0,1),(1,2),(4,5)])

        for method in [using_regex, using_str_api]:
            self.assertEqual(method('aaadaa','dd'), [(-1,-1)])


    ############################
    #### Regex Substitution ####
    ############################
    def test_transformation_of_strings(self):
        def square(match):
            number = int(match.group(0))
            return str(number**2)
        
        def actual(text):
            return re.sub(r"\d+", square, text)

        self.assertEqual(actual("1 2 3 4 5 6 7 8 9"), "1 4 9 16 25 36 49 64 81")


    def test_replacements_in_strings(self):
        def actual(html):
            return re.sub("(<!--.*?-->)", "", html)

        html = """
        <head>
        <title>HTML</title>
        </head>
        <object type="application/x-flash" 
          data="your-file.swf" 
          width="0" height="0">
          <!-- <param name="movie"  value="your-file.swf" /> -->
          <param name="quality" value="high"/>
        </object>
        """

        expected = '''
        <head>
        <title>HTML</title>
        </head>
        <object type="application/x-flash" 
          data="your-file.swf" 
          width="0" height="0">
          
          <param name="quality" value="high"/>
        </object>
        '''

        self.assertEqual(actual(html), expected)
        

    def test_regex_substitution(self):
        lines = '''
        if a + b > 0 && a - b < 0:
            start()
        elif a*b > 10 || a/b < 1:
            stop()
        print set(list(a)) | set(list(b)) 
        #Note do not change &&& or ||| or & or |
        #Only change those '&&' which have space on both sides.
        #Only change those '|| which have space on both sides.
        '''
	
        expected = '''
        if a + b > 0 and a - b < 0:
            start()
        elif a*b > 10 or a/b < 1:
            stop()
        print set(list(a)) | set(list(b)) 
        #Note do not change &&& or ||| or & or |
        #Only change those '&&' which have space on both sides.
        #Only change those '|| which have space on both sides.
        '''


        def actual(lines):
            lines = re.sub(r'(?<= )&&(?= )', 'and', lines)
            lines = re.sub(r'(?<= )\|\|(?= )', 'or', lines)
            return lines

        self.assertEqual(actual(lines), expected)


    ###################################
    #### Validating Roman Numerals ####
    ###################################
    def test_roman(self):
        def actual(x):
            pat = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
            return bool(re.search(pat, x))

        self.assertTrue(actual('CDXXI'))
        self.assertFalse(actual('CDCD'))


    ##################################
    #### Validating phone numbers ####
    ##################################
    def test_validating_phone_number(self):
        def actual(pn):
            return bool(re.match(r'[789][0-9]{9}$', pn))

        self.assertTrue(actual('9587456281'))
        self.assertFalse(actual('1252478965'))


    ################################################
    #### Validating and Parsing Email Addresses ####
    ################################################
    def test_validating_and_parsing_email_addresses(self):
        def actual(cc):
            from email.utils import parseaddr
            email_pattern = r'^[a-zA-Z][\w\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
            name, email = parseaddr(cc)
            return bool(re.match(email_pattern, email))

        self.assertTrue(actual('DOSHI <DOSHI@hackerrank.com>'))
        self.assertFalse(actual('VIRUS <virus!@variable.:p>'))
    

    ########################
    #### Hex Color Code ####
    ########################
    def test_hex_color_code(self):

        def is_css_selector(line, hexcode):
            line = line.strip()
            if re.match(r'%s( *\{)?$' % (hexcode), line):
                return True
            return False

        def hex_color_code(lines):
            hex_pattern = re.compile(r'#[0-9a-fA-F]{3}\b|#[0-9a-fA-F]{6}\b')
            for line in lines:
                for matcher in re.finditer(hex_pattern, line):
                    code = matcher.group()
                    if is_css_selector(line, code):
                        continue
                    yield code

        css = '''
        #BED
        {
            color: #FfFdF8; background-color:#aef;
            font-size: 123px;
            background: -webkit-linear-gradient(top, #f9f9f9, #fff);
        }
        #Cab
        {
            background-color: #ABC;
            border: 2px dashed #fff;
        }
        '''
        lines = css.splitlines()
        expected = ['#FfFdF8', '#aef', '#f9f9f9', '#fff', '#ABC', '#fff']
        self.assertEqual(list(hex_color_code(lines)), expected)
    

    ##############################
    #### HTML Parser - Part 1 ####
    ##############################
    def test_html_parser_part1(self):
        # create a subclass and override the handler methods
        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                print("Start :", tag)
                for attr in attrs:
                    print('->', ' > '.join([str(a) for a in attr]))
            def handle_endtag(self, tag):
                print("End   :", tag)
            def handle_startendtag(self, tag, attrs):
                print("Empty :", tag)
                for attr in attrs:
                    print('->', ' > '.join([str(a) for a in attr]))

        def filter_html_comment(html):
            comments_pat = re.compile(r'<!--.*?-->', re.DOTALL)
            return re.sub(comments_pat, '', html)

        def actual(html):
            html = filter_html_comment(html)
            parser = MyHTMLParser()
            parser.feed(html)
            parser.close()

        html = '''<html><head><title>HTML Parser - I</title></head>
                  <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>'''
        expected = ''' Start : html
                       Start : head
                       Start : title
                       End   : title
                       End   : head
                       Start : body
                       -> data-modal-target > None
                       -> class > 1
                       Start : h1
                       End   : h1
                       Empty : br
                       End   : body
                       End   : html
                       '''
        html, expected = map(strips, [html, expected])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            actual(html)
            self.assertEqual(fake_out.getvalue(), expected)


    ###########################################################
    #### Detect HTML Tags, Attributes and Attribute Values ####
    ###########################################################
    def test_html_tags_attributes_and_attribute_values(self):
        html = '''<head>
                  <title>HTML</title>
                  </head>
                  <object type="application/x-flash" 
                  data="your-file.swf" 
                  width="0" height="0">
                  <!-- <param name="movie" value="your-file.swf" /> -->
                  <param name="quality" value="high"/>
                  </object>
                  '''
        expected = '''head
                      title
                      object
                      -> type > application/x-flash
                      -> data > your-file.swf
                      -> width > 0
                      -> height > 0
                      param
                      -> name > quality
                      -> value > high
                      '''

        html, expected = map(strips, [html, expected])
        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                print(tag)
                for attr in attrs:
                    print('->',' > '.join(map(str,attr)))
                
        def actual(html):
            parser = MyHTMLParser()
            parser.feed(html)
            parser.close()

        with patch('sys.stdout', new=StringIO()) as fake_out:
            actual(html)
            self.assertEqual(fake_out.getvalue(), expected)


    ########################
    #### Validating UID ####
    ########################
    def test_validating_uid(self):
        def is_valid(uid):
            ''' v It must contain at least 2 uppercase English alphabet characters. A-Z
                v It must contain at least 3 digits (0 - 9).
                v It should only contain alphanumeric characters (a-z, A-Z & 0-9).
                v No character should repeat.
                v There must be exactly  characters in a valid UID.'''
            if len(uid)!=10:
                return False
            if len([c for c in uid if c in ascii_uppercase]) < 2:
                return False
            if len([i for i in uid if i in digits]) < 3:
                return False
            if not uid.isalnum():
                return False
            if len(set(uid)) != len(uid):
                return False
            return True

        self.assertFalse(is_valid("B1CD102354"))
        self.assertTrue(is_valid("B1CDEF2354"))


    ########################################
    #### Validating Credit Card Numbers ####
    ########################################
    def test_validating_credit_card_numbers(self):
        def actual(card):
            if not bool(re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$', card)):
                return False;
            card = card.replace('-', '')
            if bool(re.search(r'(\d)\1{3,}', card)):
                return False
            return True

        for cn in ['4253625879615787', '4424424424442444', '5122-2368-7954-3214']:
            self.assertTrue(actual(cn))

        for cn in ['42536258796157867',      #17 digits in card number → Invalid 
                   '4424444424442444',       #Consecutive digits are repeating 4 or more times → Invalid
                   '5122-2368-7954 - 3214',  #Separators other than '-' are used → Invalid
                   '44244x4424442444',       #Contains non digit characters → Invalid
                   '0525362587961578']:      #Doesn't start with 4, 5 or 6 → Invalid
            self.assertFalse(actual(cn))


    #################################
    #### Validating Postal Codes ####
    #################################
    def test_validating_postal_codes(self):
        ''' A postal code must be a number in the range of (100000 - 999999).
            A postal code must not contain more than one alternating repetitive digit pair '''

        def actual(postal_code):
            valid_digit = bool(re.search(r'^[1-9]\d\d\d\d\d$', postal_code))
            few_alternating_pairs = len(re.findall(r'(\d)(?=\d\1)', postal_code)) <= 1
            return valid_digit and few_alternating_pairs

        # Here, 1 is an alternating repetitive digit.
        self.assertTrue(actual('121426'))
        # Here, NO digit is an alternating repetitive digit.
        self.assertTrue(actual('523563'))
        # Here, both 2 and 5 are alternating repetitive digits.
        self.assertFalse(actual('552523'))


    #######################
    #### Matrix Script ####
    #######################
    def test_matrix_script(self):
        def actual(mat):
            s = ''.join([''.join(c) for c in zip(*mat)])
            res = re.sub(r'(?<=\w)[ !@#$%&]+(?=\w)', ' ', s)
            return res
        
        mat = '''Tsi
                 h%x
                 i #
                 sM 
                 $a 
                 #t%
                 ir!'''
        mat = lstrips(mat).splitlines()
        self.assertEqual(actual(mat), "This is Matrix#  %!")


if __name__ == "__main__":

    unittest.main()
