#! /usr/bin/env python3.4
import sys
import os
import math

class Transaction:
    def __init__(self,transType,value):
        if transType != "W" or transType != "D":
            raise ValueError("TransType is incorrect")
        else:
            self.transType = transType
        self.value = value

class Person:
    def __init__(self,firstname,lastname):
        self.firstName = firstname
        self.lastName = lastname
    def __str__(self):
        return self.firstName+" "+self.lastName


class Account:
    def __init__(self,ID,owner,balance):
        self.accountID = ID
        self.owner = owner
        self.balance = balance
        self.minValue = 1000

    def __str__(self):
        if self.balance < 0:
            balance = "($"+str(self.balance*-1)+")"
        else:
            balance = "$"+str(self.balance*-1)+")"
        name = self.owner.firstName+" "+self.owner.lastName
        return self.accountID+", "+name+", Balance = "+balance

    def applyTransaction(self,transaction):
        if transaction.transType == "D":
            self.balance = self.balance + transaction.value
        else:
            checkbal = self.balance - transaction.value
            if checkbal > 0:
                self.balance = int(str('%02d' % checkbal))
                if checkbal < self.minValue:
                    deduct = self.balance - 10
                    self.balance = int(str('%02d' % deduct))
            else:
                raise ValueError("Transaction cannot be completed due to negative balance after transaction")
        return self



class Bank:
    def __init__(self):
        self.accounts = {}

    def createAccount(self,firstname,lastname,accountID):
        if accountID not in self.accounts:
            person = Person.__init__(self,firstname,lastname)
            newAccount = Account.__init__(self,accountID,person,500)
            self.accounts[accountID] = newAccount
        else:
            pass
        return self

    def applyTransaction(self,accountID,transaction):
        if accountID not in self.accounts:
            pass
        else:
            self.accounts[accountID] = Account.applyTransaction(self,transaction)
        return self

