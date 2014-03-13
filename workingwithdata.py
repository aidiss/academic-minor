#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  workingwithdata.py
# This script is intended to work with csv tables. Data imnport will be in two tables a) node table and b) edge table. Node table will contain discipline names and number of entries. Edge table will have.

import csv, time
import networkx as nx

#1)read edge file, 2) get info from 'is_vdu' file, 3create a dictionary, 4transform to json

def get_entry_info( tempname ):
    with open('is_vdu.csv', 'rb') as csvnodefile:
        spamreader1 = csv.reader(csvnodefile)
        for row in spamreader1:
            if tempname == row[0]: # if the username shall be on column 3 (-> index 2)
                try:
                    return AVERAGE(row[3:7]) # taip turetu veikt
                    return (int(row[3]) + int(row[4]) + int(row[5]) + int(row[6]) + int(row[7]))/5  # cia gal irgi problema
                except:
                    pass
                    
def AVERAGE( skaiciai ):
    skaiciai  = [int(x) for x in skaiciai if x!='']   # perfiltruoja, kad imtu tik tuos, kurie netusti, ir paverstu juos skaiciais (is teksto)
    return 1.0*sum(skaiciai)/len(skaiciai)   # bet jei bus None, vel beda...

def get_edges_of_academicminor():
    print "\nReading edges from Gephi CSV export"
    global completelist
    source = ''
    target = ''
    type = 'Directed'
    weight = 0
    weighted = 0
    weightedweight = 0
    entry = []
    completelist = []
    with open('140312 [Edges].csv', 'rb') as csvedgefile:
        spamreader2 = csv.reader(csvedgefile)
        for row in spamreader2:
            source = row[0]
            target = row[1]
            type = 'Directed'
            weight = row[5]
            weighted = get_entry_info(source)
            #~ print "weight, weighted:", weight, weighted # taip galima pracheckint kurio truksta
            if weight != None  and weighted != None:
                weightedweight = float(weight) / weighted ####<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<####<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<####<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            else:
                weightedweight = None # kad kintamasis neprapultu
            entry = [source, target, type, weight, weighted, weightedweight]
            completelist.append(entry)
            completelist.sort(key = lambda row: row[5])

get_edges_of_academicminor()
count = 0

for x in completelist:
    count += 1
print "Total edges found:", count, '\n\n'
    #~ if x[5] > 0.1:
        #~ ', x

def writeEdgeStatCSV():
    print "Writing a edge CSV"
    with open('thenewedgelist.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for y in completelist:
            spamwriter.writerow(y)
    print "Complete.\n\n"

writeEdgeStatCSV()

secondlist = []
first = x[0]

print "Creating a list of unique nodes..."
count = 0
with open('is_vdu.csv', 'rb') as csvnodefile:
    spamreader1 = csv.reader(csvnodefile)
    for x in spamreader1:
        count += 1
        secondlist.append(x[0])

print "Complete.", count, 'unique nodes found.\n\n'

templist = [] #pilnas sarasas
tempprog = [] #apie viena programa
oneprog = [{'progname':'filosofija'}, {'outunique':'10'}, {'weightedweightsum':'0'}]
tempdict = {}


print "Creating stats for each node..."
for x in secondlist:
    count1 = 0
    outuniquecount = 0
    tempdict['programname'] = x
    sumsum = 0
    for y in completelist:
        if x == y[0]:
            count1 += 1
            if y[5] != None:
                sumsum += float(y[5]) 
                #~ print float(y[5]) 
            else:
                pass #weightedweight = None # kad kintamasis neprapultu
    tempdict['outunique'] = count1
    tempdict['weightedweightsum'] = sumsum
    #~ print tempdict
    templist.append(dict(tempdict))
print "Complete", len(templist), '.\n\n'

def writeNodeStatCSV(templist):
    print "Writing a node CSV"
    temp = []
    with open('thenewnodelist.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for y in templist:
            temp = []
            temp.append(y['programname'])
            temp.append(y['outunique'])
            temp.append(y['weightedweightsum'])
            spamwriter.writerow(temp)
    print "Complete.\n\n"

writeNodeStatCSV(templist)


              


