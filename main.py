#?   Call it EasyReddit- for orgammerrs who are bored while in if the terminal and want to have a quick look on reddit

# ? a python app where user inputs a keyword and then all the subreddits with that keyword are shown for the user to click on and then the top rated in descending order get shown--- very simple but good use of API for python

#*  https://medium.com/geekculture/utilizing-reddits-api-8d9f6933e192
#* https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c
#*  https://www.reddit.com/dev/api/#GET_new

#  TODO add in option at start for hot, new etc

#  TODO add in indices for each post and then allow user to select an indicy based on which post they want to view more details about (comments, votes etc)

import requests

username = 'Smerdyboy'
password = 'Summerland!5'
#? person_use_script
app_id = 'N-0CDuLkuSuK9EGrZGHHVw'
#? secret code
secret = 'J-RUa6xeU0GUWnmKPHcrDo4q4Ll8sw'
auth = requests.auth.HTTPBasicAuth(app_id, secret)

data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}
headers = {'User-Agent': 'Smerdyboy/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
access_token = res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {access_token}"}}

subreddit = input("What subreddit do you want to search on Reddit? Type No to close. \n")
filter = input("What filter do you want to choose? New, Hot, Top? Type No to close. \n")

if subreddit == "No" or filter == "No":
    print("Bye")
else:
    res = requests.get(f"https://oauth.reddit.com/r/{subreddit.lower()}/{filter.lower()}", headers=headers)
    children = res.json()['data']['children']
    # print(children[0])

    for idx, post in enumerate(children):
        print(f"""{idx + 1}.) {post['data']['title']} Score: {post['data']['score']}
----------------------------------------------------------------------------------------------------------------------------
        """)
    
    selection_string = input("Do you want to look at more details for a post? Type in the number or No to leave: ")

    if selection_string == "No":
        print("Bye")
    else:
        selection_int = int(selection_string)
        # print(children[selection_int - 1])
        selected_data = children[selection_int - 1]['data']
        # print(selected_data)

        subreddit = selected_data['subreddit']
        title = selected_data['title']
        selftext = selected_data['selftext']
        ups = selected_data['ups']
        downs = selected_data['downs']
        score = selected_data['score']

        print(f"""
SubReddit: {subreddit}
{title} Score: {score} Up: {ups} Downs: {downs}
{selftext} """)
