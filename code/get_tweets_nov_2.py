import twint
import time
import nest_asyncio
import datetime as dt
import random
nest_asyncio.apply()

# -------
def get_all_tweets_from_day(date, candidate='Trump'):
    
    f = "%Y-%m-%d"
    lam_plus_1 = lambda x: (x + dt.timedelta(days=1)).strftime("%Y-%m-%d")    
    
    d = dt.datetime.strptime(date, f)
    print(f"""\n Begin scraping {candidate}'s tweets on {d}\n""")
    outfile = f"../data/tweets/all_{candidate.lower()}_{date}.csv"

    # twint search query details
    c = twint.Config()
    c.Search = candidate
    c.Lang = 'en'
    c.Since = date
    c.Until = lam_plus_1(d)
    c.Store_csv = True
    c.Output = outfile
    c.Hide_output = True

    # run the search (manually interrupt when there are sufficient number of unique tweets in outfile)
    timeout = time.time() + 60 * 3.5 * 60
    while True:
        time.sleep(1)
        if time.time() > timeout:
            break
        try:
            print(f'Beginning to scrape {candidate}')
            twint.run.Search(c)
            print(f"Scraping complete. File: {outfile} created.")
            return
        except:
            print("Error caught. Restarting.")
            time.sleep(90)
            continue
    
    print(f"All done with {candidate}'s tweets.")
    
get_all_tweets_from_day('2020-11-02', candidate='Biden')
time.sleep(10)
get_all_tweets_from_day('2020-11-02', candidate='Trump')
