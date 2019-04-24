__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "test_graph"

from graph import *
from class_point import *
import unittest
from copy import *

import numpy as np
from math import inf


class GraphTest(unittest.TestCase):
    def setUp(self):
        # Points
        self.point1 = Point(0, 1)
        self.point2 = Point(0, 2)
        self.point3 = Point(0, 3)
        self.point4 = Point(0, 4)

        # Vertices
        self.vertices1 = [self.point1]
        self.vertices2 = [self.point1, self.point2]
        self.vertices3 = [self.point1, self.point2, self.point3]
        self.vertices4 = [self.point1, self.point2, self.point3, self.point4]

        # Edges
        self.edges12_1 = [(self.point1, self.point2, 3.)]
        self.edges12_2 = [(self.point2, self.point1, 5.)]
        self.edges123_1 = [(self.point1, self.point2, 3.), (self.point1, self.point3, 5.)]
        self.edges123_2 = [(self.point1, self.point2, 3.), (self.point1, self.point3, 5.), (self.point2, self.point3, 7.)]
        self.edges123_3 = [(self.point1, self.point2, 3.), (self.point2, self.point3, 7.)]
        self.edges123_4 = [(self.point2, self.point3, 7.)]
        self.edges1234_1 = [(self.point1, self.point2, 3.), (self.point1, self.point3, 5.), (self.point1, self.point4, 7.)]
        self.edges1234_2 = [(self.point1, self.point2, 3.), (self.point1, self.point3, 5.), (self.point2, self.point3, 10.), (self.point1, self.point4, 7.)]
        self.edges1234_3 = [(self.point1, self.point2, 3.), (self.point1, self.point3, 5.), (self.point2, self.point3, 10.), (self.point1, self.point4, 7.), (self.point2, self.point4, 7.)]
        self.edges1234_4 = [(self.point1, self.point2, 3.), (self.point1, self.point3, 5.), (self.point2, self.point3, 10.), (self.point1, self.point4, 7.), (self.point2, self.point4, 7.), (self.point4, self.point3, 5.)]
        self.edges1234_5 = [(self.point1, self.point3, 5.), (self.point2, self.point3, 10.), (self.point1, self.point4, 7.), (self.point2, self.point4, 7.), (self.point4, self.point3, 5.)]

        # Graphs
        self.emptygraph = Graph([], [])
        self.graph1 = Graph(copy(self.vertices1), [])
        self.graph12_1 = Graph(copy(self.vertices2), copy(self.edges12_1))
        self.graph12_2 = Graph(copy(self.vertices2), copy(self.edges12_2))
        self.graph123_1 = Graph(copy(self.vertices3), copy(self.edges123_1))
        self.graph123_2 = Graph(copy(self.vertices3), copy(self.edges123_2))
        self.graph123_3 = Graph(copy(self.vertices3), copy(self.edges123_3))
        self.graph123_4 = Graph(copy(self.vertices3), copy(self.edges123_4))
        self.graph1234_1 = Graph(copy(self.vertices4), copy(self.edges1234_1))
        self.graph1234_2 = Graph(copy(self.vertices4), copy(self.edges1234_2))
        self.graph1234_3 = Graph(copy(self.vertices4), copy(self.edges1234_3))
        self.graph1234_4 = Graph(copy(self.vertices4), copy(self.edges1234_4))
        self.graph1234_5 = Graph(copy(self.vertices4), copy(self.edges1234_5))

    def testGetVerticesEmptyGraph(self):
        graph = copy(self.emptygraph)
        res = graph.getVertices()
        expected = []
        self.assertEqual(res, expected)

    def testGetVerticesGraph12_1(self):
        graph = copy(self.graph12_1)
        res = graph.getVertices()
        expected = copy(self.vertices2)
        self.assertEqual(res, expected)

    def testGetEdgesEmptyGraph(self):
        graph = copy(self.emptygraph)
        res = graph.getEdges()
        expected = []
        self.assertEqual(res, expected)

    def testGetEdgesGraph12_1(self):
        graph = copy(self.graph12_1)
        res = graph.getEdges()
        expected = copy(self.edges12_1)
        self.assertEqual(res, expected)

    def testSetVerticesEmptyGraph(self):
        graph = copy(self.emptygraph)
        graph.setVertices(copy(self.vertices1))
        value = graph.getVertices()
        expected = copy(self.vertices1)
        self.assertEqual(value, expected)

    def testSetVerticesErrorList(self):
        graph = copy(self.emptygraph)
        try:
            value = graph.setVertices(copy(self.point1))
        except:
            self.assertRaises(AssertionError)

    def testSetVerticesErrorVerticesNotPoint(self):
        graph = copy(self.emptygraph)
        try:
            value = graph.setVertices(["a", 1])
        except:
            self.assertRaises(AssertionError)

    def testSetEdgesGraph12_1(self):
        graph = copy(self.graph12_1)
        graph.setEdges(copy(self.edges12_2))
        value = graph.getEdges()
        expected = copy(self.edges12_2)
        self.assertEqual(value, expected)

    def testSetEdgesErrorList(self):
        graph = copy(self.graph12_1)
        try:
            value = graph.setEdges(((Point(1, 0), Point(2, 0), 3.)))
        except:
            self.assertRaises(AssertionError)

    def testSetEdgesErrorOneEdgeNotTuple(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.setEdges([(copy(self.point1), copy(self.point2), 3.), [copy(self.point1), copy(self.point3), 3.]])
        except:
            self.assertRaises(AssertionError)

    def testSetEdgesErrorOneLenEdgeNot3(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.setEdges([(copy(self.point1), copy(self.point2), 3.), (copy(self.point1), copy(self.point3))])
        except:
            self.assertRaises(AssertionError)

    def testSetEdgesErrorVertexNotInVertices(self):
        graph = copy(self.graph12_1)
        try:
            value = graph.setEdges([(copy(self.point1), copy(self.point2), 3.), (copy(self.point1), copy(self.point3), 3.)])
        except:
            self.assertRaises(AssertionError)

    def testSetEdgesErrorPoidsNotFloat(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.setEdges([(copy(self.point1), copy(self.point2), 3.), (copy(self.point1), copy(self.point3), "a")])
        except:
            self.assertRaises(AssertionError)

    def testSetEdgesErrorOneEdgeBetweenSameVertex(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.setEdges([(copy(self.point1), copy(self.point2), 3.), (copy(self.point1), copy(self.point1), 5.)])
        except:
            self.assertRaises(AssertionError)

    def testSetEdgesErrorTwoEdgesBetweenSameVertices(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.setEdges([(copy(self.point1), copy(self.point2), 3.), (copy(self.point2), copy(self.point1), 5.)])
        except:
            self.assertRaises(AssertionError)

    def testAddVertexEmptyGraph(self):
        graph = copy(self.emptygraph)
        graph.add_vertex(copy(self.point1))
        value = graph.getVertices()
        expected = copy(self.vertices1)  # point1
        self.assertEqual(value, expected)

    def testAddVertexErrorVertexNotPoint(self):
        graph = copy(self.emptygraph)
        try:
            value = graph.add_vertex([copy(self.point1), "a"])
        except:
            self.assertRaises(AssertionError)

    def testAddVertexAlreadyInVertices(self):
        graph = copy(self.graph1)
        graph.add_vertex(copy(self.point1))
        value = graph.getVertices()  # inchange
        expected = copy(self.vertices1)
        self.assertEqual(value, expected)

    def testAddEdgeWithNodesAlreadyInVertices(self):
        graph = copy(self.graph123_1)
        graph.add_edge(copy(self.point2), copy(self.point3), 7.)
        value = graph.getEdges()
        expected = copy(self.edges123_1) + [(copy(self.point2), copy(self.point3), 7.)]
        self.assertEqual(value, expected)

    def testAddEdgeWithNodesNotInVertices(self):
        graph = copy(self.emptygraph)
        graph.add_edge(copy(self.point2), copy(self.point3), 7.)
        value_edges = graph.getEdges()
        expected_edges = [(copy(self.point2), copy(self.point3), 7.)]
        self.assertEqual(value_edges, expected_edges)
        value_vertices = graph.getVertices()
        expected_vertices = [copy(self.point2), copy(self.point3)]
        self.assertEqual(value_vertices, expected_vertices)

    def testAddEdgeErrorAlreadyEdgeBetweenSameVertices(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.add_edge(copy(self.point2), copy(self.point1), 10.)  # arete (copy(self.point1), copy(self.point2), 3.) dans graph
        except:
            self.assertRaises(AssertionError)

    def testAddEdgeErrorEdgeAlreadyInEdges(self):
        graph = copy(self.graph123_1)
        try:
            graph.add_edge(copy(self.point1), copy(self.point2), 3.)
        except:
            self.assertRaises(AssertionError)

    def testAddEdgeErrorEdgeAlreadyInEdgesWithVertex1And2Reverse(self):
        graph = copy(self.graph123_1)
        try :
            value = graph.add_edge(copy(self.point2), copy(self.point1), 3.)  # arete (copy(self.point1), copy(self.point2), 3.) dans Edges
        except:
            self.assertRaises(AssertionError)

    def testAddEdgeErrorEdgeBetweenSameVertex(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.add_edge(copy(self.point2), copy(self.point2), 3.)
        except:
            self.assertRaises(AssertionError)

    def testAddEdgeErrorSommet1NotPoint(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.add_edge([1], copy(self.point2), 3.)
        except:
            self.assertRaises(AssertionError)

    def testAddEdgeErrorSommet2NotPoint(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.add_edge(copy(self.point1), "a", 3.)
        except:
            self.assertRaises(AssertionError)

    def testAddEdgeErrorPoidsNotFloat(self):
        graph = copy(self.graph123_1)
        try:
            value = graph.add_edge(copy(self.point1), copy(self.point2), "b")
        except:
            self.assertRaises(AssertionError)

    def testSuppEdgeGraph12_1(self):
        graph = copy(self.graph12_1)
        graph.supp_edge((copy(self.point1), copy(self.point2), 3.))
        value = graph.getEdges()
        expected = []
        self.assertEqual(value, expected)

    def testSuppEdgeErrorEdgeNotInEdges(self):
        graph = copy(self.graph12_1)
        try:
            value = graph.supp_edge((copy(self.point1), copy(self.point2), 30.))
        except:
            self.assertRaises(AssertionError)

    def testSuppEdgeErrorEdgeNotTuple(self):
        graph = copy(self.graph12_1)
        try:
            value = graph.supp_edge([copy(self.point1), copy(self.point2), 3.])
        except:
            self.assertRaises(AssertionError)

    def testSuppVertexGraph1(self):
        """ graphe sans arete donc edges inchangee"""
        graph = copy(self.graph1)
        graph.supp_vertex(copy(self.point1))
        value = graph.getVertices()
        expected = []
        self.assertEqual(value, expected)

    def testSuppVertexGraph12_1(self):
        """ graphe avec arete donc supprimer un sommet, supprime les aretes associees au sommet """
        graph = copy(self.graph12_1)
        graph.supp_vertex(copy(self.point1))
        value_vertices = graph.getVertices()
        expected_vertices = [copy(self.point2)]
        self.assertEqual(value_vertices, expected_vertices)
        value_edges = graph.getEdges()
        expected_edges = []
        self.assertEqual(value_edges, expected_edges)

    def testSuppVertexErrorVertexNotInVertices(self):
        graph = copy(self.graph1)
        try:
            value = graph.supp_vertex(copy(self.point4))
        except:
            self.assertRaises(AssertionError)

    def testMatricePoidsGraph1(self):
        graph = copy(self.graph1)
        value = graph.matrice_poids()
        expected = np.array([[0]])
        self.assertTrue(np.array_equal(value, expected))

    def testMatricePoidsGraph123_1(self):
        graph = copy(self.graph123_1)
        value = graph.matrice_poids()
        expected = np.array([[0., 3., 5.],
                             [3., 0., inf],
                             [5., inf, 0.]])
        self.assertTrue(np.array_equal(value, expected))

    def testSuccesseursGraph123_1(self):
        graph = copy(self.graph123_1)
        value = graph.successeurs()
        expected = [[(copy(self.point2), 3.), (copy(self.point3), 5.)], [(copy(self.point1), 3.)], [(copy(self.point1), 5.)]]
        self.assertEqual(value, expected)

    def testSuccesseursGraph1234_2(self):
        graph = copy(self.graph1234_2)
        value = graph.successeurs()
        expected = [[(copy(self.point2), 3.), (copy(self.point3), 5.), (copy(self.point4), 7.)], [(copy(self.point1), 3.), (copy(self.point3), 10.)], [(copy(self.point1), 5.), (copy(self.point2), 10.)], [(copy(self.point1), 7.)]]
        self.assertEqual(value, expected)
        
    def testSuccesseursSansPoidsGraph1234_2(self):
        graph = copy(self.graph1234_2)
        value = graph.successeurs_sans_poids()
        expected = [[copy(self.point2), copy(self.point3), copy(self.point4)], [copy(self.point1), copy(self.point3)], [copy(self.point1), copy(self.point2)], [copy(self.point1)]]
        self.assertEqual(value, expected)
        
    def testSuccesseursSansPoidsGraph123_1(self):
        graph = copy(self.graph123_1)
        value = graph.successeurs_sans_poids()
        expected = [[copy(self.point2), copy(self.point3)], [copy(self.point1)], [copy(self.point1)]]
        self.assertEqual(value, expected)

    def testEstAtteint(self):
        graph = copy(self.graph1234_1)
        value = graph.est_atteint(copy(self.point3), copy(self.point4))
        self.assertTrue(value)

    def testEstPasAtteint(self):
        graph = copy(self.graph123_4)
        value = graph.est_atteint(copy(self.point1), copy(self.point3))
        self.assertFalse(value)

    def testEstAtteintErrorVertexNotInGraph2(self):
        graph = copy(self.graph12_1)
        try:
            graph.est_atteint(copy(self.point1), copy(self.point3))
        except:
            self.assertRaises(AssertionError)

    def testEstAtteintErrorVertexNotInGraph1(self):
        graph = copy(self.graph12_1)
        try:
            graph.est_atteint(copy(self.point3), copy(self.point1))
        except:
            self.assertRaises(AssertionError)

    def testEstAtteintErrorGraphEmpty(self):
        graph = copy(self.emptygraph)
        try:
            graph.est_atteint(copy(self.point1), copy(self.point2))
        except:
            self.assertRaises(AssertionError)
