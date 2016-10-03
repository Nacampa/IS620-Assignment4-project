# IS620 - Assignment 4
# Program: assignment4.py
# Student: Neil Acampa
# Date:    09/23/16
# Function: To create a graph database with at least one categorical node
#           and to perform centrality measures (Degree and Eigenvector)
#           and then to perform these across nodes

#           Read in movie data from IMDB and test on a small sample. Create nodes and graph
#           Headings: Title,year,length,budget,rating (Using Movie info and average rating)
#           Headings: votes,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,mpaa	(Not using)
#           Headings: Action,Animation,Comedy,Drama,Documentary,Romance,Short (Using Movie Genra)

#           09/23/16: Read in a few records from movie database and parsed data	  Complete
#           09/24/16: Read in entire database using ipython and partse 		  Complete
#  	    09/25/16: Next create small graph				          Complete
#           09/25/16: Nodes and Edges created for 300 records			  Complete
#           09/25/16: Display Graph						  Complete
#           09/26/16: Working on displaying simple graph and graph with labels
#           09/26/16: Able to do a movie genra degree centrality		  Complete
#           09/26/16: Need to get tvalue for dof (58791)  at 99.5% ci		  Complete

#           09/26/16: Need to put genra stats in table				  Not started

#           09/29/16: Create a randomly generated array of 200 numbers from 	  Complete
#                     58,798 records for stats and graph

#           09/29/16: Display a few nodes and 1 few edges			  Not started

#           09/29/16: Put all repeatable routines in functions			  Not Started
#           09/29/16: Add Degree for each genra, show results and execute T-test  Started in ver all2
#                   : Do above but with genra =  str("Drama") + "-" + movieyear





from __future__ import absolute_import 
from __future__ import division
import re
import os 
import math
import decimal
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import networkx as nx
import random
#from prettytable import prettytable


# Movie nodes
movietitle =[]
movieyear  =[]
movielength=[]

# Posible Edge Value
rating=[]

# Genra Nodes
actiongenra=[]
animationgenra=[]
comedygenra=[]
dramagenra=[]
docgenra=[]
romancegenra=[]
shortgenra=[]

linelst=[]
lines  = ""



def parse_data(linelst):
 """Parse each line and update arrays"""

 movietitle.append(linelst[0])
 movieyear.append(linelst[1])
 movielength.append(linelst[2])
 rating.append(linelst[4])
 actiongenra.append(linelst[17])
 animationgenra.append(linelst[18])
 comedygenra.append(linelst[19])
 dramagenra.append(linelst[20])
 docgenra.append(linelst[21])
 romancegenra.append(linelst[22])
 shortgenra.append(linelst[23])
 return


if __name__ == "__main__":
 linecnt    = 0
 print
 print
 filepath=""
 valid = 0
 print ("Enter the Full File Path including the File")
 print ("or Press return to use File Path c:\movie.tab")
 filepath = raw_input("Please enter the File Path now ")
 valid = 0
 if filepath == "":
     filepath = "c:\movies.tab" 

 print filepath
 try:
       f = open("c:\movies.tab","r")
       try:
         valid=1
         for lines in f:
           lines = lines.rstrip()
           linelst = lines.split("\t");
           movietitle.append(linelst[0])
           movieyear.append(linelst[1])
           movielength.append(linelst[2])
           rating.append(linelst[4])
           actiongenra.append(linelst[17])
           animationgenra.append(linelst[18])
           comedygenra.append(linelst[19])
           dramagenra.append(linelst[20])
           docgenra.append(linelst[21])
           romancegenra.append(linelst[22])
           shortgenra.append(linelst[23])

       finally:
         f.close()
 except IOError:
       print "File not Found - Program aborting"

 if not(valid):
     exit()
 
 p = 1;
 totallen = len(movietitle)

 # Critical values for 99 and 95 percent one sided T-Test
 cv     = 3.143
 cv1    = 1.943

 print ("The data was found at www.imdb.com")
 print ("The Movie database consists of movie title, length in minutes, year released, avg rating and movie genre")
 print 
 print ("Two nodes were created, one Movie with attributes movie title, year and rating")
 print ("The second is Genre consisting of 7 Genres (Action, Animation, Comedy, Drama, Documentary, Romance and Short")
 print
 print ("An edge is created linking Movie and Genra based on a 0,1 entry in file")
 print ("with Edge properties: year and rating")
 print
 print ("Two centrality measures are calculated: Degree and Eigenvector")
 print 
 print ("Degree Centrality: Is a measure of the number of edges or links incident upon a node.")
 print ("In Degree Centrality a nodes importance increases with the number of in or outbound edges")
 print ("Inbound edges indicate popularity, output indicate influence")
 print ("A specific node: Genre is important because there are many movies linked to that Genre")
 print
 print ("Eigenvector Centrality: Measures the importance of a node based on its connectivity to  other important nodes")
 print ("It assigns numbers to each node based on this relationship")
 print
 print ("Example: 'Comedy' has high degree centrality and the 'Romance' has low degree centrality")
 print ("A database with many 'Romantic Comedies' may have a higher relative 'Romance' eigenvector measure")
 print ("by virtue of its associaton with the 'Comedy' ")
 print ("Shorts may also have a higher eigenvector measure due to the association with Comedy or Drama")
 print 
 print
 print ("One sided T-tests have been run at a 99 percent CI alpha of .01 with CV: %.3f") % (cv)
 print ("                            and at a 95 percent CI alpha of .05 with CV: %.3f") % (cv1)
 print
 print ("Statistics have been gathered on a random sample of 150 data points")
 print ("                              on a random sample of 300 data points")
 print ("                        and for the entire db of 58,789 data points")
 print
 print
 print
 print


 while (p <=3):
  if (p == 1):
   k = 150
  else:
   if (p == 2):
     k = 300
   else:
     k = totallen

 
