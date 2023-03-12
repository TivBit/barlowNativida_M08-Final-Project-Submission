# -*- coding: utf-8 -*-
"""
Creed on %(Date: 23 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: Final Project
"""
class Member():
    def __init__(self, acctVerify, fname, lname, acctNum, acctPin):
        self.acctVerify = acctVerify
        self.fname = fname
        self.lname = lname
        self.acctNum = acctNum
        self.acctPin = acctPin

    def __eq__(self, other):
        if isinstance(other, Member):
            return (self.acctNum == other.acctNum)

    def __repr__(self):
        return f"{self.fname} {self.lname} is a member of SDEV 220 Bank.  {self.fname}'s account number is {self.acctNum}."

class Account(Member):
    def __init__(self, balance, response, withdrawAmount):
        self.balance = balance
        self.response = response
        self.withdrawAmount = withdrawAmount
