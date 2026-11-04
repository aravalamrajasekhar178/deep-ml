def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    import numpy as np 
    from sklearn.preprocessing import MinMaxScaler 
    x=np.array(x).reshape(-1,1)
    scaled_data=MinMaxScaler().fit_transform(x)
    ans=[]
    for i in scaled_data:
        ans.append(i[0])
    return ans   
    pass