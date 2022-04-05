# ~~~ make-request.py ~~~
import requests

# route 1 -- ping
def call_ping_route():
  ''' Execute ping request '''
  r = requests.get("http://localhost:5555/ping") # make the request
  return r

# route 2 -- random word
def call_random_word_route():
  ''' Execute random_word request '''
  r = requests.get("http://localhost:5555/word") # make the request
  return r

# route 3 -- string count
def call_string_count():
  ''' Execute string_count post '''
  to_post = {'test_key':'test_value'}
  r = requests.post("http://localhost:5555/string-count", json=to_post) # make the request
  return r

route_callers = [
  call_ping_route,
  call_random_word_route,
  call_string_count
  ]

for call_route in route_callers:
  r = call_route()
  #check r for error status
  r.raise_for_status()
  data = r.json()
  print(data) # print the response
