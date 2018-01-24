# -*- coding: utf-8 -*-
'''
Utah Python North - 1/17/2018
Chris Cox - @chrisrycx, chrisrycx@github.io 

Functions
- What is a function?
    -- Section of code that can be reused
- Why use functions?
    -- cleaner code
    -- more efficient code
    -- modular code
    -- encapsulates variables, namespaces/scope

Decorators
- What is a decorator?
    -- Expands a functions capabilities without changing actual function
   
'''
from random import randrange,sample


def main():

    pythonistas = ['DrChebib','PilotPrepperAndy','Dirk','Brett','Keith','John','Chris']

     #---------- Function Basics ------------
    #Basic function
    #winner = prizewinner(pythonistas)
    #print(winner)

    #Function with arguments
    #winners = prizewinners(names=pythonistas)
    #print(winners)


    #Function with keyword args and reverse position
    #winners = prizewinners2(number=2,names=pythonistas)
    #print(winners)
   
    #Function with variable number of arguments

    #---------- Function Details -----------
    #Return a function/closure
    #myfunc = getwinners2(prizewinners2)
    #winners = myfunc(pythonistas,3)
    #print(winners)
    
    #Assign a function to variable
    
    #---------- Decorators ----------------
    #Congrats decorator
    winners = prizewinners2(pythonistas,3)
    print(winners)


def startswith(letter):
    '''
    Decorator with parameters
    '''
    def inner(func):
        def _func_(names,number):
            results = func(names=names,number=number)
            return [x for x in results if x[0]==letter]
        return _func_
    return inner


def sortnames(func):
    '''
    Decorator that sorts names
    '''
    def new_func(names,number):
        results = func(names=names,number=number)
        print('In sort:',results)
        return sorted(results) 
    return new_func

def congrats(func):
    '''
    Decorator that adds congrats to winners
    '''
    def new_func(names,number):
        results = func(names=names,number=number)
        print('In congrats:',results)
        return ['Congrats '+ x for x in results] 
    return new_func

def getwinners2(func):
    '''
    Function that takes a function
    '''
    def new_func(names,number):
        return func(names=names,number=number)
    return new_func

def getwinners(func,names,number):
    '''
    Function that takes a function
    '''
    func_parms={'names':names,'number':number}
    winners = func(**func_parms)
    return winners


@congrats
@sortnames
@startswith('D')
def prizewinners2(**kwargs):
    '''
    This function returns a winner from list. Variable arguments.
    ''' 
    #print(kwargs)
    #print(type(kwargs))
    winners = sample(kwargs['names'],kwargs['number'])
    print('in prize')
    return winners

def prizewinners(names,number=1):
    '''
    This function returns a winner from list
    '''    
    winners = sample(names,number)
    return winners

def prizewinner(names):
    '''
    This function returns a winner from list
    '''    
    winner = names[randrange(0,len(names),1)]
    return winner

if __name__ == '__main__':
    main()

