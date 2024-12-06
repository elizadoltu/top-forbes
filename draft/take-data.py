import requests
from bs4 import BeautifulSoup

def fetch_billionaire_profile_data(profile_uri):
    try:
        if profile_uri.startswith('https://www.forbes.com/profile/'):
            profile_uri = profile_uri.split('/profile/')[1].split('?')[0]  
        
        # Correct URL formation
        profile_url = f"https://www.forbes.com/profile/{profile_uri}/?list=billionaires"
        
        print(f"Fetching profile from: {profile_url}")
        
        response = requests.get(profile_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            personal_stats = {}
            stats_block = soup.find('div', class_='listuser-content__block person-stats')
            if stats_block:
                items = stats_block.find_all('dl', class_='listuser-block')
                for item in items:
                    title = item.find('dt', class_='profile-stats__title')
                    value = item.find('dd', class_='profile-stats__text')
                    if title and value:
                        personal_stats[title.get_text(strip=True)] = value.get_text(strip=True)
            return personal_stats
        else:
            print(f"Error fetching profile: {profile_url}, Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

billionaire_profile = fetch_billionaire_profile_data('bernard-arnault')
if billionaire_profile:
    print("Profile data extracted:", billionaire_profile)
