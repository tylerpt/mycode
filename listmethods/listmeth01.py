#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
print(proto[1])
#proto.extend('dns') #this line will add d, n, and s
proto.append('dns') #will add "dns" to the end of the list
protoa.append('dns') #will add "dns" to the end of the list
print(proto)
proto2 = [22,80,443,53] #list of common ports
proto.extend(proto2) #pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2)#pass proto2 as an arguemtn to the append method
print(protoa)