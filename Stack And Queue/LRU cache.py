# User function Template for python3

'''
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.pre=None
'''


class LRUCache:

    def __init__(self, cap):

        self.hsmap = dict()
        self.capacity = self.count = cap
        self.queue = []

    # This method works in O(1)
    def get(self, key):
        try:
            t = self.hsmap[key]
            self.queue.remove(key)
            self.queue += [key]
            return t
        except:
            return -1

    # This method works in O(1)
    def set(self, key, value):
        try:
            self.queue.remove(key)
            self.queue += [key]
            self.hsmap[key] = value
        except:
            if self.count == 0:
                self.queue.pop(0)
            else:
                self.count -= 1
            self.queue += [key]
            self.hsmap[key] = value


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.pre = None


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  # number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i + 1]), int(a[i + 2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i + 1])), end=' ')
                i += 2
            q += 1
        print()
# } Driver Code Ends