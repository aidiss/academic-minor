#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  networkx_gret.py
#  
#  Copyright 2014 Saonkfas <Saonkfas@SAONKFAS-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import csv
import networkx as nx
mdg=nx.MultiDiGraph()

def get_nodes_of_academicminor():
    print ("\nReading nodes from Gephi CSV export")
    nodeid = 0
    nodelabel = ''
    nodefaculty = ''
    nodeweight = ''
    count = 0
    with open('is_vdu.csv', 'rb') as csvnodefile:
        nodereader = csv.reader(csvnodefile)
        for row in nodereader:
            count += 1
            nodeid = row[0]
            #~ psp = row[1]
            #~ gsp = row[2]
            #~ isy2009 = row[3]
            #~ ist2010 = row[4]
            #~ ist2011 = row[5]
            #~ ist2012 = row[6]
            #~ ist2013 = row[7]
            nodelabel = row[1]
            nodefaculty = row[13]
            mdg.add_node(nodeid, label=nodelabel, faculty=nodefaculty)
            #~ print count
get_nodes_of_academicminor()

#~ def add_Edges():
    #~ mdg.addedge
    #~ print
def get_nodeid_by_nodelabel(nodelabel):
    #~ print 'Looking for', nodelabel, 'id'
    for nodeid, attr in mdg.nodes(data=True):
        try:
            #~ print nodeid, attr['label'], mdg.degree(nodeid)
            if nodelabel == attr['label']:
                return nodeid
            #~ print nodelabel, 'id is', nodeid, '\n\n'
        except:
            return None
        

def get_Edges_of_academicminor():
    print ("\nReading Edges from Gephi CSV export")
    sourceid = ''
    targetid = ''
    rawweight = 0
    weighted = 0
    weightedweight = 0
    count = 0
    with open('140312 (Edges).csv', 'rb') as csvedgefile:
        edgereader = csv.reader(csvedgefile)
        for row in edgereader:
            count += 1

            sourcelabel = row[1]
            targetlabel = row[2]
            sourceid = get_nodeid_by_nodelabel(sourcelabel)
            targetid = get_nodeid_by_nodelabel(targetlabel)
            rawweight = row[5]
            #~ if weight != None  and weighted != None:
                #~ weightedweight = float(rawweight) / weighted ####<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<####<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<####<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            #~ else:
                #~ weightedweight = None # kad kintamasis neprapultu
            #~ print sourcelabel, targetlabel
            
            mdg.add_edge(sourceid, targetid, weight=rawweight)
    print (count)
get_Edges_of_academicminor()

#~ print 'printing nodes'
#~ for nid, attr in mdg.nodes(data=True):
    #~ print nid    
           
print ('printing Edges')
count = 0
for sid, tid, attr in sorted(mdg.edges(data=True)):
    count += 1
    print (sid, tid, attr['weight'])
print (count)
            

#~ G1 = nx.read_dot("grafas0227.dot")

#~ get_Edges_of_academicminor()
#~ count = 0
#~ 
#~ 
#~ 
 #~ #id must be number#adds a node
#~ 
#~ 
#~ 
#~ # A container of nodes
#~ h = nx.path_graph(10) 
#~ mdg.add_nodes_from(h) # g now contains the nodes of h
#~ 
#~ # In contrast, you can remove any node of the graph
#~ mdg.remove_node(2) 
#~ 
#~ # Single edge
#~ mdg.add_edge(1,2) 
#~ e=(2,3) 
#~ mdg.add_edge(*e) # unpack edge tuple
#~ # List of Edges
#~ mdg.add_Edges_from([(1 ,2) ,(1 ,3)])
#~ # Container of Edges
#~ mdg.add_Edges_from(h.Edges())
#~ # In contrast, you can remove any edge of the graph
#~ mdg.remove_edge(1,2)
