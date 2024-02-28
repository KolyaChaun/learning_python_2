from abc import ABC, abstractmethod

from home_work_08_models import Post


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


class PostScheduler:
    def __init__(self, post: Post, channel: SocialChannel) -> None:
        self.post = post
        self.channel = channel

    def process_schedule(self):
        if self.post.ready_to_post():
            self.channel.post_a_message(self.post.message)
        else:
            print(
                f"The message: '{self.post.message}' will be loaded on {self.channel.type}"
            )


def main():
    youtube = YouTubeChannel("YouTube", 100)
    post = Post("Download video tutorial on python", 1076776745)

    facebook = FacebookChannel("Facebook", 2000)
    post_facebook = Post("Upload photo to facebook", 454353453)

    twitter = TwitterChannel("Twitter", 1000)
    post_twitter = Post("Upload a post to Twitter", 123958454545)

    post_scheduler_youtube = PostScheduler(post, youtube)
    post_scheduler_facebook = PostScheduler(post_facebook, facebook)
    post_scheduler_twitter = PostScheduler(post_twitter, twitter)

    post_scheduler_youtube.process_schedule()
    post_scheduler_facebook.process_schedule()
    post_scheduler_twitter.process_schedule()


if __name__ == "__main__":
    main()
