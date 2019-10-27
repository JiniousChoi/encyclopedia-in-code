#!/usr/bin/env python3

from copy import copy

all_txt = [
    {"fname": "res/Array.txt",
     "type": "Array"},
    {"fname": "res/HashTable.txt",
     "type": "HashTable"},
    {"fname": "res/LinkedList.txt",
     "type": "List"},
    {"fname": "res/Math.txt",
     "type": "Math"},
    {"fname": "res/TwoPointers.txt",
     "type": "TwoPointers"},
    {"fname": "res/String.txt",
     "type": "String"},
    {"fname": "res/BinarySearch.txt",
     "type": "BinarySearch"},
    {"fname": "res/DivideAndConquer.txt",
     "type": "DivideAndConquer"},
    {"fname": "res/DynamicProgramming.txt",
     "type": "DP"},
    {"fname": "res/Backtracking.txt",
     "type": "Backtracking"},
    {"fname": "res/Stack.txt",
     "type": "Stack"},
    {"fname": "res/Heap.txt",
     "type": "Heap"},
    {"fname": "res/Greedy.txt",
     "type": "Greedy"},
    {"fname": "res/Sort.txt",
     "type": "Sort"},
    {"fname": "res/BitManipulation.txt",
     "type": "BitManipulation"},
    {"fname": "res/Tree.txt",
     "type": "Tree"},
    {"fname": "res/DFS.txt",
     "type": "DFS"},
    {"fname": "res/BFS.txt",
     "type": "BFS"},
    {"fname": "res/UnionFind.txt",
     "type": "UnionFind"},
    {"fname": "res/Graph.txt",
     "type": "Graph"},
    {"fname": "res/Design.txt",
     "type": "Design"},
    {"fname": "res/TopologicalSort.txt",
     "type": "TopologicalSort"},
    {"fname": "res/Trie.txt",
     "type": "Trie"},
    {"fname": "res/BinaryIndexedTree.txt",
     "type": "BinaryIndexedTree"},
    {"fname": "res/SegmentTree.txt",
     "type": "SegmentTree"},
    {"fname": "res/BST.txt",
     "type": "BST"},
    {"fname": "res/Recursion.txt",
     "type": "Recursion"},
    {"fname": "res/BrainTeaser.txt",
     "type": "BrainTeaser"},
    {"fname": "res/Queue.txt",
     "type": "Queue"},
    {"fname": "res/Minimax.txt",
     "type": "Minimax"},
    {"fname": "res/ReservoirSampling.txt",
     "type": "ReservoirSampling"},
    {"fname": "res/OrderedMap.txt",
     "type": "OrderedMap"},
    {"fname": "res/Geometry.txt",
     "type": "Geometry"},
    {"fname": "res/Random.txt",
     "type": "Random"},
    {"fname": "res/RejectionSampling.txt",
     "type": "RejectionSampling"},
    {"fname": "res/SlidingWindow.txt",
     "type": "SlidingWindow"},
    {"fname": "res/LineSweep.txt",
     "type": "LineSweep"},
    {"fname": "res/RollingHash.txt",
     "type": "RollingHash"},
    {"fname": "res/SuffixArray.txt",
     "type": "SuffixArray"},
]

locked_ids = [156, 157, 158, 159, 161, 163, 170, 186, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 259, 261, 265, 266, 267, 269, 270, 271, 272, 276, 277, 280, 281, 285, 286, 288, 291, 293, 294, 296, 298, 302, 305, 308, 311, 314, 317, 320, 323, 325, 333, 339, 340, 346, 348, 351, 353, 356, 358, 359, 360, 361, 362, 364, 366, 369, 370, 379, 408, 411, 418, 422, 425, 426, 428, 431, 439, 444, 465, 469, 471, 484, 487, 489, 490, 499, 505, 510, 511, 512, 527, 531, 533, 534, 536, 544, 545, 548, 549, 550, 555, 562, 568, 569, 570, 571, 573, 574, 577, 578, 579, 580, 582, 584, 585, 586, 588, 597, 602, 603, 604, 607, 608, 610, 612, 613, 614, 615, 616, 618, 619, 624, 625, 631, 634, 635, 642, 644, 651, 656, 660, 663, 666, 681, 683, 694, 702, 708, 711, 716, 723, 727, 734, 737, 742, 750, 751, 755, 758, 759, 760, 772, 774, 776, 800, 1045, 1050, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1075, 1076, 1077, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1097, 1098, 1099, 1100, 1101, 1102, 1107, 1112, 1113, 1118, 1119, 1120, 1121, 1126, 1127, 1132, 1133, 1134, 1135, 1136, 1141, 1142, 1148, 1149, 1150, 1151, 1152, 1153, 1158, 1159, 1164, 1165, 1166, 1167, 1168, 1173, 1174, 1176, 1180, 1181, 1182, 1183, 1188, 1193, 1194, 1196, 1197, 1198, 1199, 1204, 1205, 1211, 1212, 1213, 1214, 1215, 1216, 1225, 1228, 1229, 1230, 1231, 1236]

def main():
    leetcode = make_leetcode()
    solved_ids = make_solved_ids('solved_docs.txt')
    unsolved_ids = sorted(list(set(leetcode.keys()) -set(locked_ids) - set(solved_ids)))
    print("=========== SOLVED =========")
    print()
    print_leetcode(leetcode, solved_ids)
    print()
    print("=========== UNSOLVED =========")
    print()
    print_leetcode(leetcode, unsolved_ids)

def make_solved_ids(fname):
    with open(fname) as f:
        lines = [line.strip() for line in f.readlines()]
    lines2 = [line.split('.')[0].strip('LC') for line in lines]
    solved_ids = [int(line) for line in lines2 if line.isnumeric()]
    dedup_ids = []
    for i in solved_ids:
        if i not in dedup_ids:
            dedup_ids.append(i)
    return dedup_ids

def make_leetcode():
    leetcode = {}
    for probs in map(parse_txt, all_txt):
        merge(leetcode, probs)
    return leetcode

def merge(leetcode, probs):
    for prob in probs:
        _id, _type = prob["id"], prob["type"]
        if _id in leetcode:
            leetcode[_id]["types"].append(_type)
        else:
            leetcode[_id] = copy(prob)
            leetcode[_id]['types'] = [_type]
            del leetcode[_id]['type']
    return leetcode

def parse_txt(m):
    fname, _type = m['fname'], m['type']
    with open(fname) as fp:
        txt = fp.read()
    probs = make_probs(txt)
    # inject `type` attr.
    for prob in probs:
        prob['type'] = _type
    return probs

def make_probs(txt):
    tokens1 = txt.replace('\n','').split('\t')
    tokens2 = [l.strip() for l in tokens1 if l!='']
    return [{"id": int(_id), "title": _title, "percent": _percent, "level": _level}
            for (_id, _title, _percent, _level) in partition(tokens2, 4)]
    
def partition(xs, n):
    it = iter(xs)
    cnt = len(xs)
    return [[next(it) for _ in range(n)] for _ in range(cnt//n)]

def print_leetcode(leetcode, ids=None):
    if ids == None:
        ids = sorted(list(leetcode.keys()))
    probs = [leetcode[i] for i in ids if i in leetcode]
    for prob in probs:
        prob['types'].sort()
        print(format_prob(prob))
        print()

def format_prob(p):
    _id, _title, _percent, _level, _types = p['id'], p['title'], p['percent'], p['level'], p['types']
    return "LC{}.{} ({}-{})\nTopics: {}".format(_id, _title, _level, _percent, ', '.join(_types))

main()

