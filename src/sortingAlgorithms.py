import random
import time
import matplotlib.pyplot as plt
import matplotlib.style as style
import progressbar

class Sorter:
    def selectionSort(self, arr):
        res = []
        for i in range(len(arr)):
            m = min(arr)
            res.append(m)
            arr.remove(m)
        return res

    def insertionSort(self,arr):
        def swap(array, x, y):
            temp = array[x]
            array[x] = array[y]
            array[y] = temp
        i = 1
        while i < len(arr):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                swap(arr, j-1, j)
                j = j-1
            i += 1
        return arr
    
    def bubbleSort(self,arr):
        def swap(array, x, y):
            temp = array[x]
            array[x] = array[y]
            array[y] = temp
        
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    swap(arr, j, j+1)
        
        return arr

    def merge(self, arr, l, r, m):
        sizeLeft = m-l+1
        sizeRight = r-m
        L = [0] * (sizeLeft+1)
        R = [0] * (sizeRight+1)

        for i in range(sizeLeft):
            L[i] = arr[l+i]
        
        for j in range(sizeRight):
            R[j] = arr[m+1+j]

        L[sizeLeft] = max(arr) + 1
        R[sizeRight] = max(arr) + 1    

        i = 0
        j = 0
        for k in range(l, r+1):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

    def mergeHelper(self, arr, l, r):
        if l < r:
            m = (l+r)//2
            self.mergeHelper(arr, l, m)
            self.mergeHelper(arr, m+1, r)
            self.merge(arr, l, r, m)
        return arr

    def mergeSort(self, arr):
        res = self.mergeHelper(arr, 0, len(arr) - 1)
        return res

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        
        if r < n and arr[largest] < arr[r]:
            largest = r
        
        if largest!=i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0 , -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr,i,0)
        
        return arr

    def partition(self, arr, l, r):
        i = l-1
        pivot = arr[r]
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1],arr[r] = arr[r], arr[i+1]
        return (i+1)


    def quickSortHelper(self, arr,l,r):
        if l < r:
            p = self.partition(arr, l , r)
            self.quickSortHelper(arr, l ,p-1)
            self.quickSortHelper(arr, p+1, r) 

    def quickSort(self, arr):
        self.quickSortHelper(arr,0,len(arr)-1)
        return arr

    def testAll(self,numTestCases, listLength = 50, printing = True):
        times = {}
        if numTestCases > 1000:
            raise Exception("Number of test cases should be <= 1000")

        if printing:
            print("Testing Selection Sort...")
        start = time.time()
        for i in range(numTestCases):
            testList = random.sample(range(1000), listLength)
            expectedList = sorted(testList)
            actualList = self.selectionSort(testList)
            if expectedList != actualList:
                print("Test Selection Sort Failed: \nExpected List:     {}\nActual List:       {}".format(expectedList, actualList))
                return False
        end = time.time()
        tot = (end-start) * 1000
        if printing:
            print("Test Selection Sort Passed, Time: {}ms".format(tot))
        times['s'] = tot

        if printing:
            print("Testing Merge Sort...")
        start = time.time()
        for i in range(numTestCases):
            testList = random.sample(range(1000), listLength)
            expectedList = sorted(testList)
            actualList = self.mergeSort(testList)
            if expectedList != actualList:
                print("Test Merge Sort Failed: \nExpected List:     {}\nActual List:       {}".format(expectedList, actualList))
                return False
        end = time.time()
        tot = (end-start) * 1000
        if printing:
            print("Test Merge Sort Passed, Time: {}ms".format(tot))
        times['m'] = tot

        if printing:
            print("Testing Bubble Sort...")
        start = time.time()
        for i in range(numTestCases):
            testList = random.sample(range(1000), listLength)
            expectedList = sorted(testList)
            actualList = self.bubbleSort(testList)
            if expectedList != actualList:
                print("Test Bubble Sort Failed: \nExpected List:     {}\nActual List:       {}".format(expectedList, actualList))
                return False
        end = time.time()
        tot = (end-start) * 1000
        if printing:
            print("Test Bubble Sort Passed, Time: {}ms".format(tot))
        times['b'] = tot
        
        if printing:
            print("Testing Insertion Sort...")
        start = time.time()
        for i in range(numTestCases):
            testList = random.sample(range(1000), listLength)
            expectedList = sorted(testList)
            actualList = self.insertionSort(testList)
            if expectedList != actualList:
                print("Test Insertion Sort Failed: \nExpected List:     {}\nActual List:       {}".format(expectedList, actualList))
                return False
        end = time.time()
        tot = (end-start) * 1000
        if printing:
            print("Test Insertion Sort Passed, Time: {}ms".format(tot))
        times['i'] = tot

        if printing:
            print("Testing Heap Sort...")
        start = time.time()
        for i in range(numTestCases):
            testList = random.sample(range(1000), listLength)
            expectedList = sorted(testList)
            actualList = self.heapSort(testList)
            if expectedList != actualList:
                print("Test Heap Sort Failed: \nExpected List:     {}\nActual List:       {}".format(expectedList, actualList))
                return False
        end = time.time()
        tot = (end-start) * 1000
        if printing:
            print("Test Heap Sort Passed, Time: {}ms".format(tot))
        times['h'] = tot

        if printing:
            print("Testing Quick Sort...")
        start = time.time()
        for i in range(numTestCases):
            testList = random.sample(range(1000), listLength)
            expectedList = sorted(testList)
            actualList = self.quickSort(testList)
            if expectedList != actualList:
                print("Test Quick Sort Failed: \nExpected List:     {}\nActual List:       {}".format(expectedList, actualList))
                return False
        end = time.time()
        tot = (end-start) * 1000
        if printing:
            print("Test Quick Sort Passed, Time: {}ms".format(tot))
        times['q'] = tot
        if printing:
            print ("All Tests Passed")
        return times

    def test(self, numTestCases = 50, numIterations = 5, display = False):
        names = ['MergeSort', 'QuickSort', 'HeapSort', 'BubbleSort', 'InsertionSort', 'SelectionSort']
        abv = ['m', 'q', 'h', 'b', 'i', 's']
        MergeSort = []
        QuickSort = []
        HeapSort = []
        BubbleSort = []
        InsertionSort = []
        SelectionSort = []
        listLengths = []

        for lengths in progressbar.progressbar(range(0, numIterations*10, 10)):
            times = self.testAll(numTestCases, listLength = lengths, printing = False)
            listLengths.append(lengths)
            MergeSort.append(times['m'])
            QuickSort.append(times['q'])
            HeapSort.append(times['h'])
            BubbleSort.append(times['b'])
            InsertionSort.append(times['i'])
            SelectionSort.append(times['s'])
        

        plt.plot(listLengths, MergeSort)
        plt.plot(listLengths, QuickSort)
        plt.plot(listLengths, HeapSort)
        plt.plot(listLengths, BubbleSort)
        plt.plot(listLengths, InsertionSort)
        plt.plot(listLengths, SelectionSort)

        plt.legend(names, loc='upper left')
        plt.xlabel("Number of Items in List")
        plt.ylabel("Runtime (ms)")
        plt.title("Sorting Algorithm Comparison")
        plt.grid()

        if display:
            plt.show()

        filename = "../figures/SortingComparison{}.png".format(numIterations * 10)
        plt.savefig(filename)


if __name__ == "__main__":
    sorter = Sorter()
    print("Enter of number of iterations to test")
    num = int(input())
    sorter.test(numTestCases = 50, numIterations = num, display = False)





            
