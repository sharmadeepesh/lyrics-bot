import os
try:
    from bs4 import BeautifulSoup
    import requests
    import urllib
except ModuleNotFoundError:
    print("Some dependencies were not found on your system. Installing them may take a while.")
    os.system("python -m pip install bs4 requests urllib")

url = "https://search.azlyrics.com/search.php?q={}"

def get_lyrics(name, artist):
    lyrics = ""
    query = artist + ' ' + name
    response = requests.get(url.format(urllib.parse.quote(query)))
    soup = BeautifulSoup(response.text,'html.parser')
    link = soup.find('td',{'class':'text-left'})
    song_url = link.find('a').get('href')
    response = requests.get(song_url).text
    soup = BeautifulSoup(response,'html.parser')
    for goods in soup.find_all('div',{'class':None}):
        if len(goods.text)==0:
            pass
        lyrics += goods.text
    print(lyrics)

def main():
    name = input("[+] Enter the name of the song : ")
    artist = input("[+] Enter the name of the artist [leave empty if you want] : ")
    get_lyrics(name, artist)

if __name__ == "__main__":
    print('''
  _                _            ____        _   
 | |              (_)          |  _ \      | |  
 | |    _   _ _ __ _  ___ ___  | |_) | ___ | |_ 
 | |   | | | | '__| |/ __/ __| |  _ < / _ \| __|
 | |___| |_| | |  | | (__\__ \ | |_) | (_) | |_ 
 |______\__, |_|  |_|\___|___/ |____/ \___/ \__|
         __/ |                                  
        |___/   
                                By /sharmadeepesh/                                        
    ''')
    main()
