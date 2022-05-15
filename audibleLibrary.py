import audible
import csv

def convertTime(_runtime):
    try:
        hours = str(int(_runtime / 60))
        minutes = str(_runtime % 60)
        _runtime_hm = hours + ':' + minutes.zfill(2)
        return _runtime, _runtime_hm
    except:
        return '0', '0:00'

def getContributors(_contributors):
    try:
        _contributor_list = []
        for _contributor in _contributors:
            _contributor_list.append(_contributor['name'])
        return ';'.join(_contributor_list)
    except:
        return 'N/A'

def getLibrary():
    AUTH = audible.Authenticator.from_file('auth/audible_auth.txt')
    with audible.Client(auth=AUTH) as client:
        library = client.get(
            "1.0/library",
            num_results=1000,
            response_groups="product_desc, product_attrs, contributors",
            sort_by="Author"
        )
        book_list = []
        for book in library["items"]:
            author_list = book['authors']
            authors = getContributors(author_list)
            narrator_list = book['narrators']
            narrators = getContributors(narrator_list)
            title = book['title']
            purchased = book['purchase_date']
            released = book['release_date']
            runtime_mmm, runtime_hm = convertTime(book['runtime_length_min'])
            book_list.append([authors,title,narrators,runtime_mmm,runtime_hm,released,purchased])
    return book_list

def writeLibrary(_library):
    fields = ['authors','title','narrators','runtime_mmm','runtime_hm','released','purchased']
    with open('data/library.csv', 'w', newline='', encoding='UTF8') as output:
        write = csv.writer(output)
        write.writerow(fields)
        write.writerows(_library)

library = getLibrary()
writeLibrary(library)
