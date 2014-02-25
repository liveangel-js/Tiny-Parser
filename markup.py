# -*- coding: cp936 -*-
# python 2.7
#python markup.py <test.txt> test.html
import sys,re
from handlers import *
from util import *
from rules import *
class Parser:
    def __init__(self,handler):
        self.handler=handler
        self.rules=[]
        self.filters=[]
    def addRule(self,rule):
        self.rules.append(rule)
    def addFilter(self,pattern,name):
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    def parse(self,file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block,self.handler)
                    if last:
                        break
        self.handler.end('document')
class BasicTextParser(Parser):
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(ListRule())
        self.addRule(HeadingRule())
        self.addRule(TitleRule())
        self.addRule(ListItemRule())
        self.addRule(ParagraphRule())
        self.addFilter(r'\*(.*?)\*','emphasis')
        self.addFilter(r'(http://[\.a-zA-z/]+)','url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z])','mail')
handler = HTMLRenderer()
parser=BasicTextParser(handler)

parser.parse(sys.stdin)
        
        
