import re

# REXP = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/[-\w.]+'
REXP2 = r'(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?'


def read_urls_from_file():
    list_of_urls = []
    try:
        with open("example.txt") as file:
            for line in file:
                # print(line)
                url = re.findall(REXP2, line)
                # print(url)
                if not url:  # check if the current list is empty. this is insane to me right now lol, compared to how i was gonna check
                    continue
                else:

                    list_of_urls.append(f'https://www.youtube.com/watch?v={url[0]}')
                # list_of_urls.append(url)
    except Exception as e:
        print(e)
    print(list_of_urls)
    return list_of_urls[:3]  # returns Video Ids


if __name__ == '__main__':
    read_urls_from_file()
