import audible

FILENAME = 'auth/audible_auth.txt'
AUTH = audible.Authenticator.from_file(FILENAME)

with audible.Client(auth=AUTH) as client:
    library = client.get(
        "1.0/library",
        num_results=1000,
        response_groups="product_desc, product_attrs",
        sort_by="-PurchaseDate"
    )

    book_list = []

    for book in library["items"]:
        title = book['title']
        purchased = book['purchase_date']
        released = book['release_date']
        runtime = book['runtime_length_min']
        book_list.append([title,runtime,released,purchased])

book_list.sort()
for book in book_list:
    print(book)
