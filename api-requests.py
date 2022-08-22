import requests

response = requests.get('https://gitlab.com/api/v4/users/nanuchi/projects')
instructors_projects = response.json()

for each_project in instructors_projects:
    print(f'Project Name: {each_project["name"]} \nProject Url: {each_project["web_url"]}')

# print(response.json())
#
# print(type(response.json()))
#
# print(response.json()[0])