# Do 2 passes first on a small subset of the data base
# Pass 2 on the entire db - but no graph

# For now do graph on 200 nodes and later do random 
# Get k times without replacement for total length (58,789) and put keys in array
  
   
  m = []
  m = random.sample(xrange(totallen), k)
  l = k
 
  
  
 
#   Test  node creation
#   Later test with all records using l - Also put all in function(s)
  
  
  g = nx.Graph()
  g.clear()
  glabels=[]
  mlabels=[]

  # Arrays for Degree by Genra and Genra's outside of 99.5% CI
  genra_degree  = []
  genra_deg_sig = []
  genra_deg_per = []


# Arrays for Eigenvector Centrality by Genra and Genra's outside of 99.5% CI
  eigencntrl      = []
  eigensig        = []


# Arrays for Betweenness Centrality by Genra and Genra's outside of 99.5% CI
  betweencntrl    = []
  betweensig      = []

# Arrays for Closeness Centrality by Genra and Genra's outside of 99.5% CI
  closecntrl    = []
  closesig      = []


  # Create Movie Nodes
  for x in range(l):
    i = m[x]
    g.add_node(i, movietitle=movietitle[i], movieyear = movieyear[i], rating = rating[i])


 
  
 # Create genra nodes
  g.add_node("g1", genre="action")
  g.add_node("g2", genre="animation")
  g.add_node("g3", genre="comedy")
  g.add_node("g4", genre="drama")
  g.add_node("g5", genre="documentary")
  g.add_node("g6", genre="romance")
  g.add_node("g7", genre="short")


 # Create Genre labels for lookup in Degree and Eigvector centrality arraays
  glabels = []
  glabels.append("Action")
  glabels.append("Animation")
  glabels.append("Comedy")
  glabels.append("Drama")
  glabels.append("Documentary")
  glabels.append("Romance")
  glabels.append("Short")

# Create Genre Labels for output
  glabelsout = []
  glabelsout.append("Action     ")
  glabelsout.append("Animation  ")
  glabelsout.append("Comedy     ")
  glabelsout.append("Drama      ")
  glabelsout.append("Documentary")
  glabelsout.append("Romance    ")
  glabelsout.append("Short      ")

