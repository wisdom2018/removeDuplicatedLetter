#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/17 1:48 PM
# @Author: wisdom
# @File:removeDuplicatedCharacter.py

def removeDuplicateLetters(s: str) -> str:
    stack = []
    for idx, char in enumerate(s):
        if char in stack: continue
        while stack and char < stack[-1] and stack[-1] in s[idx:]:
            stack.pop()
        stack.append(char)
    return "".join(stack)



if __name__ == '__main__':
    print('remove duplicated character')
    strings = input()
    print(strings)
    print(removeDuplicateLetters(strings))
