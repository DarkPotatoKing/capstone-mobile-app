import json, requests

port_num = 3001
url = 'http://localhost:{}'.format(port_num)

resp = requests.get(url=url)
data = json.loads(resp.text)

log_headers = data['log_headers'][0]
print '\t\t'.join(log_headers)

for row in data['log_data']:
    print '\t'.join(row)