# Create Genre Headings
  gheadings=[]
  gheadings.append("Genre      ")
  gheadings.append("Degree")
  gheadings.append("Deg Per")
  gheadings.append("Sig")
  gheadings.append("Eign")
  gheadings.append("Sig")

  
  glabels = np.array(glabels)
  totalgenra = 7

   
  # Create Movie labels used in graph
  for i in range(l):
    temp = str(movietitle[i])
    mlabels.append(temp)
   

  mlabels = np.array(mlabels)



 # Create Edges
 # For second graph Edges will be created for Genra-year of movie release
  for x in range(l):
    i = m[x]
    if (actiongenra[x] == '1'):
      g.add_edge(i, glabels[0], avg_user_rating = rating[i], year_released = movieyear[i])
      gn = glabels[0] + str(movieyear[i])
      #g.add_edge(i,gn, avg_user_rating = rating[i], year_released = movieyear[i])



  for x in range(l):
    i = m[x] 
    if (animationgenra[x] == '1'):
      g.add_edge(i, glabels[1], avg_user_rating = rating[i], year_released = movieyear[i])
      gn = glabels[1] + str(movieyear[i])
      #g.add_edge(i,gn, avg_user_rating = rating[i], year_released = movieyear[i])
      


  for x in range(l):
    i = m[x]
    if (comedygenra[i] == '1'):
      g.add_edge(i, glabels[2], avg_user_rating = rating[i], year_released = movieyear[i])
      gn = glabels[2] + str(movieyear[i])
      #g.add_edge(i,gn, avg_user_rating = rating[i], year_released = movieyear[i])
      


  for x in range(l):
    i = m[x]
    if (dramagenra[x] == '1'):
      g.add_edge(i, glabels[3], avg_user_rating = rating[i], year_released = movieyear[i])
      gn = glabels[3] + str(movieyear[i])
      #g.add_edge(i,gn, avg_user_rating = rating[i], year_released = movieyear[i])
      

  for x in range(l):
    i = m[x]
    if (docgenra[i] == '1'):
      g.add_edge(i,glabels[4], avg_user_rating = rating[i], year_released = movieyear[i])
      gn = glabels[4] + str(movieyear[i])
      #g.add_edge(i,gn, avg_user_rating = rating[i], year_released = movieyear[i])
      

  for x in range(l): 
    i = m[x]
    if (romancegenra[i] == '1'):
      g.add_edge(i, glabels[5], avg_user_rating = rating[i], year_released = movieyear[i])
      gn = glabels[5] + str(movieyear[i])
      #g.add_edge(i,gn, avg_user_rating = rating[i], year_released = movieyear[i])
      
 

  for x in range(l):
    i = m[x]
    if (shortgenra[i] == '1'):
      g.add_edge(i, glabels[6], avg_user_rating = rating[i], year_released = movieyear[i])
      gn = glabels[6] + str(movieyear[i])
      #g.add_edge(i,gn, avg_user_rating = rating[i], year_released = movieyear[i])
      
  

 
  mnodes   = np.array(nx.get_node_attributes(g,'movietitle').keys())
  gennode = nx.get_node_attributes(g,'genre').keys()


  # Start Gathering Statistics  May just do for degree and eigenvector centrality
  deg       = nx.degree(g)
  ev        = nx.eigenvector_centrality_numpy(g)
 
  # Filter all Centrality measures for Genra.
  for i in range(7):
    temp = deg[glabels[i]]
    genra_degree.append(temp)
    temp = ev[glabels[i]]
    eigencntrl.append(temp)

 
   
 # Get T-stats (avg, std, se) for Genra 
  
  #dof = ((l) - (totalgenra+1))
  dof = 6
  avggenra = np.mean(np.array(genra_degree))
  sdgenra  = np.std(np.array(genra_degree))
  se       = (sdgenra/np.sqrt(totalgenra))

  avgev    = np.mean(np.array(eigencntrl))
  sdev     = np.std(np.array(eigencntrl))
  seev     = (sdev/np.sqrt(totalgenra))

  # Switch to a 99 and 95 percent 1 tailed

  # 99.5% CI with 58791 dof
  # 1 tailed T-Test at alpha of .005 = 2.576
  # # Changed 09/30/16 for 6 dof 3.707



  # Switch to a 99 and 95 percent 1 tailed

  # 99% CI with 58791 dof
  # 1 tailed T-Test at alpha of .01  = 2.326
  # Changed 09/30/16 for 6 dof 3.143


  # 95% CI for 6 dof
  # 1 Tailed T-Test at alpha of .05 = 1.943


  # Get Margin of Error = (Critical Value(tdof) * (Std/sqrt(n)

  # old Critical values for al data points
 
  #cv     = 2.576
  #cv1    = 2.326

  # new critical values using 6 dof (for Genras)

  cv     = 3.143
  cv1    = 1.943

  me     = cv * se
  me1    = cv1 * se

  meev    = cv * seev
  meev1   = cv1 * seev
 
  thigh    = avggenra + me
  tlow     = avggenra - me

  thighev  = avgev + meev
  tlowev   = avgev - meev


  # Update array for Degree stats
  for i in range(7):
   temp = ((genra_degree[i]) / l)
   genra_deg_per.append(temp)
   if (genra_degree[i] > np.abs(thigh)):
     genra_deg_sig.append("***")
   else:
     genra_deg_sig.append("  ")

 
  # Eigenventor Centrality Confidence Intervals and T-test
  
  for i in range(7):
   if (eigencntrl[i] > np.abs(thighev)):
     eigensig.append("***")
   else:
     eigensig.append("  ")

  
   
  print ("Genre Statistics: One sided T-Test at a 99 percent CI for %d records") % (k)
  print ("Avg Degree Centrality: %.2f   Stdev: %.2f  Standard Error:  %.2f") % (avggenra, sdgenra, se)
  
  print ("Avg Eigen Centrality:   %.2f   Stdev: %.2f   Standard Error:  %.2f") % (avgev, sdev, seev)
  print
  print ("Critical Value:                         %.3f") % (cv)
  print
  print ("99 percent CI for Degree is:            Lower (%.2f) Upper (%.2f)") % (tlow, thigh)
  print  
  print
  print ("99 percent CI for Eigen Centrality is:  Lower (%.2f) Upper (%.2f)") % (tlowev, thighev)
  print
  print ("Significant Genre at .01 alpha indicated by '***'")
  print

  print ("%s\t%s\t%s\t%s\t%s\t%s") % (gheadings[0], gheadings[1], gheadings[2], gheadings[3], gheadings[4], gheadings[5])
  for i in range(7):
    print ("%s\t%d\t%.2f\t%s\t%.2f\t%s") % (glabelsout[i], genra_degree[i], genra_deg_per[i], genra_deg_sig[i], eigencntrl[i], eigensig[i])
    print



  # Now do T-test at Alpha .01 
  thigh    = avggenra + me1
  tlow     = avggenra - me1

  thighev  = avgev + meev1
  tlowev   = avgev - meev1

  genra_deg_sig = []
  genra_deg_per = []
  # Update array for Degree stats
  for i in range(7):
   temp = (genra_degree[i] / l)
   genra_deg_per.append(temp)
   if (genra_degree[i] > np.abs(thigh)):
     genra_deg_sig.append("**")
   else:
     genra_deg_sig.append(" ")

 
  # Eigenventor Centrality Confidence Intervals and T-test
  eigensig = []
  for i in range(7):
   if (eigencntrl[i] > np.abs(thighev)):
     eigensig.append("**")
   else:
     eigensig.append("  ")

 
  print ("Genre Statistics: One sided T-Test at a 95 percent CI for %d records") % (k)
  print ("Avg Degree Centrality: %.2f   Stdev: %.2f  Standard Error: %.2f") % (avggenra, sdgenra, se)
  print
  print ("Avg Eigen Centrality:   %.2f   Stdev: %.2f   Standard Error: %.2f") % (avgev, sdev, seev)
  print
  print ("Critical Value:                       %.3f") % (cv1)
  print 
  print ("95 percent CI for Degree is:          Lower (%.2f) Upper (%.2f)") % (tlow, thigh)
  print  
  print
  print ("95 percent CI for Eigen Centrality is: Lower (%.2f) Upper (%.2f)") % (tlowev, thighev)
  print
  print ("Significant Genre's at .05 alpha indicated by '**'")
  print
  print ("%s\t%s\t%s\t%s\t%s\t%s") % (gheadings[0], gheadings[1], gheadings[2], gheadings[3], gheadings[4], gheadings[5])
  for i in range(7):
    print ("%s\t%d\t%.2f\t%s\t%.2f\t%s") % (glabelsout[i], genra_degree[i], genra_deg_per[i], genra_deg_sig[i], eigencntrl[i], eigensig[i])
    print

  print
  print

  if (p == 1):
    print ("Example of a Movie node")
    print
    mnodes   = nx.get_node_attributes(g,'movietitle').keys()
    print g.node[mnodes[1]]
    print
    print ("Example of a Genre node")
    gennodes = nx.get_node_attributes(g,'genre').keys()
    print
    print g.node[gennodes[3]]
    print
    print ("Exaple of an Edge")
    print
    print g.edge[mnodes[1]]
    print
    print
    print
    print

    
  if ((p == 1) or (p == 2)):
    nx.draw(g, node_color = 'b', edge_color = 'r', with_labels = True)
    #plt.savefig("moviegenraA.png") # save as png
    plt.show() # display

  p = p + 1


  # Histogram
  #dhist = nx.degree_histogram(genra.degree)
  #plt.savefig("gdeghist")
 
  # Second graph still in progress
  #nx.draw_networkx_nodes(g,pos, nodelist=g.nodes(),node_color='r',node_size=500, alpha=0.8)
  #nx.draw_networkx_nodes(g,pos, nodelist=g.nodes(),node_color='r',node_size=500, alpha=0.8)

  # Split movie and genra nodes 
  mnodes   = nx.get_node_attributes(g,'movietitle').keys()
  gennode = nx.get_node_attributes(g,'genre').keys()

  #pos=nx.spring_layout(g) 
  #nx.draw_networkx_nodes(g,pos, nodelist=gennode,node_color='r',node_size=500, alpha=0.8)
  #nx.draw_networkx_nodes(g,pos, nodelist=mnodes,  node_color='y',node_size=500, alpha=0.8)

  #nx.draw_networkx_edges(g,pos,width=1.0,alpha=0.5)
  #nx.draw_networkx_edges(g,pos,edgelist=g.edges(), width=8,alpha=0.5,edge_color='b')

 
  #nx.draw_networkx_labels(g,pos,glabels,font_size=16)


  #plt.axis('off')
  #plt.savefig("moviegenraB.png") # save as png
  #plt.show() # display

 

 

   
 