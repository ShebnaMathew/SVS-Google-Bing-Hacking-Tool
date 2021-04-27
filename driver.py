'''
Author: Shebna Mathew
Course: Software Security and Vulnerabilities
Semester: Spring '21
'''

from bing_hacking_helper import intro,get_user_choice,get_user_url,bing

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
