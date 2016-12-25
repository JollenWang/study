#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

from chapter_11_survey import AnonymousSurvey

question = "What language is your first learn to speak?"
my_survey = AnonymousSurvey(question)

if __name__ == "__main__":
    my_survey.show_question()
    print("Enter 'Q' or 'q' to quit.\n")
    while True:
        response = input("language: ")
        if response == 'Q' or response == 'q':
            break
        my_survey.store_response(response)

    print("Thank you for the survey!")
    my_survey.show_results()
