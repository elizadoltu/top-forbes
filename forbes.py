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
        
        api_url = f"https://www.forbes.com/forbesapi/person/{profile_uri}.json"
        print(f"Fetching profile from: {api_url}")
        
        response = requests.get(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code == 200:
            data = response.json() 
            
            person_data = data.get('person', {})
            person_lists = person_data.get('personLists', [])
            
            latest_entry = next((entry for entry in person_lists if entry.get('year') == 2024), None)
            if not latest_entry:
                latest_entry = max(person_lists, key=lambda x: x.get('year', 0), default=None)
            
            if latest_entry:
                personal_stats = {
                    "naturalId": latest_entry.get("naturalId"),
                    "name": latest_entry.get("name"),
                    "year": latest_entry.get("year"),
                    "month": latest_entry.get("month"),
                    "uri": latest_entry.get("uri"),
                    "rank": latest_entry.get("rank"),
                    "listUri": latest_entry.get("listUri"),
                    "personName": latest_entry.get("personName"),
                    "finalWorth": latest_entry.get("finalWorth"),
                    "age": latest_entry.get("age"),
                    "country": latest_entry.get("country"),
                    "city": latest_entry.get("city"),
                    "firstNames": latest_entry.get("firstName"),
                    "lastName": latest_entry.get("lastName"),
                    "title": latest_entry.get("title"),
                    "source": latest_entry.get("source"),
                    "industries": latest_entry.get("industries"),
                    "bio": latest_entry.get("bios", []),
                    "image": latest_entry.get("squareImage"),
                    "organization": latest_entry.get("organization"),
                    "birthdate": latest_entry.get("birthdate"),
                    'squareImage': latest_entry.get('squareImage'),
                    'bios': latest_entry.get('bios'),
                    'status': latest_entry.get('status'),
                    'countryOfCitizenship': latest_entry.get('countryOfCitizenship'),
                }
                return personal_stats
            else:
                print("No data available for the specified year.")
                return None
        else:
            print(f"Error fetching profile: {api_url}, Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def crawl_forbes_billionaires():
    page = 1
    all_billionaires = []
    max_billionaires = 200  

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
                "naturalId": personal_data.get("naturalId"),
                    "name": personal_data.get("name"),
                    "year": personal_data.get("year"),
                    "month": personal_data.get("month"),
                    "uri": personal_data.get("uri"),
                    "rank": personal_data.get("rank"),
                    "listUri": personal_data.get("listUri"),
                    "personName": personal_data.get("personName"),
                    "finalWorth": personal_data.get("finalWorth"),
                    "age": personal_data.get("age"),
                    "country": personal_data.get("country"),
                    "city": personal_data.get("city"),
                    "firstNames": personal_data.get("firstNames"),
                    "lastName": personal_data.get("lastName"),
                    "title": personal_data.get("title"),
                    "source": personal_data.get("source"),
                    "industries": personal_data.get("industries"),
                    "bio": personal_data.get("bios", []),
                    "image": personal_data.get("squareImage"),
                    "organization": personal_data.get("organization"),
                    "birthdate": personal_data.get("birthdate"),
                    'squareImage': personal_data.get('squareImage'),
                    'bios': personal_data.get('bios'),
                    'status': personal_data.get('status'),
                    'countryOfCitizenship': personal_data.get('countryOfCitizenship'),
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
