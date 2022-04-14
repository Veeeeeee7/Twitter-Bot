import tweepy
import requests


def get_random_quote():
    try:
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']

            quote = data[0]['quoteText']
            return quote
        else:
            print("Error while getting quote")
    except:
        print("Something went wrong! Try Again!")


client = tweepy.Client(consumer_key='kq4EaeU45rHMDC5C2LWpgZUhN',
                       consumer_secret='eSnpg1gVeso25i32xJArd7g6KBPVgWA96CLoKHTHxQGQ4V1mLm',
                       access_token='1514715541008646145-JTuyStSrQlislOWRGLz0ek5nUKDpr2',
                       access_token_secret='Hywu3d07p95Pkr9BDDI9vm24oevrUPHRPWRzEN6velqxF')

response = client.create_tweet(text=get_random_quote())
