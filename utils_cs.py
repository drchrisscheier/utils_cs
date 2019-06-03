# -*- coding: utf-8 -*-

import pandas as pd
from collections import namedtuple

def replace_umlauts(text, is_spacy=False):
    """
    Replaces german umlauts and sharp s in given text.
    :param text: text as str
    :return: manipulated text as str
    """
    if is_spacy:
        res = text.text
    else:
        res = text 
    res = res.replace('ä', 'ae')
    res = res.replace('ö', 'oe')
    res = res.replace('ü', 'ue')
    res = res.replace('Ä', 'Ae')
    res = res.replace('Ö', 'Oe')
    res = res.replace('Ü', 'Ue')
    res = res.replace('ß', 'ss')
    return res

def get_wordcloud_text(text, fname="wordcloud.png"):
    wordcloud = WordCloud(width=800,height=600,  background_color='white', normalize_plurals=False)
    wordcloud.generate(text)
    wordcloud_img=wordcloud.to_image()
    wordcloud_img.save(fname)
    plt.imshow(wordcloud_img)
    
def get_wordcloud_freq(words, counts, fname="wordcloud.png"):
    d = {}
    for a, x in zip(words, counts ):
            d[a] = x

    wordcloud = WordCloud(width=800,height=600,  background_color='white')
    wordcloud.generate_from_frequencies(frequencies=d)
    wordcloud_img=wordcloud.to_image()
    
    wordcloud_img.save(fname)  
    plt.imshow(wordcloud_img)


def map2scale(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return int(rightMin + (valueScaled * rightSpan))

def dict2df(dict_, key_col='token', val_col='value'):
    df = pd.DataFrame()
    df[key_col] = list(dict_.keys())
    df[val_col] = list(dict_.values())
    df.sort_values(by=val_col, axis=0, ascending=False, inplace=True)
    return df

def gen_edge_coordinates(graph, layout):
    xs = []
    ys = []
    val = namedtuple("edges", "xs ys")

    from_nodes =[]
    to_nodes = []
    named_edges = namedtuple('named_edges','from_n to_n')

    edge_node_idx = []
    edge_node_cnt = 0
    prev_edge = ""

    for edge in graph.edges():
        from_node = layout[edge[0]]
        to_node = layout[edge[1]]
        xs.append([from_node[0],to_node[0]])
        ys.append([from_node[1], to_node[1]])

        from_nodes.append(edge[0])
        to_nodes.append(edge[1])

    return val(xs=xs, ys=ys), named_edges(from_n=from_nodes, to_n = to_nodes)

    
def gen_node_coordinates(layout):
    names, coords = zip(*layout.items())
    xs, ys = zip(*coords)
    val = namedtuple("nodes", "names xs ys")
    return val(names=names, xs=xs, ys=ys)
