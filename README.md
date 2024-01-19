Prediction of protein candidates for stress tolerance in Arabidopsis thaliana

Author: Hansi Thewarapperuma
Date: 24.01.2022

Majority voting algorithm was implemented on Arabidopsis thaliana DREB2A containing protein network to predict protein candidates for stress tolerance. 
The initial steps were as follows:
•	Arabidopsis thaliana DREB2A protein in the STRING protein-protein interaction database was searched. The corresponding STRING ID was 3702.AT5G05410.1
•	The maximum interactions were increased to 500 (1st shell) and the interactions were downloaded in tabular format (“string_interactions_short.tsv”)
•	We have a text data file containing known Arabidopsis thaliana proteins for stress tolerance is provided. (“AT_stress_proteins.txt”)
The algorithm to predict the majority voting score of unknown proteins for a given function in a network:
Input: The text file containing known proteins annotated to a particular function (AT_stress_proteins.txt) / TSV file of interactions between all the proteins obtained from STRING DB (string_interaction_short.tsv)

Output: The list of unknown proteins with the predicted majority voting score in a text file

Procedure: 

**Create a network using all known and unknown proteins

Import networkx to generate a graph
Create an empty graph without no nodes and edges
Open the string_interaction_short.tsv file and do strip and split to relevant lines
Add edges to the empty graph from line[o] node to line[1] node meanwhile nodes are updated with .upper()
Create a list of all the nodes (here includes both known and unknown proteins) in the generated graph (nodes_list)


**Create the list of known proteins

Create an empty list, namely known_proteins_list
Open the AT_stress_proteins.txt file and do strip and split to relevant lines
Append 1st index of every line (line[1].upper())to the above mentioned list
Use the set operator to eliminate duplications


**Create the list of unknown proteins

Create an empty list, namely unknown_proteins_list
Iterate through the nodes_list and check the nodes that are absent in known_proteins_list
Append those nodes to the above mentioned list


**Predicting the majority voting score for the unknown proteins

Assign the count variable to 0
Iterate through the items of unknown_proteins_list and get the neighbours for each item and create a list for that
Iterate through the known protein list and if a member if known protein list is found as an element in neighbours list;
Count is incremented by 1


