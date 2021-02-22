import twint
import time

print("Starting Biden tweets.")
b = twint.Config()
b.Search = 'biden'
b.Lang = 'en'
b.Since = '2020-11-02'
b.Until = '2020-11-03'
b.Store_csv = True
b.Output = f"../data/tweets/all_biden_nov_2.csv"
twint.run.Search(b)
print("Successfully scraped Biden tweets.")

print("Starting Trump tweets.")
time.sleep(300)
t = twint.Config()
t.Search = 'trump'
t.Lang = 'en'
t.Since = '2020-11-02'
t.Until = '2020-11-03'
t.Store_csv = True
t.Output = "../data/tweets/all_trump_nov_2.csv"

print("Successfully scraped Trump tweets.")

twint.run.Search(t)