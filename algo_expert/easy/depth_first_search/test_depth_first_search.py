import unittest
from depth_first_search import Node

class Test(unittest.TestCase):
    
    def test_depthFirstSearch(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])


if __name__ == '__main__':
    unittest.main()

