import requests

url = 'https://httpbin.org/get'

#send get requests - requests.get() has url as required parameter and countless
#optional parameters like params, headers, auth...
x=requests.get(url)



#print status code - 200 means everything is OK
print(x.status_code)



#print response text - notice it reminds you of JSON
print(x.text)


#access url(the url we sent our request to, PARAMETERS included)
print(x.url)




#access content type - different depenting on what kind of response we expect
print(x.headers['Content-Type'])


#print cookies( pieces of information stored in browser to identify user)
print(x.cookies)



#.json() turns response into valid JSON( stored as dictionary in python)
print(x.json())

#post method - sends POST request to url( notice I made a simple express app
#to test it out)
mydata={"name":"Ljuban","age":"13"}
url="http://localhost:3000/"
x=requests.post(url, data=mydata)
print(x.text)
