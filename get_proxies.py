def proxies_pool():
    url = 'https://www.sslproxies.org/'

    # Retrieve the site's page. The 'with'(Python closure) is used here in order to automatically close the session when done
    with requests.Session() as res:
        proxies_page = res.get(url)

    # Create a BeutifulSoup object and find the table element which consists of all proxies
    soup = BeautifulSoup(proxies_page.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    return [
        f"{row.find_all('td')[0].string}:{row.find_all('td')[1].string}"
        for row in proxies_table.tbody.find_all('tr')
    ]