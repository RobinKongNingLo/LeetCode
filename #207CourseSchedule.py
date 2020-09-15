from collections import defaultdict

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = defaultdict(list)
        self.grey = set()
        self.black = set()
        self.findCycle = set()
        for course, prereq in prerequisites:
            self.graph[course].append(prereq)
        for course in range(numCourses):
            self.dfs(course)
        if self.findCycle:
            return False
        else: 
            return True

    def dfs(self, course):
        if course in self.black:
            return
        if course in self.grey:
            self.findCycle.add(1)
            return
        self.grey.add(course)
        for dep in self.graph[course]:
            self.dfs(dep)
        self.grey.remove(course)
        self.black.add(course)