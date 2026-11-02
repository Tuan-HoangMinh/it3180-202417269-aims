def search_by_category(items, category):
    keyword = category.strip().casefold()

    if not keyword:
        return []

    return [
        dvd for dvd in items
        if keyword in dvd.category.casefold()
    ]

def search_by_title(cart, title):
    keyword = title.strip().casefold()

    if not keyword:
        return []

    return [
        dvd for dvd in cart.items
        if keyword in dvd.title.casefold()
    ]