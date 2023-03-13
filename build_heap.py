# python3
import os

def build_heap(data):
    swaps = []
    size = len(data)
    for i in range(size//2, -1, -1):
        SiftDown(data, i, swaps)
    return swaps

def SiftDown(data, i, swaps):
    size = len(data)
    min_index = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2 
    if leftChild < size and data[leftChild] < data[min_index]:
        min_index = leftChild
    if rightChild < size and data[rightChild] < data[min_index]:
        min_index = rightChild
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        SiftDown(data, min_index, swaps)

def main():       
    text = input()
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
        fileName = input()
        path = './tests/'    
        mape = os.path.join(path, fileName)
        #if "a" in fileName:
         #   print("Faila nosaukumā ir kļūda:")
          #  return
            
        #else:
        try:
            with open(mape, mode="r") as file:
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
