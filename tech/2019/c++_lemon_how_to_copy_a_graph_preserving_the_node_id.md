# c++ lemon how to copy a graph preserving the node id
2019/08/11

C++ lemon library provides a copy class [DigraphCopy](http://lemon.cs.elte.hu/pub/doc/1.2.3/a00107.html). However, this class does not preserve the node id between the newly created graph and old graph.
To preserve the node id, we can manually create and delete the nodes for the new graph. Below is the function to make such copy happen:
```C++
#include <lemon/list_graph.h>
using namespace lemon;
typedef ListDigraph::ArcMap<double> ArcMap;
typedef ListDigraph::Node Node;
typedef ListDigraph::Arc Arc;
void digraph_copy(const ListDigraph& oldGraph, const ArcMap& oldArcMap, ListDigraph& G, ArcMap& A){
  for(int i = 0; i <= oldGraph.maxNodeId(); i++)
    G.addNode();
  for(ListDigraph::NodeIt n(G); n != INVALID; ++n){
    if(!oldGraph.valid(n))
       G.erase(n);
  }
  for(ListDigraph::ArcIt a(oldGraph); a != INVALID; ++a){
    Arc a1 = G.addArc(oldGraph.source(a), oldGraph.target(a));
    A[a1] = oldArcMap[a];
  } 
}
```
example usage:
```C++
#include <iostream>
int main(){
  ListDigraph G1;
  ArcMap A1(G1);
  Node n0 = G1.addNode();
  Node n1 = G1.addNode();
  Node n2 = G1.addNode();
  Arc a01 = G1.addArc(n0, n1);
  Arc a02 = G1.addArc(n0, n2);
  A1[a01] = 3;
  A1[a02] = 4;
  G1.erase(n1);
  ListDigraph G2;
  ArcMap A2(G2);
  digraph_copy(G1, A1, G2, A2);
  std::cout << countNodes(G2) << std::endl;
  std::cout << countArcs(G2) << std::endl;
  for(ListDigraph::NodeIt n(G2); n != INVALID; ++n){
    std::cout << G2.id(n) << std::endl;
  }
  for(ListDigraph::ArcIt a(G2); a != INVALID; ++a){
    std::cout << G2.id(G2.source(a)) << ' ' << G2.id(G2.target(a)) << std::endl;
    std::cout << A2[a] << std::endl;
  }
  return 0;
}
```