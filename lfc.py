from urllib.request import urlopen
from bs4 import BeautifulSoup

# Link to the website
link = 'https://www.liverpoolfc.com/match/2018-19/first-team/fixtures-and-results'

if __name__ == '__main__':
    # Open the website
    website = urlopen(link)

    # Get HTML code of the website
    html_code = website.read()

    # Create Soup object with our html code from the link
    soup = BeautifulSoup(html_code, 'html.parser')

    # Find date and names of the teams
    next_match = soup.find("div", {"class": "next-match num-fixtures-2"})
    date = next_match.find('p').string.strip()
    which_teams = next_match.findAll('img')

    # Find which team is the next Liverpool FC rival
    team = which_teams[0]['alt'] + ' (away)' if which_teams[1]['alt'] == 'Liverpool' else which_teams[1]['alt'] + ' (home)'

    # Print the team and date
    print()
    print(team)
    print(date, ' UK time')
    input("\nPress enter to finish...")
