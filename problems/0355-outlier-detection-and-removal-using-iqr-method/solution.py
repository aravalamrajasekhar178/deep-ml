import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	# Your code here
	q1=np.percentile(data,25)
	q3=np.percentile(data,75)
	iqr=q3-q1
	lb=q1-k*iqr
	ub=q3+k*iqr
	cleaned=[]
	outliers=[]
	for idx,i in enumerate(data):
		if i<lb or i>ub:
			outliers.append(idx)
		else:
			cleaned.append(i)
	return {'cleaned_data':cleaned,'outlier_indices':outliers,'lower_bound':round(lb,4),'upper_bound':round(ub,4)}
	pass