import requests
from concurrent.futures import ThreadPoolExecutor



def make_request():
    api_key='sJypd5QS+4kSmL5WcjFXww==NYyv5EQu4UPjPQ61'
    limit = 1000
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    print('Function Called')
    if response.status_code == requests.codes.ok:
        #open('quotes.txt','w')
        file=open('quotes.txt','r+')
        #with open('quotes.txt') as fp:
        print(response.text)
        file.writelines(response.text)
        file.writelines('/n')
                #fp.write('%s\n' % text)
        #open.close()
        open('quotes.txt').close()
    else:
        print("Error:", response.status_code, response.text)

def main():
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for x in range(1000):
            task=executor.submit(make_request()) 
main()