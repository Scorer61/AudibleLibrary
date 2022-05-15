import audible

FILENAME = 'auth/audible_auth.txt'
AUTH = audible.Authenticator.from_file(FILENAME)

def convertTime(_runtime):
    try:
        hours = str(int(_runtime / 60))
        minutes = str(_runtime % 60)
        return hours + ':' + minutes.zfill(2)
    except:
        return 'N/A'

def getAuthors(_authors):
    _author_list = []
    for _author in _authors:
        _author_list.append(_author['name'])
    return ';'.join(_author_list)

with audible.Client(auth=AUTH) as client:
    library = client.get(
        "1.0/library",
        num_results=1000,
        response_groups="product_desc, product_attrs, contributors",
        sort_by="-PurchaseDate"
    )

    book_list = []

    for book in library["items"]:
        author_list = book['authors']
        authors = getAuthors(author_list)
        title = book['title']
        purchased = book['purchase_date']
        released = book['release_date']
        runtime_mmm = book['runtime_length_min']
        runtime_hm = convertTime(runtime_mmm)
        book_list.append([authors,title,runtime_mmm,runtime_hm,released,purchased])

book_list.sort()
book_list.insert(0,['authors','title','runtime_mmm','runtime_hm','released','purchased'])
for book in book_list:
    print(book)
