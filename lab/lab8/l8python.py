import json

with open('data\schacon.repos.json', 'r', encoding = 'utf-8') as file:
    data = json.load(file)
    
csv = ""
for line in data[0:5]:
    csv += line.get('name') +","+ line.get('html_url') +","+ line.get('updated_at') +","+ line.get('visibility') + '\n'

with open('chacon.csv', 'w') as output:
    output.write(csv)
    







