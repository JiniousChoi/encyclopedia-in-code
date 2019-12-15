#!/usr/bin/python3

'''
This scripts returns newly arranged code for prettier python code to be printed
Python code, of all languages, shows very awful readability when a function is
split into two parts across two pages.

Feed whatever python code to print to this script, and then it inserts empty
lines, hence as few segmented functions as possible

Scripted by jinchoiseoul@gmail.com
'''

class Document:
    
    def __init__(self, max_lines=30):
        self.nline = max_lines
        self.doc = [Page(self.nline)]


    def _add_line(self, line):
        '''만약 페이지가 부족하다면 추가해서라도 line 추가'''
        self.doc[-1].add_line(line)


    def add_lines(self, lines):
        '''lines is considered as an atomic chunk to be added in a page'''
        self._adjust_page_idx(len(lines))
        
        #now, lines can be added sequentially
        for line in lines:
            try:
                self._add_line(line)
            except PageOverflowException:
                self.doc.append(Page(self.nline))
                self._add_line(line)

    
    def get_size(self):
        return len(self.doc)
            

    def get_content(self, page_no):
        '''page_no is zero-based'''
        page = self.doc[page_no]
        return page.printer()


    def _adjust_page_idx(self, n_line):
        '''Makes sure given lines can be added line by line in the last page
        1. 공간이 충분하다면 통과
        2. 공간이 부족하다면,
         - 만약 lines가 어차피 한페이지에 담기지 못한 만큼 크다면 통과
         - 만약 lines가 한페이지에는 들어갈 수 있다면, 새 마지막페이지를 만들고 종료(자동으로 거기부터 추가되게 됨)
        '''
        if n_line <= self.nline and not self._addable(n_line):
            self.append_new_doc()


    def append_new_doc(self):
        self.doc.append(Page(self.nline))


    def _addable(self, n_line):
        '''Returns if last page has enough room'''
        doc = self.doc
        if len(doc)==0:
            return False

        last_page = doc[-1]
        n_rest = last_page.get_rest_line_cnt()
        if n_rest >= n_line:
            return True
        else:
            return False

    def printer(self):
        for i,page in enumerate(self.doc):
            print(i, page.printer())

class PageOverflowException(Exception):
    pass

class Page:
    
    def __init__(self, max_lines):
        if not max_lines or not isinstance (max_lines, int):
            raise Exception
        self.lines = []
        self.max_lines = max_lines

    def add_line(self, line):
        if len(self.lines) >= self.max_lines:
            raise PageOverflowException
        self.lines.append(line)
    
    def printer(self):
        return ''.join(self.lines)
    
    def get_rest_line_cnt(self):
        return self.max_lines - len(self.lines)


def code_print(original):
    '''Returns rearranged'''
    result = []
    
    state = Stage()
    
    for line in original.splitlines():
        stage.feed(line)
        if state.state == 'in-chunk':


if __name__=='__main__':
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', dest='file')
    options, remainer = parser.parse_args()

    fname = options.file
    with open(fname, 'r') as fp:
        orig = fp.read()
        rearranged = code_print(orig)
        print(rearranged)
