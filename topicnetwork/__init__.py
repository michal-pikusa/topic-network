import networkx as nx
from networkx.algorithms import community
from nltk.corpus import stopwords
import re

def build_graph(text):
    word_list = []
    G = nx.Graph()
    for line in text:
        line = (line.strip()).split()
        for i, word in enumerate(line):
            if i != len(line)-1:
                word_a = word
                word_b = line[i+1]
                if word_a not in word_list:
                    word_list.append(word_a)
                if word_b not in word_list:
                    word_list.append(word_b)
                if G.has_edge(word_a,word_b):
                    G[word_a][word_b]['weight'] += 1
                else:
                    G.add_edge(word_a,word_b, weight = 1)
    return G

def calculate_central_nodes(text_network):
    bc = (nx.betweenness_centrality(text_network,weight='weight'))
    nx.set_node_attributes(text_network, bc, 'betweenness')
    bc_threshold = sorted(bc.values(), reverse=True)[20]
    to_keep = [n for n in bc if bc[n] > bc_threshold]
    filtered_network = text_network.subgraph(to_keep)
    return filtered_network

def create_and_assign_communities(text_network):
    communities_generator = community.girvan_newman(text_network)
    top_level_communities = next(communities_generator)
    next_level_communities = next(communities_generator)
    return next_level_communities

def find_topics(text):
    try:
        text_network = build_graph(text)
        text_network = calculate_central_nodes(text_network)
        topics = create_and_assign_communities(text_network)
        return topics
    except:
        print("Error: Something went wrong. Check your input. You need at least 20 unique words in your text to start the analysis.")
        

def clean(text):
    new_text = []
    no_punct = [re.sub(r'[^\w\s]','',x) for x in text] 
    stop_words = set(stopwords.words('english'))
    for line in no_punct:
        new_line = ([item.lower() for item in line.split() if not item.lower() in stop_words])
        new_text.append(' '.join((new_line)))
    return new_text
