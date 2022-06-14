from itertools import cycle
import requests

# Generate the pools
def create_pools():
    proxies = proxies_pool()
    headers = [random_header() for _ in range(len(proxies))]

    # This transforms the list into itertools.cycle object (an iterator) that we can run 
    # through using the next() function in lines 16-17.
    proxies_pool = cycle(proxies)
    headers_pool = cycle(headers)
    return proxies_pool, headers_pool
  
# Usage example
proxies_pool, headers_pool = create_pools() 
current_proxy = next(proxy_pool)
current_headers = next(headers_pool)

# Introduce the proxy and headers in the GET request
with requests.Session() as req:
    page = req.get(link, proxies={"http": current_proxy, "https": current_proxy},
                   headers=current_headers, timeout=30)