#!/usr/bin/python3

import unittest
from code_print import Document

class CodePrintTest(unittest.TestCase):

    def test_one_line(self):
        lines = ['hello']
        doc = Document(max_lines=30)
        doc.add_lines(lines)

        self.assertEqual(doc.get_size(), 1)
        self.assertEqual(doc.get_content(0), 'hello')

    def test_two_lines(self):
        lines = ['hello\n', 'I am Jinsung\n']
        doc = Document(max_lines=30)
        doc.add_lines(lines)

        self.assertEqual(doc.get_size(), 1)
        self.assertEqual(doc.get_content(0), 'hello\nI am Jinsung\n')

    def test_three_lines(self):
        chunk = ['hello\n', 'I am Jinsung\n', 'Bye bye\n']
        doc = Document(max_lines=2)
        doc.add_lines(chunk)

        self.assertEqual(doc.get_size(), 2)
        self.assertEqual(doc.get_content(0), 'hello\nI am Jinsung\n')
        self.assertEqual(doc.get_content(1), 'Bye bye\n')

    def test_line_threetimes(self):
        lines = ['hello\n', 'I am Jinsung\n', 'Bye bye\n']
        doc = Document(max_lines=2)
        for line in lines:
            doc.add_lines([line])

        self.assertEqual(doc.get_size(), 2)
        self.assertEqual(doc.get_content(0), 'hello\nI am Jinsung\n')
        self.assertEqual(doc.get_content(1), 'Bye bye\n')

#execution part
unittest.main()

