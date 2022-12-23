import partition

def quick_sort(arr, low, high):

  if low < high:
  
    pivot = partition.partition(arr, low, high)

    quick_sort(arr, low, pivot-1)
    quick_sort(arr, pivot+1, high)
