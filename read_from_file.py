import re
REXP = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/[-\w.]+'

def read_urls_from_file():
    list_of_urls = []
    try:
        with open("example.txt") as file:
            for line in file:
                url = re.findall(REXP, line)
                if not url:  # check if the current list is empty. this is insane to me right now lol, compared to how i was gonna check
                    continue
                else:
                    list_of_urls.append(url[0])

    except Exception as e:
        print(e)

    return list_of_urls


print(read_urls_from_file())