import os
import googleapiclient.discovery

from config import get_youtube_key


def search_videos(args):

    pageToken = None
    search = None
    if 'search' in args:
        search = args['search']
    if 'pageToke' in args:
        pageToken = args['pageToken'] 
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = get_youtube_key()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        q=search,
        fields="items/snippet/title,items/snippet/description,items/snippet/thumbnails/default,nextPageToken,prevPageToken",
        type="video",
        pageToken=pageToken
    )

    response = request.execute()

    return response
