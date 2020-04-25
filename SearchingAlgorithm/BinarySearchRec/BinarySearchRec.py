
# functional
def search(arr,start_pos,end_pos,x):
	if end_pos >= start_pos:
		mid_pos = start_pos + (end_pos-start_pos)//2
		if x == arr[mid_pos]:
			return mid_pos
		elif x < arr[mid_pos]:
			return search(arr,start_pos,mid_pos-1,x)
		else:
			return search(arr,start_pos,mid_pos+1,x)
	else:
		return False

if __name__ == '__main__':
	arr = range(100)
	print(search(arr,0,len(arr)-1,1))