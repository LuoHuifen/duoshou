# -*- coding: utf-8 -*-
from read_file import read_file
from write_file import file_init
from statistics import *

data_list = []
'''
data_list= [data1, data2, data3]
data = {
    "pay_num": 0.0,
    "pay_type": '',
    "pay_time": '',
    "pay_object": '',
}
'''


if __name__ == '__main__':
    # 初始化一下输出文件的环境
    # 默认把结果写到result/result.txt
    # 你可以用file_init('a.txt')改变输出文件名
    file_init()
    # 读取config配置的csv文件
    read_file(data_list)
    # 简单的统计
    count(data_list)
    # 统计50~100的消费和收入
    select_cost_between(50, 100, data_list)
    # 只统计50~100的消费
    select_cost_between(50, 100, data_list, pay_only=True)
    # 统计在某些商家上的消费
    spend_on_seller('饿了么', data_list)
    spend_on_seller('Apple', data_list)
    spend_on_seller('麦当劳', data_list)
    spend_on_seller('KFC', data_list)
    spend_on_seller('华莱士', data_list)
    # 按照支付对象分类统计，从小到大排序，正数为输出，负数为收入
    group_by_seller(data_list)