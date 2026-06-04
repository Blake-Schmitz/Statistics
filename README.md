This microservice provides functionality for finding maximum, minimum, longest, and shortest values in lists. It also compares values in a list to a threshold and counts how many
values meet or surpass it.

By default, the microservice runs on 127.0.0.1:5000, but this can be changed by modifying the URL and PORT constants in main.py

Install required libraries by running "pip install -r requirements.txt" in a command prompt at the app's location.

All requests are made as POST requests to the specified URL and path.  
Include the list as JSON array with 'data' as the key as follows: {'data': list}
The response bodies are JSON arrays as specified below each request.  
Any needed query parameters are listed below each request.
<br>
<br>

Maximum: Finds the maximum value and its index.  
POST to URL:PORT/max/  
body: {'data': list}  
response: {'result': maximum value, 'index': [index of maximum value]}  
notes: Accepts nested lists. If a value is a list, only the last value of the list is
considered. If a value appears multiple times, all of its indexes
 are returned in the list of indexes.  
<br>

Minimum: Finds the minimum value and its index.  
POST to URL:PORT/min/  
body: {'data': list}  
response: {'result': minimnum value, 'index': [index of minimum value]}  
notes: Accepts nested lists. If a value is a list, only the last value of the list is
considered. If a value appears multiple times, all of its indexes
are returned in the list of indexes.  
<br>

Long: Finds the longest list or string in a list.
POST to URL:PORT/long/  
body: {'data': list}  
response: {'result': length of list or string, 'index': [index]}
notes: Non-list and Non-string values are given a length of 1. If multiple
values share the longest length, all values' indexes are included in the
list of indexes.
<br>

Short: Finds the longest list or string in a list.
POST to URL:PORT/short/  
body: {'data': list}  
response: {'result': length of list or string, 'index': [index]}  
notes: Non-list and Non-string values are given a length of 1. If multiple
values share the shortest length, all values' indexes are included in the
list of indexes.  
<br>

Threshold: Finds the number of values in a list that meet or exceed a given threshold.  
POST to URL:PORT/threshold/  
query params: 'threshold': threshold value (float)
body: {'data': list}  
response: {'count': number of values => threshold, 'percent': percent of values => threshold}  
notes: Accepts nested lists. If a value is a list, only the last value in the list is considered.
The percent is rounded to 2 decimal points.
