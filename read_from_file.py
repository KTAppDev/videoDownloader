import re
REXP = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/[-\w.]+'
REXP2 = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'

def read_urls_from_file():
    list_of_urls = []
    try:
        with open("example.txt") as file:
            for line in file:
                url = re.findall(REXP2, line)
                if not url:  # check if the current list is empty. this is insane to me right now lol, compared to how i was gonna check
                    continue
                else:
                    list_of_urls.append(url)

    except Exception as e:
        print(e)

    return list_of_urls


print(read_urls_from_file())