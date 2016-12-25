#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import unittest
from chapter_11_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What is your favorite language?"
        self.survey = AnonymousSurvey(question)
        self.favorites = ["C", "Python", "Java", "Go"]

    def test_single_response(self):
        self.survey.store_response(self.favorites[0])
        self.assertIn(self.favorites[0], self.survey.responses)

    def test_three_response(self):
        for i in range(0, 4):
            self.survey.store_response(self.favorites[i])
        #for response in self.favorites:
        #    self.survey.store_response(response)
        for response in self.favorites:
            self.assertIn(response, self.survey.responses)

unittest.main()
