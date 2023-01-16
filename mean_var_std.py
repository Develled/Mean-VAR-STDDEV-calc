import numpy as np

def calculate(list):
    
  ## raise value error if list is less than 9 values
  if len(list) <9:
      raise ValueError("List must contain nine numbers.")
    
  ##convert list into a 3x3 array
  arr = (np.array(list).reshape(3,3))
    
  ##create calculations dictionary
  calculations = {}
    
  ##create a list for the mean values
  avg = []
  ##calculate the mean for both axes and the flattened matrix
  mean0 = np.mean(arr, axis=0)
  mean1 = np.mean(arr, axis=1)
  meanFlat = np.mean(arr)
  ##add values to the list for mean values
  avg.append(mean0.tolist())
  avg.append(mean1.tolist())
  avg.append(meanFlat)
  ##add the mean to the calculations dict
  calculations['mean'] = avg
    
    
  ##create a list for the variance
  variance = []
  ##calculate the variance for both axes and the flattened matrix
  var0 = np.var(arr, axis=0)
  var1 = np.var(arr, axis=1)
  varFlat = np.var(arr)
  ##add values to the list for variance
  variance.append(var0.tolist())
  variance.append(var1.tolist())
  variance.append(varFlat)
  ##add the variance to the calculations dict
  calculations['variance'] = variance
    
    
  ##create a list for the standard deviation
  stdD = []
  ##calculate the standard deviation for both axes and the flattened matrix
  std0 = np.std(arr, axis=0)
  std1 = np.std(arr, axis=1)
  stdFlat = np.std(arr)
  ##add values to the standard deviation list
  stdD.append(std0.tolist())
  stdD.append(std1.tolist())
  stdD.append(stdFlat)
  ##add the standard deviations to the calculations dict
  calculations['standard deviation'] = stdD
    
    
  ##create a list for the max values
  maxList = []
  ##calculate the max values for both axes and the flattened matrix
  max0 = np.max(arr, axis=0)
  max1 = np.max(arr, axis=1)
  maxFlat = np.max(arr)
  ##add values to the max values list
  maxList.append(max0.tolist())
  maxList.append(max1.tolist())
  maxList.append(maxFlat)
  ##add the max values to the calculations dict
  calculations['max'] = maxList
  
    
  ##create a list for the minimum values
  minList = []
  ##calculate the minimum values for both axes and the flattened matrix
  min0 = np.min(arr, axis=0)
  min1 = np.min(arr, axis=1)
  minFlat = np.min(arr)
  ##add values to the minimum values list
  minList.append(min0.tolist())
  minList.append(min1.tolist())
  minList.append(minFlat)
  ##add the minimum values to the calculations dict
  calculations['min'] = minList
  
    
  ##create a list for the sums
  sums = []
  ##calculate the sum for both axes and the flattened matrix
  sum0 = np.sum(arr, axis=0)
  sum1 = np.sum(arr, axis=1)
  sumFlat = np.sum(arr)
  ##add values to the list of sums
  sums.append(sum0.tolist())
  sums.append(sum1.tolist())
  sums.append(sumFlat)
  ##add the sums to the calculations dict
  calculations['sum'] = sums  

  return calculations