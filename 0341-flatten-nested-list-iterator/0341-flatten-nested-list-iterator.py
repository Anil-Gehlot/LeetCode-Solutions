# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
  def __init__(self, nestedList: List[NestedInteger]):
    self.q = collections.deque()
    self.addInteger(nestedList)

  def next(self) -> int:
    return self.q.popleft()

  def hasNext(self) -> bool:
    return self.q

  def addInteger(self, nestedList: List[NestedInteger]) -> None:
    for ni in nestedList:
      if ni.isInteger():
        self.q.append(ni.getInteger())
      else:
        self.addInteger(ni.getList())


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())