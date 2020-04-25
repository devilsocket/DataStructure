

class Search:

	def __init__(self,arr,x):
		self.array = arr
		self.x = x
		self.start_pos = 0
		self.end_pos = len(arr)-1

	def binary(self):
		while self.start_pos <= self.end_pos:
			mid_pos = self.start_pos + (self.end_pos-self.start_pos)//2
			if arr[mid_pos] == self.x:
				return mid_pos
			elif arr[mid_pos] > self.x:
				self.end_pos = mid_pos - 1
			else:
				self.start_pos = mid_pos + 1
		return False



# functional
def search(arr,start_pos,end_pos,x):
	while start_pos <= end_pos:
		mid_pos = start_pos + (end_pos-start_pos)//2
		if x == arr[mid_pos]:
			return mid_pos
		elif arr[mid_pos] < x:
			start_pos = mid_pos + 1
		else:
			end_pos = mid_pos - 1

	return False

if __name__ == '__main__':
	arr = range(101)
	print(search(arr,0,len(arr)-1,100))
	s = Search(arr,100)
	print(s.binary())