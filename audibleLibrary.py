import audible

FILENAME = 'auth/audible_auth.txt'
AUTH = audible.Authenticator.from_file(FILENAME)

def convertTime(value):
    try:
        hours = str(int(value / 60))
        minutes = str(value % 60)
        return hours + ':' + minutes.zfill(2)
    except:
        return 'N/A'

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
        runtime_mmm = book['runtime_length_min']
        runtime_hm = convertTime(runtime_mmm)
        book_list.append([title,runtime_mmm,runtime_hm,released,purchased])

book_list.sort()
book_list.insert(0,['title','runtime_mmm','runtime_hm','released','purchased'])
for book in book_list:
    print(book)
