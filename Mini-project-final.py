import os
stock = []
with open('CprE_Subject.csv') as f:
    next(f)
    for line in f:
        token = line.split(',')
        courseCode = token[0]
        name = token[1]
        type = token[2]
        credits = token[3]
        semester = token[4]
        lecturer = token[5]
        stock.append((courseCode, name, type, credits, semester, lecturer))
#---------------------------------------------------------------------------------------------------------------------------------#
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.pos_map = {}

    def get_credit_value(self, credits):
        if credits[0].isdigit():
            return int(credits[0])
        return 0
    
    def insert_from_stock(self, stock_data):
        for item in stock_data:
            course_info = {  
                'code': item[0],
                'name': item[1],
                'credits': self.get_credit_value(item[3])
            }
            self.heap.append(course_info) 
            idx = len(self.heap) - 1 
            self.pos_map[item[0]] = idx 
            self.heapify_up(idx) 

    def heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx]['credits'] > self.heap[parent]['credits']:
            self.swap(idx, parent)
            self.heapify_up(parent)

    def heapify_down(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left]['credits'] > self.heap[largest]['credits']:
            largest = left
        if right < len(self.heap) and self.heap[right]['credits'] > self.heap[largest]['credits']:
            largest = right
        if largest != idx:
            self.swap(idx, largest) 
            self.heapify_down(largest)
    
    def swap(self, i, j):
        self.pos_map[self.heap[i]['code']] = j
        self.pos_map[self.heap[j]['code']] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_max_load(self):
        res = self.heap[0]
        return f"{res['code']} ({res['name']}) - {res['credits']} Credits"
#----------------------------------------------------------------#
    def update_credit(self, course_code, new_credit):  
        idx = self.pos_map[course_code]
        old_credit = self.heap[idx]['credits']
        self.heap[idx]['credits'] = new_credit
        print(f"\nCourse {course_code} updated to {new_credit} credits.") 
        
        if new_credit > old_credit:
            self.heapify_up(idx)
        else:
            self.heapify_down(idx)
#---------------------------------------------------------------------------------------------------------------------------------#
class Node :
    def __init__ (self, course_code, data): 
        self.value = course_code
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree :
    def __init__ (self):
        self.root = None
    
    def insert (self, course_code, data):
        newNode = Node(course_code, data)
        if self.root is None:
            self.root = newNode
            return
        
        current = self.root
        while True:
            if course_code < current.value:
                if current.left is None:
                    current.left = newNode
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = newNode
                    return
                current = current.right
    
    def display_sorted(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.display_sorted(node.left)
        print(f"{node.value} - {node.data[1]}")
        if node.right:
            self.display_sorted(node.right)
#---------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------#
myHeap = MaxHeap()

myHeap.insert_from_stock(stock)

print("\n--- Current Max Load ---")
print("Highest Credit Course:", myHeap.get_max_load())

#---------------------------------------------------------------------------------------------------------------------------------#
myBST = BinarySearchTree()

for item in stock:
    myBST.insert(item[0], item)

print("Import Complete")
print("--- Sorted Course List ---")
myBST.display_sorted()

myHeap.update_credit("10123124", 5) 

print("New Max Course is now:", myHeap.get_max_load())