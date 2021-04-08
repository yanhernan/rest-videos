import os
import googleapiclient.discovery

from config import get_youtube_key


def search_videos(search):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
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
        type="video"
    )

    response = request.execute()

    return response
