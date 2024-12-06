import requests
import json
from bs4 import BeautifulSoup

def fetch_billionaire_data(page):
    url = f"https://www.forbes.com/forbesapi/person/billionaires/2024/position/true.json?fields=uri,finalWorth,age,country,source,rank,category,personName,industries,organization,gender,firstName,lastName,squareImage,bios,status,countryOfCitizenship&page={page}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for page {page}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def fetch_billionaire_profile_data(profile_uri):
    try:
        if profile_uri.startswith('https://www.forbes.com/profile/'):
            profile_uri = profile_uri.split('/profile/')[1].split('?')[0]  
        
        profile_url = f"https://www.forbes.com/profile/{profile_uri}/?list=billionaires"
        
        print(f"Fetching profile from: {profile_url}")
        
        response = requests.get(profile_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            personal_stats = {}
            stats_block = soup.find('div', class_='listuser-content__block person-stats')
            if stats_block:
                items = stats_block.find_all('dl', class_='listuser-block__item')
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

def crawl_forbes_billionaires():
    page = 1
    all_billionaires = []
    max_billionaires = 300  

    while len(all_billionaires) < max_billionaires:
        data = fetch_billionaire_data(page)

        if data is None:
            print(f"No data found or error on page {page}. Stopping.")
            break
        
        if 'personList' not in data or 'personsLists' not in data['personList']:
            print(f"'personsLists' field not found in response for page {page}. Stopping.")
            break
        
        for person in data['personList']['personsLists']:
            if len(all_billionaires) >= max_billionaires:
                break  

            profile_uri = person.get('uri')
            personal_data = fetch_billionaire_profile_data(profile_uri)

            billionaire = {
                'rank': person.get('rank'),
                'name': person.get('personName'),
                'finalWorth': person.get('finalWorth'),
                'age': person.get('age'),
                'country': person.get('country'),
                'source': person.get('source'),
                'industries': person.get('industries'),
                'organization': person.get('organization'),
                'gender': person.get('gender'),
                'firstName': person.get('firstName'),
                'lastName': person.get('lastName'),
                'squareImage': person.get('squareImage'),
                'bios': person.get('bios'),
                'status': person.get('status'),
                'countryOfCitizenship': person.get('countryOfCitizenship'),
            }

            if personal_data:
                billionaire.update(personal_data)

            print(f"Added billionaire: {billionaire['name']} (Rank: {billionaire['rank']})")
            all_billionaires.append(billionaire)

        page += 1

    return all_billionaires

def save_to_file(data, filename="billionaires_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    all_billionaires = crawl_forbes_billionaires()
    save_to_file(all_billionaires)
