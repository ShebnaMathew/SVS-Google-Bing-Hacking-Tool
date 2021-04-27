# software-vulnerabilities-and-security-google-hacking-tool
CY5770 SVS Project Spring 2021

Steps to run the tool:
Run the driver file from either the command line or any Python IDE.

How it works:
1. The program takes in a url from the user as the input. This is the url which needs to be checked against all the search results from the queries.
2. The program loads all the queries from the Bing Hacking database (Future scope: Google Hacking Database).
3. Once the queries are loaded, the search is initiated by running one query at a time on Bing.
4. Once a the program gets a ’hit’, meaning the url appeared in one of the searches, the program exits to avoid any more searches.
5. If there are no hits, the latest results are cached and an appropriate message is displayed.

A Web application url may appear in more than one search for different queries. To save time, only the first hit is displayed in the results and the search stops and the program exits.

Future scope:
- incorporate the Google Search Engine along with the GHDB - the Google Hacking Database
- building a Graphical Interface to use the tool more easily
- showing all the hits from all the search results of the queries rather than just the first hit
- optimization to make it faster so that the previous idea is possible
- show the current progress and the time taken to run a search
