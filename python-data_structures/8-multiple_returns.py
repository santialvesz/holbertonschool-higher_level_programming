#!/usr/bin/python3
def multiple_returns(sentence):
    new_sen = ()
    if len(sentence) == 0:
        new_sen = 0, "None"
    else:
        new_sen = len(sentence), sentence[0]
    return new_sen
