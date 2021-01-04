import json
import requests

url = 'http://0.0.0.0:5000/predict'
myobj = {'email_content': """> you\'re Anyone knows how much it costs to host a web portal ?
>
Well, it depends on how many visitors you're expecting.
This can be anywhere from less than 10 bucks a month to a couple of $100. 
You should checkout http://www.rackspace.com/ or perhaps Amazon EC2 
if youre running something big..

To unsubscribe yourself from this mailing list, send an email to:
groupname-unsubscribe@egroups.com
"""}

x = requests.post(url, data=json.dumps(myobj))
result = json.loads(json.loads(x.text))
print(result['is_spam'])