def slices(series, length):
    if length > len(series):
     	raise ValueError('Length must not exceed string length!')
    if length <= 0:
    	raise ValueError('Length must be positive!')
    if not len(series):
    	raise ValueError('Series must not be empty!')
    
    result = []
    
    for i in range(0, len(series) - length + 1):
    	result.append(series[i:i+length])
    
    return result
    
