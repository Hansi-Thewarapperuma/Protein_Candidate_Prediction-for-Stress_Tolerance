'''
implementing the majority voting algorithm on Arabidopsis thaliana DREB2A
Input : tsv file from STRING / AT_Stress_proteins.txt (known proteins)
Output: Unkown proteins with its corresponding scores
Author: Hansi Thewarapperuma
Date: 24/01/2022
'''

import networkx as nx
from networkx import neighbors
from collections import OrderedDict


# count=0
known_proteins_list = []
unknown_proteins_list = []
neighbors_list = []
Dict = {}

#  ****create a network including all known and unknown proteins from a TSV file-STRING DB****

# create an empty graph with no nodes and edges
G = nx.Graph()

with open("string_interactions_short.tsv", 'r') as file:
    for line in file:
        if '#' not in line:
            line = line.strip().split('\t')
            # adding edges to the empty graph
            G.add_edge(line[0].upper(),line[1].upper(), weight=line[12])

    # create the list of known and unknown proteins taken from the graph G
    nodes_list = list(set(G.nodes))
    # print(len(nodes_list))


# ****create the list of known proteins****
with open('AT_stress_proteins.txt', 'r') as file2:
    for line in file2:
        line = line.strip().split('\t')
        # print(line[1])

        known_proteins_list.append(line[1].upper())
        # set operator used to eliminate duplications
        known_proteins_list2 = list(set(known_proteins_list))
    print(len(known_proteins_list))
    print(len(known_proteins_list2))
# for node in nodes_list:
#     for protein in known_proteins_list:
#         if protein != node:
#             unknown_proteins_list.append(node)

    # ****creating the list of unknown proteins****
    for node in nodes_list:
        if node not in known_proteins_list2:
            unknown_proteins_list.append(node)
    print('Number of unknown proteins in the network: ', len(unknown_proteins_list))
    print(unknown_proteins_list)

    # ****finding the corresponding scores for unknown proteins****
    for protein in unknown_proteins_list:
        count = 0
        # get all the neighbours for each unknown protein
        list1 = list(set(G.neighbors(protein)))
        # neighbors_list.append(list1)

        # iterate through the known protein list
        # if a member of known protein list is found as a neighbour of unknown protein increment the count by 1
        for item in known_proteins_list2:
            if item in list1:
                count += 1
        #print(protein,count)
        # create a dictionary where key- unknown protein / value-score
        Dict[protein] = count
    print(Dict)

    # for key,value in Dict.items():
    #     print(key,value)

    # sorting the dictionary in descending order by the value
    descending_dict = OrderedDict(sorted(Dict.items(), key=lambda t: t[1], reverse= True))
    print(descending_dict)

    # for item in descending_dict.items():
    #     print(item)
    # for key,value in descending_dict.items():
    #     print(key,value)

with open('unknown proteins and scores.txt', 'w') as file3:
    for key,value in descending_dict.items():
        output = key,value
        # file3.write(str(output))
        file3.write(f'{output}\n')


print('The degree of ATDREB2A protein: ',G.degree['DREB2A'])











