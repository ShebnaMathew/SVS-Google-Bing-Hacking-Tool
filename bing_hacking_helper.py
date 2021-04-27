import webbrowser
from urllib.request import Request,urlopen
from sys import argv
from urllib.parse import quote
from parseHtml import ParseHtml
from html.parser import HTMLParser

DB_URL = "https://resources.bishopfox.com/files/tools/googlediggity/dictionaries/Bing%20Queries.txt"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

def intro():
    '''
    Function: Prints out a greeting to the user.
    Parameters: None
    Returns: None
    '''
    print("\n")
    print("*"*42)
    print("* WELCOME TO BINGO - A Bing Hacking Tool *")
    print("*"*42)
    print("\n")

def get_user_choice():
    '''
    Function: Presents the user with 3 options.
                It keeps prompting the user until they choose a valid option.
    Parameters: None
    Returns: A string representing the user selected option
    '''
    options = ['A','B','C']
    while True:
        print('-'*30)
        search = input("Please select an option:\nA. Search in cached results\n"
                       "B. Start a new search (new searches take longer)\n"
                       "C. Quit\n"
                       "Your choice:").upper()
        
        if search in options:
            break
    return search

def get_user_url():
    '''
    Function: Prompts the user for a Web Application url
    Parameter: None
    Returns: A string representing the url the user enters 
    '''
    return input("Enter the web url to check for:")

def load_db_queries():
    '''
    Function: Loads all the queries and their corresponding categories
                from the Bing Hacking Database.
    Parameters: None
    Returns: A list of all queries and categories
    '''
    queries = []
    categories = []

    try:
        req = Request(DB_URL, headers=hdr)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        content = urlopen(req)

        for line in content:
            try:
                query = line.decode('utf-8').replace('\n','').split(';;')
                queries.append(query[2])
                categories.append(query[1])
                
            except:
                continue
        return queries, categories
            
    except Exception as e:
        print(e)

def bing(site, use_cache=True):
    '''
    Function: The main engine of the program. It loads all the queries from the DB.
                And then based on the user option to use the cache or not,
                it proceeds to look for the user url in the results and display
                the result to the user.
    Parameter: site - a string representing the user input url
                use_cache - a boolean representing whether to search in the cached results
    Returns: None
    '''
    queries = []
    categories = []
    cache = {}
    vulnerable = False

    queries, categories = load_db_queries()

    # run a new scan
    if not use_cache:
        
        for idx, each in enumerate(queries):
            try:
                print("TRYING QUERY:" + each + "\n")
                search_url = 'https://www.bing.com/search?q=' + quote(each)
                html = urlopen(search_url).read().decode('utf8')
                parser = ParseHtml()
                parsed_html = parser.feed(html)

                for url in parser.get_results():
                    cache[url] = [each, categories[idx]]
                
                isVulnerable, complete_url = parser.is_site_in_results(site)
                    
                if isVulnerable:
                    vulnerable = True
                    show_result(site, each, categories[idx], complete_url)
                    break

                print("*"*10 + "\n\n\n")
                
            except Exception as e:
                print(e)

        # update the cache results if there was a complete run without a hit
        if not isVulnerable:
            with open('cached_results.txt', 'w') as out:
                for url,val in cache.items():
                    out.write(url + "::" + val[0] + "::" + val[1] + "\n")
    
    # run a scan from cached results   
    else:
        try:
            with open('cached_results.txt', 'r') as results:
                for each in results:
                    line = each.replace('\n','').split('::')
                    if site in line[0]:
                        vulnerable = True
                        show_result(site, line[1], line[2], line[0])
                        break
                    
        except FileNotFoundError as e:
            print('No cached results available! Please run a new search.')
          
    if not vulnerable:
        print("\n\nSEARCH COMPLETED!\n" + site + " doesn't appear in any of our google hacking query searches.")

def show_result(user_url, query, category, result_url):
    '''
    Function: Prints out the output when there's a search hit.
    Parameters: user_url - A string representing the user input url,
                query - A string representing the query which got a hit
                category - A string representing the category the query belongs to
                result_url - A string representing the complete url of the specific page of
                    web application
    Returns: None         
    '''
    print("\n\n")
    print("-"*80)
    print("BINGO ! WE GOT A HIT -\n" + user_url + " appears in our search results.\n")
    print("CATEGORY:", category)
    print("QUERY:", query)
    print("COMPLETE URL:", result_url)
    print("-"*80)

def main():

    intro()
    choice = get_user_choice()
    
    if choice == "A":
        bing(get_user_url())
        
    elif choice == "B":
        bing(get_user_url(), False)
        
    else:
        print("\n\nThanks for using this tool !\n\n")


if __name__ == "__main__":
    main()
