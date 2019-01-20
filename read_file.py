# -*- coding: utf-8 -*-
import csv
import re
import time

from config import alipay_list, wechatpay_list


def read_file(data_list):
    for file in alipay_list:
        read_alipay_file('./csv/' + file, data_list)
    for file in wechatpay_list:
        read_wechatpay_file('./csv/' + file, data_list)

def read_alipay_file(file_name, data_list):
    start = False
    csv_reader = csv.reader(open(file_name, encoding='utf-8'))
    for row in csv_reader:
        if re.search('交易号', row[0]):
            start = True
            continue
        elif re.search('--------------------------', row[0]) and start:
            break
        if start:
            data = {
                "pay_num": float(row[9]),
                "pay_type": '',
                "pay_time": time.strptime(row[2], "%Y/%m/%d %H:%M"),
                "pay_object": row[7].strip(),
                'id': row[0]
            }
            if re.search('支出', row[10]):
                data['pay_type'] = '支出'
            elif re.search('收入', row[10]):
                data['pay_type'] = '收入'
            else:
                continue
            data_list.append(data)
    print(file_name + "读取完成")


def read_wechatpay_file(file_name, data_list):
    start = False
    csv_reader = csv.reader(open(file_name, encoding='utf-8'))
    for row in csv_reader:
        if re.search('交易时间', row[0]):
            start = True
            continue
        if start:
            data = {
                "pay_num": float(row[5].strip('¥')),
                "pay_type": '',
                "pay_time": time.strptime(row[0], "%Y-%m-%d %H:%M:%S"),
                "pay_object": row[2].strip() if row[2] != '/' else row[1].strip(),
                'id': row[8]
            }
            if re.search('支出', row[4]):
                data['pay_type'] = '支出'
            elif re.search('收入', row[4]):
                data['pay_type'] = '收入'
            else:
                continue
            data_list.append(data)
    print(file_name + "读取完成")
