#!/usr/bin/env python

import sys
from collections import defaultdict
#from itertools import combinations

dic = defaultdict(list)

#input: <RFP, fid> 
#All fid's with same RFP would have come here
#for all fid's with same RFP,
# print <fid1 fid2, 1>


for line in sys.stdin:
	line = line.strip()
	wlist = line.split('\t',1)
	dic[wlist[0]].append(wlist[1])

#XXX AMAZON Elastic Mapreduce does not support combinations
#for rfp in dic:
	#fidset = set(dic[rfp])
	#for fidpair in combinations(fidset,2):
	#	print '%s %s\t %s' %(fidpair[0],fidpair[1],1)

for rfp in dic:
	#remove duplicates, convert it back to list
	#set does not support indexing where list does
	fidset = list(set(dic[rfp]))
	for i in range(len(fidset)):
		for j in range(i+1,len(fidset)):
			print  '%s %s\t %s' %(fidset[i],fidset[j],1)
