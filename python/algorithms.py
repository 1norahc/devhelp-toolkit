#BFS
from collections import deque

class Algorithms:
    def __init__(self): pass 
    
    def __name__(self) -> str: return

    def __class__(self): pass 
    
    def __str__(self) -> str: pass 

    def __dir__(self): pass 

    def __format__(self, format_spec): pass 

    def __commit__(self) -> str: return 

    class BSA:
        def __init__(self, nums, target):
            if(isinstance(nums, list) == False):print(f"'nums' param should be an list.")
            else: self.nums, self.target=nums,target

        def __str__(self) -> str:
            return """ Binary Search Algorithm \n Given a sorted array of n integers and a target value, determine if the target exists in the array in logarithmic time using the binary search algorithm. If target exists in the array, print the index of it."""
        
        def __main__(self,nums,target):
            (left,right)=(0,len(nums)-1)
            while(left<=right):
                mid=(left+right)//2
                if(target==nums[mid]):return(mid)
                elif(target<nums[mid]):right=mid-1
                else:left=mid+1
            return(-1)

        def bsa(self, show_ans=False):
            index=self.__main__(nums=self.nums,target=self.target)
            if(show_ans==True):
                if(index!=-1):return('Element found at index',index)
                else:return('Element found not in the list')
            else:
                if(index!=-1):return(index) 
                else:return(None)
    
    class BFS:
        def __init__(self, implementaion=0):
            if(implementaion==1):self.__main__(self.recursive())
            elif(implementaion==0):self.__main___(self.iterative())
            else:print("Implementation number out of range idiot (:.")

        def __str__(self) -> str: return """ Breadth-First Search (BFS) \n Breadth–first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a ‘search key’) and explores the neighbor nodes first before moving to the next-level neighbors. """

        class iterative: 
            def __str__(self) -> str: return "BFS, iterative method."
            class Graph:
                def __init__(self,edges,n):
                    self.adjList=[[]for _ in range(n)]
                    for(src,dest)in edges:
                        self.adjList[src].append(dest)
                        self.adjList[dest.append(src)]

            def BFS(graph,v,discovered):
                q,discovered[v]=deque(),True
                q.append(v)
                while(q):
                    v=q.popleft()
                    print(v,end=' ')
                    for u in graph.adjList[v]:
                        if(not discovered[u]):
                            discovered[u]=True
                            q.append(u)

        class recursive: 
            def __str__(self) -> str: return "BFS, recuresive method."

        def __main__(self): pass 

A = Algorithms()
print(A)
   
