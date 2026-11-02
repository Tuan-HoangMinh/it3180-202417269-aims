def search_by_category(items, category):
    """Return DVDs whose category contains the given keyword."""
    keyword = category.strip().casefold()

    if not keyword:
        return []

    return [
        dvd for dvd in items
        if keyword in dvd.category.casefold()
    ]


def search_by_title(items, title):
    """Return DVDs whose title contains the keyword, ignoring letter case."""
    keyword = title.strip().casefold()

    if not keyword:
        return []

    return [
        dvd for dvd in items
        if keyword in dvd.title.casefold()
    ]
