from abc import ABC, abstractmethod
from home_work_08_models import Post
from time import time


class SocialChannel(ABC):
    def __init__(self, type: str, followers: int) -> None:
        # self.channel: Channel = channel
        self.type = type
        self.followers = followers

    @abstractmethod
    def post_a_message(self, message: str):
        pass


class YouTubeChannel(SocialChannel):
    def post_a_message(self, message: str):
        print(f"Post on youtube massege: {message}")


class FacebookChannel(SocialChannel):
    def post_a_message(self, message: str):
        print(f"Post on facebook massege: {message}")


class TwitterChannel(SocialChannel):
    def post_a_message(self, message: str):
        print(f"Post on twitter massege: {message}")


def channel_dispatcher(channel: SocialChannel, message: str) -> None:
    channel.post_a_message(message)


def process_schedule(post: Post, channel: SocialChannel) -> None:
    message = post.message
    timestamp = post.timestamp
    if timestamp <= time():
        channel_dispatcher(channel, message)
    else:
        print(f"The message: '{message}' will be loaded on {channel.type}")


def main():
    youtube = YouTubeChannel("YouTube", 100)
    post = Post("Download video tutorial on python", 1076776745)

    facebook = FacebookChannel("Facebook", 2000)
    post_facebook = Post("Upload photo to facebook", 454353453)

    twitter = TwitterChannel("Twitter", 1000)
    post_twitter = Post("Upload a post to Twitter", 123958454545)

    process_schedule(post, youtube)
    process_schedule(post_facebook, facebook)
    process_schedule(post_twitter, twitter)


if __name__ == "__main__":
    main()
