# pip install google
# pip install beautifulsoup4

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "Schools in Dehradun"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)