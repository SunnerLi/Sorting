import time
import sys
import random


def insertionSort(_list):
	"""
		The implementation of insertion sort
		Input	=> list want to sort
		Output	=> result list had been sorted
	"""
	for i in range(1, len(_list)):
		key = _list[i]
		j = i - 1
		while _list[j] > key and j >= 0:
			_list[j + 1] = _list[j]
			j -= 1
		_list[j + 1] = key
	return _list


def quickSort(_list):
	"""
		The implementation of quick sort(main function)
		Input	=> list want to sort
		Output	=> result list had been sorted
	"""
	return quickSortConq(_list, 0, len(_list)-1)


def quickSortConq(_list, p, r):
	"""
		The implementation of quick sort(conquer function)
		Input	=> list want to sort, the start position and end position
		Output	=> result list had been sorted
	"""
	if r>p:
		_list, q = quickSortPart(_list, p, r)
		_list = quickSortConq(_list, p, q)

		#to avoid the repeation of the random number
		try:
			_list = quickSortConq(_list, q+1, r)
		except:
			print q, " \ ", r
	return _list


def quickSortPart(_list, p, r):
	"""
		The implementation of quick sort(partition function)
		Input	=> list want to sort, the start position and end position
		Output	=> result list had been sorted, the index about pivot position
	"""
	pivot = _list[p]
	i = p
	for j in range(p+1, r):
		if _list[j] <= pivot:
			i += 1
			_list[i], _list[j] = _list[j], _list[i]
	_list[i], _list[p] = _list[p], _list[i]
	return _list, i


def mergeSort(_list):
	"""
		The implementation of merge sort(main function)
		Input	=> list want to sort
		Output	=> result list had been sorted
	"""
	return mergeSortSplit(_list)



def mergeSortSplit(_list):
	"""
		The implementation of merge sort(split function)
		Input	=> list want to sort
		Output	=> result list had been sorted
	"""
	if len(_list) == 1:
		return _list
	l2 = _list[:len(_list)/2]
	l3 = _list[len(_list)/2:]
	l2 = mergeSortSplit(l2)
	l3 = mergeSortSplit(l3)
	return mergeSortMerge(l2, l3)


def mergeSortMerge(l1, l2):
	"""
		The implementation of merge sort(conquer function)
		Input	=> two lists want to sort
		Output	=> result list had been sorted
	"""
	l3 = []
	i = 0
	j = 0
	while i < len(l1) and j < len(l2):
		if l1[i] > l2[j]:
			l3.append(l2[j])
			j += 1
		else:
			l3.append(l1[i])
			i += 1
	while i != len(l1):
		l3.append(l1[i])
		i += 1
	while j != len(l2):
		l3.append(l2[j])
		j += 1
	return l3


def coutingSort(_list):
	"""
		The implementation of couting sort
		Input	=> list want to sort
		Output	=> result list had been sorted

		<*> Causion: the array cannot contain "0" element
	"""
	#initialize the array
	B = []
	C = _list

	#four loop
	for x in range(1, 1000):
		B.append(0)
	for i in range(0, len(_list)):
		B[_list[i]-1] += 1
	for i in range(1, len(B)):
		B[i] += B[i-1]
	for i in range(len(_list)-1, -1, -1):
		C[B[_list[i]-1]-1] = _list[i]
		B[_list[i]-1] -= 1
	return C


def randomDetermineList(llong):
	"""
		The function can generate the random list which size can defined
		Input	=> the length of the list you want
		Output	=> the random list
	"""
	_ = []
	for x in range(1,llong):
		_.append(random.randint(0, 99))
	return _


if __name__ == '__main__':
	ll = []
	print 	"""
-------------------------------------------------------------------------
		Four Sorint Anaylasize
-------------------------------------------------------------------------
	1. insertion sort
	2. quick sort
	3. merge sort
	4. couting sort

	As the result, you can see the two principle:
	(i) . T(insertion sort) = O( N^2 ), so it spend much time.
	(ii). T(counting sort) = O( N + K), so it spend least time.

	The list is generate randomly. 
	The length of the list is 1000.
	The element in the list is in the interval {0, 99}

------------------------------------------------------------------------
			"""

	#	calculate the time to conduct insertion sort
	ll = randomDetermineList(1000)
	startTime = time.time()
	ll = insertionSort(ll)
	endTime = time.time()
	print "insertion sort conduct time: ", (endTime - startTime)

	#	calculate the time to conduct quick sort
	ll = randomDetermineList(1000)
	startTime = time.time()
	ll = quickSort(ll)
	#print ll
	endTime = time.time()
	print "quick sort conduct time    : ", (endTime - startTime)

	#	calculate the time to conduct merge sort
	ll = randomDetermineList(1000)
	startTime = time.time()
	ll = mergeSort(ll)
	#print ll
	endTime = time.time()
	print "merge sort conduct time    : ", (endTime - startTime)

	#	calculate the time to conduct counting sort
	ll = randomDetermineList(1000)
	startTime = time.time()
	ll = coutingSort(ll)
	#print ll
	endTime = time.time()
	print "counting sort conduct time : ", (endTime - startTime)