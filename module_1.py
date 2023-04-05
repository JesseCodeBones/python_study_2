#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '


__author__ = 'Jesse Chen'

def test():
    print("hello from jesse module")

if __name__ == '__main__':
  #  当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
    test()
