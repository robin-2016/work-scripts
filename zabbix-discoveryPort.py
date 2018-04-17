#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os,json

def isport(x):
	if x == '10050\n' or x == '22\n'or x == '25\n':
		return False
	else:
		return True

port_list ={"data":None}
cmd = "ss -tnlp|awk {'print $4'}|awk -F':' '{if ($NF~/^[0-9]*$/) print $NF}'|sort |uniq 2>/dev/null"
local_ports = filter(isport,os.popen(cmd).readlines())
# test_ports = os.popen(cmd).readlines()
port_list["data"] = [{"{#TCP_PORT}":port.replace("\n","")} for port in local_ports]
port_json = json.dumps(port_list,sort_keys=True,indent=4)    #sort_keys排序   indent缩进
print(port_json)
