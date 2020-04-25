# oop
class Search:
	"""implementation of Linear Search in Python"""
	def __init__(self, arr, x):
		self.array = arr # input array
		self.length = len(arr) # length of input array
		self.x = x # the item that we are searching

	def linear(self):
		for i in range(self.length):
			if self.x == self.array[i]:
				return i
		return 0



# functional programming
def search(arr,x):
	l = len(arr)
	for i in range(0,l):
		if x == arr[i]:
			return i
	return 0


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    x = 3
    print(search(arr,x))
    s = Search(arr,x)
    print(s.linear())