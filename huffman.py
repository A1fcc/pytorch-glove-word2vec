import heapq

class Node(object):
    def __init__(self, wid, freq):
        self.wid = wid
        self.freq = freq
        self.father = None
        self.left = None
        self.right = None
        self.is_left = None
        self.code = []
        self.path = []
    

class HuffmanTree(object):

    def __init__(self, word_dict):
        self.word_count = len(word_dict)
        self.huffman = []
        self.node_heap = []
        for i, f in word_dict.items():
            node = Node(i, f)
            self.huffman.append(node)
            heapq.heappush(self.node_heap, (f, i, node))
        self.build_tree()
        self.build_node_code_and_path(self.huffman[-1].left)
        self.build_node_code_and_path(self.huffman[-1].right)
        
    def build_tree(self):
        if len(self.node_heap) <= 1:
            return
        # 利用两个词频最小的节点生成新的节点
        new_node_id = len(self.huffman)
        f_1, wid_1, node1 = heapq.heappop(self.node_heap)
        f_2, wid_2, node2 = heapq.heappop(self.node_heap)
        new_node = Node(new_node_id, f_1 + f_2)
        # left
        new_node.left = wid_1
        node1.is_left = True
        node1.father = new_node_id
        # righr
        new_node.right = wid_2
        node2.is_left = False
        node2.father = new_node_id

        self.huffman.append(new_node)
        heapq.heappush(self.node_heap, (new_node.freq, new_node.wid, new_node))
        if len(self.node_heap) > 1:
            return self.build_tree()

    def build_node_code_and_path(self, wid):
        if self.huffman[wid].is_left:
            code = [0]
        else:
            code = [1]
        self.huffman[wid].code = self.huffman[self.huffman[wid].father].code + code
        self.huffman[wid].path = [self.huffman[wid].father] + self.huffman[self.huffman[wid].father].path

        if self.huffman[wid].left is not None:
            self.build_node_code_and_path(self.huffman[wid].left)

        if self.huffman[wid].right is not None:
            self.build_node_code_and_path(self.huffman[wid].right)
    
    # 将编码转化为路径
    def generate_node_left_and_right_path(self):
        lefts = []
        rights = [] 
        for wid in range(self.word_count):
            left = []
            right = []
            for i, c in enumerate(self.huffman[wid].code):

                if c == 0:
                    left.append(self.huffman[wid].path[i])
                else:
                    right.append(self.huffman[wid].path[i])
            lefts.append(left)
            rights.append(right)
        return lefts, rights


if __name__ == "__main__":
    word_frequency = {0: 4, 1: 6, 2: 3, 3: 2, 4: 2, 5:10}
    hft = HuffmanTree(word_frequency)
    lefts, rights = hft.generate_node_left_and_right_path()
    print(f"left: {lefts}\n")
    print(f"right: {rights}\n")

