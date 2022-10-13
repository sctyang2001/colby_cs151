''' lsystem.py (adapted from Lab09) - this overall lab aims to practice working with the L-system and class.
Project09: Unique trees and shapes
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.10, 2020
'''

import random


class Lsystem:
    def __init__(self, filename=None):
        '''L-system class constructor
        Parameters:
        -----------
        filename: str. Filename of the L-system text file with the base string and 1+ replacement rules
        '''
        # Create an instance variable for the base string
        # (initialize as the empty string)
        self.base = ''

        # Create an instance variable for your replacement rules
        # (initialize as an empty list)
        self.rules = []

        # Check if filename passed in (i.e. parameter is not eNone)
        # If so, read in the L-system from the file called
        # filename. Do this by calling the read method
        # (you will implement this shortly)
        if filename != None:
            self.read(filename)


    def getBase(self):
        '''TODO: Method to get the base string
        '''
        return self.base
    

    def setBase(self, newBase):
        '''TODO: Method to set the base string
        '''
        self.base = newBase
    

    def getRule(self, ruleIdx):
        '''TODO: Method to get the rule sublist (a two element list) at index
        '''
        return self.rules[ruleIdx]
    

    def addRule(self, newRule):
        '''TODO: Method to append a new replacement rule newRule to the current list of replacement rules
        '''
        self.rules.append(newRule)
    

    def numRules(self):
        '''TODO: Method that returns the number of replacement rules currently in the L-system
        '''
        return len(self.rules)


    def read(self, filename):
        '''Reads the L-system base string and 1+ rules from a text file. Stores the data in the
        instance variables in the constructor in the format:

        base string: str.
            e.g. `'F-F-F-F'`
        replacement rules: list of 2 element sublists.
            e.g. `[['F', 'FF-F+F-F-FF']]` for one rule

        Parameters:
        -----------
        filename: str. Filename of the L-system text file with the base string and 1+ replacement
            rules
        '''
        # Open the file called filename
        file = open(filename, 'r')
        # Read in the file line-by-line.
        currLine = file.readline()
        # For each line, split it into a list.
        #   If the first list item is 'base', set the L-system base string
        #   to the second item in the list.
        #   If the first list item is 'rule', add a rule to your replacement
        #   rules consisting of the find and replace strings
        #   (2nd and 3rd items in the list).
        #   Remember: We add a rule in list format: [find str, replace str]
        while currLine != '':
            currLine = currLine.split()
            if currLine[0] == 'base':
                self.setBase(currLine[1])
            if currLine[0] == 'rule':
                self.addRule(currLine[1:])
            currLine = file.readline()
        file.close() # Close the file


    def replace(self, currString):
        '''Applies the full set of replacement rules to current 'base' L-system string `currString`.

        Overall strategy:
        - Scan the L-system string left to right, char by char
        - Apply AT MOST ONE replacement rule to a matching character.
            Example: If the current char is 'F' and that matches a rule's find string 'F', apply
           that rule then move onto the next character in the L-system string (don't try to match
           more rules to the current char).
        - If no rule matches a rule find string, we just add the char as-is to the new string.

        Parameters:
        -----------
        currString: str. The current L-system base string.

        Returns:
        -----------
        newString: str. The base string `currString` with replacement rules applied to it.
        '''
        newString = ''
        for char in currString:
            # check to see if char matches a find string in rules
            found = False
            for rule in self.rules:
                # Loop through rules
                if char == rule[0]:
                    newString += random.choice(rule[1:])
                    found = True
                    break
            if not found:
                newString += char
        return newString


    def buildString(self, n):
        '''Starting with the base string, apply the L-system replacement rules for `n` iterations.

        You should NOT change your base string instance variable here!

        Parameters:
        -----------
        n: int. Number of times you go through the L-system string to apply the replacement rules.

        Returns:
        -----------
        str. The L-system string after apply the replacement rules `n` times.
        '''

        string = self.getBase()
        for i in range(n):
            string = self.replace(string)
        return string