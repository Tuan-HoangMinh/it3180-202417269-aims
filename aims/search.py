def search_by_title(cart, title):
    keyword = title.strip().casefold()

    if not keyword:
        return []

    return [
        dvd for dvd in cart.items
        if keyword in dvd.title.casefold()
    ]