def extract_rent_listings(soup):
    """Extrai endereços, preços e links do HTML."""

    addresses = [
        address.get_text(strip=True)
        for address in soup.find_all("address")
    ]

    prices = [
        price.get_text(strip=True)
        for price in soup.find_all(
            "span",
            class_="PropertyCardWrapper__StyledPriceLine"
        )
    ]

    links = [
        link["href"]
        for link in soup.find_all(
            "a",
            class_="StyledPropertyCardDataArea-anchor"
        )
    ]

    return list(zip(addresses, prices, links))
