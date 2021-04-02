'''
schoolsIndexMap.py
  Author(s): Jason Kyle Tan (1134487)

  Project: Team Group Project
  Date of Last Update: March 18, 2021

  Functional Summary
    This file is being used to hold the constants of the index map
    used in the following files:
        extractConfirmedStudentCases.py
        extractSchoolIDs.py
    
    They are stored in this file to remove redundancy in the final program,
    having to write multiple index maps.

     Commandline Parameters: 0

  Command to run: No command required
'''

INDEX_MAP = {
    "COLLECTED_DATE": 0,
    "REPORTED_DATE": 1,
    "SCHOOL_BOARD": 2,
    "SCHOOL_ID": 3,
    "SCHOOL": 4,
    "MUNICIPALITY": 5,
    "CONFIRMED_STUDENT_CASES": 6,
    "CONFIRMED_STAFF_CASES": 7,
    "CONFIRMED_UNSPECIFIED_CASES": 8,
    "TOTAL_CONFIRMED_CASES": 9
}