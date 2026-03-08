import csv

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
        
myBST = BinarySearchTree()

with open('CprE_Subject.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        value = int(row[0])
        myBST.insert(value, row)
        print(value)
        
print("Import Complete")
    


