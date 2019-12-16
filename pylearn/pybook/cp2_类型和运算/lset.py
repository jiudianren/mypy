



def max_min_set():
    prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }
   min_price = min(zip(prices.values(), prices.keys()))
   # min_price is (10.75, 'FB')
   max_price = max(zip(prices.values(), prices.keys()))
   # max_price is (612.78, 'AAPL')
    
    
def same_diff_set():
    a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
    } b
    = {
    'w' : 10,
    'x' : 11,
    'y' : 2
    }
    # Find keys in common
   a.keys() & b.keys() # { 'x', 'y' }
   # Find keys in a that are not in b
   a.keys() - b.keys() # { 'z' }
    # Find (key,value) pairs in common
   a.items() & b.items() # { ('y', 2) }