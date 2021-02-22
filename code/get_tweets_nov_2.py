import twint
import time

print("Starting Biden tweets.")
b = twint.Config()
b.Search = 'biden'
b.Lang = 'en'
b.Since = '2020-11-02'
b.Until = '2020-11-03'
b.Store_csv = True
b.Output = f"./all_biden_nov_2.csv"
b.Hide_output = True
twint.run.Search(b)

print("Starting Trump tweets.")
time.sleep(300)
t = twint.Config()
t.Search = 'trump'
t.Lang = 'en'
t.Since = '2020-11-02'
t.Until = '2020-11-03'
t.Store_csv = True
t.Output = "../data/tweets/all_trump_nov_2.csv"
t.Hide_output = True

twint.run.Search(t)