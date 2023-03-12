# python3
import os

def build_heap(self, data):
    arrays = data
    size = len(arrays)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps

def SiftDown(self, i):
    min_index = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2 
    if leftChild < size and arrays[leftChild] < arrays[min_index]:
        min_index = leftChild
    if rightChild < size and arrays[rightChild] < arrays[min_index]:
        min_index = rightChild
    if min_index != i:
        swaps.append((i, min_index))
        arrays[i], arrays[min_index] = arrays[min_index], arrays[i]
        SiftDown(min_index)
        
def BuildHeap(self):
    n = self.size
    for i in range(n // 2 - 1, -1, -1):
        self.SiftDown(i)

def main():       
    text = input("Ievadiet datus no tastatūras:")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

        assert len(data) == n
        swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    elif "F" in text:
        fileName = input("Ievadiet faila nosaukumu:")
        path = './test/'    
        mape = os.path.join(path, fileName)
        if "a" in fileName:
            print("Faila nosaukumā ir kļūda")
            return
            
        else:
            try:
                with open(mape) as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
            except Exception as error:
                print("Error", str(error))
                return
                  
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return

if __name__ == "__main__":
    main()
