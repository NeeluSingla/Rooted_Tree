import copy
import sys

#Creating A tree form the given set of edges
def createTreeFromEdges(edges,n,queries):
    leafnode=[]
    path={}
    tree={}
    nodes={}
    for j in range(n):
        nodes[j+1]=0
    parentsList=[]
    parentsList.append(1)
    for parent in parentsList:
        tree[parent]=[]
        for i in edges:
            v1 = i.split(' ')
            if(int(v1[0])==parent or int(v1[1])==parent):
                if(int(v1[0])==parent):
                    if(int(v1[1]) not in tree):
                        tree[parent].append(int(v1[1]))
                        parentsList.append(int(v1[1]))
                else:
                    if(int(v1[0]) not in tree):
                        tree[parent].append(int(v1[0]))
                        parentsList.append(int(v1[0]))

    for query in queries:
        queryArray = query.split(' ')
        if(queryArray[0] == 'add'):
            list = add(tree , int(queryArray[1]), int(queryArray[2]))
            if(list != None):
                for child in list:
                    currentValue = nodes.get(child)
                    newValue = currentValue + int(queryArray[2])
                    nodes[child] = newValue
        else:
            nodeList = getPathByBfs(tree, int(queryArray[1]), int(queryArray[2]))
            max = -9999999999
            if(nodeList != None):
                for node in nodeList:
                    if(nodes.get(node) > max):
                        max = nodes.get(node)
            else:
                max = 0
            print(max)


#Add Function
def add(tree, nodeToAddValue, valueToAdd):
    listchildern=[]
    listchildern.append(nodeToAddValue)
    listOfChildren = tree.get(nodeToAddValue)
    new_list = copy.copy(listOfChildren)
    if(new_list != None):
        for child in new_list:
            if(child not in listchildern):
                listchildern.append(child)
                list = tree.get(child)
                if(list != None):
                    for value in list:
                        new_list.append(value)
    return listchildern
	
#Finding the shortest Path Function
def getPathByBfs(tree, startNode, endNode):
    visitedNodes=[]
    visitedNodes.append(startNode)
    queue = []
    queue.append([startNode])
    while queue:
        tempPath = queue.pop(0)
        nodeAtLast = tempPath[-1]
        if nodeAtLast == endNode:
            return tempPath
        for adjacent in tree.get(nodeAtLast, []):
            if(adjacent not in visitedNodes):
                new_path = list(tempPath)
                new_path.append(adjacent)
                queue.append(new_path)
                visitedNodes.append(adjacent)
        parentList = getNodeParents(tree, nodeAtLast)
        for parent in parentList:
            if(parent not in visitedNodes):
                new_path = list(tempPath)
                new_path.append(parent)
                queue.append(new_path)
                visitedNodes.append(parent)

def getNodeParents(tree, node):
    parentList=[]
    for value in tree:
        listChild = tree.get(value)
        if node in listChild:
            parentList.append(value)
            break
    return parentList

if __name__=='__main__':

    f = open(sys.argv[1], 'r')
    number_of_nodes = int(sys.argv[2])
    edges=[]
    for number in range(number_of_nodes-1):
        edges.append(sys.argv[3]).replace('\n',''))
    number_of_queries = int(sys.argv[4]))
    queries=[]
    for number in range(number_of_queries):
        queries.append(sys.argv[5].replace('\n',''))
    createTreeFromEdges(edges,number_of_nodes,queries)