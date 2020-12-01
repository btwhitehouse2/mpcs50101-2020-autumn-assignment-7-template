import requests
import json
import re
from colorama import Fore, Back, Style 



def user_prompt ():
    """This prompt will allow the user to enter what they want to search
    if they want to continue searching
    or if they want to exit
    """
    user_input = None
    user_generated = None
    category_input = None
    cat_var = None
    while user_input == None :
        user_input = int(input(r'Welcome to Command Line News!' '\n' 'Please make a choice: ' '[1] Top Headlines [2] Search: '))
        #this will take to one of the 7 main categories
        if user_input == 1:
            category_input = None
            while category_input == None:
                category_input = int(input(r'Select which category you would like the headlines for:' '\n' '[1] business' '\n' '[2] entertainment''\n' '[3] general''\n''[4] health''\n''[5] science''\n' '[6] sports''\n''[7] technology''\n'))
                if category_input == 1:
                    cat_var = 'business'
                    break
                elif category_input == 2:
                    cat_var = 'entertainment'
                    break
                elif category_input == 3:
                    cat_var = 'general'
                    break
                elif category_input == 4:
                    cat_var = 'health'
                    break
                elif category_input == 5:
                    cat_var = 'science'
                    break
                elif category_input == 6:
                    cat_var = 'sports'
                    break
                elif category_input == 7:
                    cat_var = 'technology'
                    break
                else:
                    category_input == None
                    print(r'Please make a valid choice:''\n''[1] business''\n' '[2] entertainment''\n''[3] general''\n''[4] health''\n''[5] science''\n''[6] sports''\n''[7] technology')
            search_api = {'category': cat_var, 'language': 'en', 'country': 'us'}
        #This will allow for custom searches
        elif user_input == 2:
            user_generated = input('Please input the category that you want to search: ').lower()

            search_api = {'q':user_generated, 'language': 'en', 'country': 'us'}
        #This will exit the search
        elif user_input == 3 or 'exit': 
            break
        else:
            user_input == None
            print("Please make a valid choice [1]Top Headlines [2]Search or [3] to exit the loop")
    return(search_api)

def create_json_output (search_api):
    # The headers remain the same for all the requests
    headers = {'Authorization': '5178921f092446eca048d486e234e05c'} 
 
    # To fetch the top headlines
    top_headlines_url = 'https://newsapi.org/v2/top-headlines'
    response = requests.get(url=top_headlines_url, headers=headers , params=search_api)
    pretty_json_output = json.dumps(response.json(), indent=0)
    return(pretty_json_output)
 



def main():
    """This piece of code will take the string of pretty_json_output and 
    create the categories of 
    -publisher
    -title
    -date
    -content """
    search_api = user_prompt()
    create_json_output (search_api)
    pretty_json_output = create_json_output (search_api)
    pretty_json_output = str(pretty_json_output)

    publisher =  re.findall(r'(?<=name":\s")\w+',pretty_json_output)
    title = re.findall(r'(?<=title":\s")\D+',pretty_json_output)
    date = re.findall(r'(?<=hedAt":\s")(\d+)-(\d+)-(\d+)',pretty_json_output)
    content = re.findall(r'(?<=content":\s")\D+',pretty_json_output)

    #Ensures that the program runs with a maximum of 10 articles
    if len(str(publisher)) >10:
        for i in range(0,10):
            print(Fore.BLUE + '# ' + (str(i+1,))+ ' article' +Fore.WHITE)
            print(publisher[i])
            print(Fore.RED + (str(title[i])) + Fore.WHITE)
            print(*date[i])
            print(content[i])
    #If there are less than 10 articles the program will still run
    elif 0 < len(str(publisher)) < 11:
        for i in range(0,len(str(publisher))):
            print(Fore.BLUE + '# ' + (str(i+1,))+ ' article' +Fore.WHITE)
            print(publisher[i])
            print(Fore.RED + (str(title[i])) + Fore.WHITE)
            print(*date[i])
            print(content[i])
    #If your custom search lead to no articles this message will print instead of an error. 
    else:
        print("There are no articles on this topic")


if __name__ == "__main__":
    main()

