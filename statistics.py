# -*- coding: utf-8 -*-

from write_file import write
import re
import time


# 简单统计
def count(data_list):
    pay = 0.0
    income = 0.0
    expenses = {}

    for data in data_list:
        if data['pay_type'] == '支出':
            pay = round(pay + data['pay_num'], 2)
            key = str(data['pay_time'].tm_year) + ' ' + str(data['pay_time'].tm_mon).zfill(2)
            if key not in expenses.keys():
                expenses[key] = 0.0
            expenses[key] = round(expenses[key] + data['pay_num'], 2)
        elif data['pay_type'] == '收入':
            income = round(income + data['pay_num'], 2)
            key = str(data['pay_time'].tm_year) + ' ' + str(data['pay_time'].tm_mon).zfill(2)
            if key not in expenses.keys():
                expenses[key] = 0.0
            expenses[key] = round(expenses[key] - data['pay_num'], 2)

    write('支出：', pay)
    write('收回：', income)
    write('实际支出：', round(pay - income, 2))
    write(' ')
    expenses_list = sorted(expenses.items(), key=lambda x: x[0])
    for item in expenses_list:
        write(item)
    write('===================================')


# 统计在某个商家的消费
def spend_on_seller(name, data_list):
    pay = 0.0

    for data in data_list:
        if re.search(name, data['pay_object']):
            if data['pay_type'] == '支出':
                pay = round(pay + data['pay_num'], 2)
                write(time.strftime("%Y-%m-%d %H:%M:%S", data['pay_time']), data['pay_object'], data['pay_num'])
            elif data['pay_type'] == '收入':
                pay = round(pay - data['pay_num'], 2)
                write(time.strftime("%Y-%m-%d %H:%M:%S", data['pay_time']), data['pay_object'], data['pay_num'], '收入')

    write(name, '的总消费：', pay)
    write('===================================')


# 按商家分类
def group_by_seller(data_list):
    pay_dict = {}

    for data in data_list:
        if data['pay_object'] not in pay_dict:
            pay_dict[data['pay_object']] = 0.0
        if data['pay_type'] == '支出':
            pay_dict[data['pay_object']] = round(pay_dict[data['pay_object']] + data['pay_num'], 2)
        elif data['pay_type'] == '收入':
            pay_dict[data['pay_object']] = round(pay_dict[data['pay_object']] - data['pay_num'], 2)

    pay_list = sorted(pay_dict.items(), key=lambda x: x[1])
    for value in pay_list:
        write(str(value).replace(' ', ''))
    write('===================================')


# 统计某个区间的消费和收入
def select_cost_between(min, max, data_list, pay_only=False):
    pay = 0.0

    for data in data_list:
        if not (min < data['pay_num'] < max):
            continue
        if data['pay_type'] == '支出':
            pay = round(pay + data['pay_num'], 2)
            write(time.strftime("%Y-%m-%d %H:%M:%S", data['pay_time']),
                  data['pay_object'], data['pay_num'])
        elif data['pay_type'] == '收入' and pay_only is False:
            pay = round(pay - data['pay_num'], 2)
            write(time.strftime("%Y-%m-%d %H:%M:%S", data['pay_time']),
                  data['pay_object'], data['pay_num'], '收入')

    write(str(min) + '~' + str(max), '的总消费：', pay)
    write('===================================')
