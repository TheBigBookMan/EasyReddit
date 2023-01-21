#*  https://www.reddit.com/dev/api/#GET_new

import requests
from colorama import Fore, Back, Style

# colorama.init(autoreset = True)

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

print("Welcome to " + Style.BRIGHT + Fore.RED + "EasyReddit!" + Style.RESET_ALL)
subreddit = input("What subreddit do you want to search on Reddit? Type " + Fore.RED + "No " + Style.RESET_ALL + "to close. \n")


if subreddit.lower() == "no":
    print("Bye")
    exit
else:
    filter = input("What filter do you want to choose? " + Style.BRIGHT + Fore.BLUE + "New, " + Fore.RED +  "Hot, " + Fore.GREEN + "Top? " + Style.RESET_ALL + "Type " + Fore.RED + "No " + Style.RESET_ALL + "to close. \n")

    if filter.lower() == "no":
        print("Bye")
        exit
    else:
      res = requests.get(f"https://oauth.reddit.com/r/{subreddit.lower()}/{filter.lower()}", headers=headers)
      children = res.json()['data']['children']
      # print(children[0])

      for idx, post in enumerate(children):
          print(f"{Style.BRIGHT}{Fore.BLUE}{idx + 1}{Style.RESET_ALL}.) {post['data']['title']}- {Style.BRIGHT}{Fore.YELLOW}Score: {Fore.CYAN}{post['data']['score']}{Style.RESET_ALL}\n-----------------------------------------------------------------------------------------")
          
      selection_string = input("\n Do you want to look at more details for a post? Type in the " + Fore.BLUE + "number " + Style.RESET_ALL + " or " + Fore.RED + "No " + Style.RESET_ALL + "to leave: ")

      if selection_string.lower() == "no":
          print("Bye")
          exit
      else:
          selection_int = int(selection_string)
          selected_data = children[selection_int - 1]['data']
          # print(selected_data)

          post_id = selected_data['id']
          author = selected_data['author']
          subreddit = selected_data['subreddit']
          title = selected_data['title']
          selftext = selected_data['selftext']
          ups = selected_data['ups']
          downs = selected_data['downs']
          score = selected_data['score']

          print(f"{Style.BRIGHT}{Fore.BLUE}SubReddit: r/{Fore.RED}{subreddit} \n{Fore.BLUE}Author: {Fore.GREEN}{author} \n{Fore.YELLOW}Score: {Fore.CYAN}{score} {Fore.YELLOW}Up: {Fore.CYAN}{ups} {Fore.YELLOW}Downs: {Fore.CYAN}{downs} \n{Fore.CYAN}{title}{Style.RESET_ALL} \n{selftext} \n--------------------------------------------------------------------------\n")
            
          selection_string = input("Do you want to look at more details for another post? Type in the " + Style.BRIGHT + Fore.BLUE + "number " + Style.RESET_ALL + " \nIf you want to view comments for this post, type " +Style.BRIGHT + Fore.YELLOW + "comments " + Style.RESET_ALL + ". \nOr " +Style.BRIGHT + Fore.RED + "No " + Style.RESET_ALL + "to leave: ")
            
          if selection_string.lower() == 'no':
              print("Bye")
              exit
          elif selection_string.lower() == 'comments':
            comments_of_post = requests.get(f"https://oauth.reddit.com/r/{subreddit.lower()}/comments/{post_id}", headers=headers)
            comments = comments_of_post.json()[1]['data']['children']

            for idx, comment in enumerate(comments):
                comment_data = comment['data']
                # print(comment_data)

                print(f"{Style.BRIGHT}{Fore.BLUE}{idx + 1}{Style.RESET_ALL}). {Style.BRIGHT}{Fore.GREEN}{comment_data['author']}- {Fore.YELLOW}Score: {Fore.CYAN}{comment_data['score']}{Style.RESET_ALL} \n{comment_data['body']}\n----------------------------------------------------------------------")

            selection_string = input("Do you want to look at more details for a post? Type in the  " + Style.BRIGHT + Fore.BLUE + "number " + Style.RESET_ALL + "or " +Style.BRIGHT + Fore.RED + "No " + Style.RESET_ALL + "to leave: ")
