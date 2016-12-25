#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import unittest
from chapter_11_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_single_response(self):
        question = "What language is you first learned?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn('English', my_survey.responses)

    def test_three_response(self):
        question = "Which language is your favorite?"
        mine = AnonymousSurvey(question)
        mine.store_response("Java")
        mine.store_response("Python")
        mine.store_response("C")

        for response in ["Java", "C", "Python"]:
            self.assertIn(response, mine.responses)

unittest.main()
