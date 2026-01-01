import requests
import sys

if len(sys.argv) !=2:
    sys.exit()

    response = request.get("https://search.brave.com/search?q=spotify" + sys.argv[1])
print(response.json())