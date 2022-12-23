def partition(arr, low, high):
     
  pivot = arr[high][2]
  i = low - 1

  for j in range(low, high):
    if arr[j][2] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i + 1
