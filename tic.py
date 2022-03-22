from TikTokApi import TikTokApi
import tik_tok_key as key

api = TikTokApi(custom_verify_fp=key.verify_fp)


# needs a link
def Get_VideoID(link):
    x = link.find("/video/")
    cut_front = link[x + 7:]
    y = cut_front.find("?")
    cut_end = link[:x + 7 + y]
    video_id = link[x + 7:x + 7 + y]
    return video_id


def Get_Video_Name(video_id):
    # This was used to test downloading a video when given a video id
    video = api.video(id=video_id)

    # Get all information from video
    video_info = video.info()

    # Printing all information found for a video
    # print(video_info)

    # Putting name of video using dictionary
    video_name = video_info['desc']
    return video_name


def Download_Video(video_id):
    video = api.video(id=video_id)
    # Bytes of the TikTok video
    video_data = video.bytes()
    print("Downloading.....")
    with open(Get_Video_Name(video_id) + ".mp4", "wb") as out_file:
        out_file.write(video_data)
    print("Download Complete")
