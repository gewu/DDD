# -*- coding: utf-8 -*-
"""
@author: kangkona
"""
import re
import csv

config = {"src":"data/t_alibaba_data_test.csv","dst":"data/t_alibaba_data_rm_cn.csv"}

def data_rm_cn(src,dst):
    '''把visit_datetime中的5月6号这样中文日期格式转换为20130506'''
    src_text = open(src,"r").read()
    csvfile = file(dst, 'wb')
    fout = csv.writer(csvfile)

    mouth_day = re.compile(r"日|月")
    dst_text  = mouth_day.sub(",",src_text)
    dst_text  = re.sub(",\n","\n",dst_text) 
     
    dst_text_records = dst_text.split("\n")
    fout.writerow(dst_text_records[0].split(","))
    dst_text_records = dst_text_records[1:-1]
    
    for record in dst_text_records:
        items = record.split(",")
        if len(items[-1]) == 1:
            items[-1] = "0" + items[-1]
        if len(items[-2]) == 1:
            items[-2] = "0" + items[-2]
        items[-2] = "2013"+items[-2] + items[-1]
        items = items[:-1]
        fout.writerow(items)
        
    csvfile.close()
         


def main():
    data_rm_cn(config["src"],config["dst"])
    print "Finished."

if __name__ == '__main__':
    main()