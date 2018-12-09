import urllib.request
import urllib.parse

response = urllib.request.urlopen("https://github.com/Niracler?tab=followers")
print(response.read().decode('utf-8'))

print(response.status)
print(response.getheaders())
print(response.getheader('Set-Cookie'))

# data = bytes(urllib.parse.urlencode({}), encoding='utf8')
# response = urllib.request.urlopen("https://github.com/session", data=data)
# print(response.read())
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
