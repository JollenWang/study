#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import unittest
from chapter_11_name_func import *

class NameTestCase(unittest.TestCase):
    def test_check_name(self):
        fname = get_formatted_name("jollen", "wang")
        self.assertEqual(fname, "Jollen Wang")
    def test_long_name(self):
        self.assertEqual(get_long_name("albert", "jony", "edthon"), "Albert Jony Edthon")

unittest.main()
