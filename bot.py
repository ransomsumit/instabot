from instapy import InstaPy

#Login
session = InstaPy(username="scarlettjohansonoffcial", password="kj816g197a",
                            geckodriver_path='geckodriver.exe',
                            headless_browser=True)

session.login()

#Setting
session.set_quota_supervisor(enabled=True,
                             peak_likes_hourly=57,
                             peak_comments_hourly=21,
                             peak_follows_hourly=48,
                             peak_follows_daily=None,
                             peak_unfollows_hourly=35,
                             peak_unfollows_daily=402)



session.set_do_comment(True, percentage=100)
session.set_comments([u'My Girl is fire :fire:',
                      u'So Awesome :flushed:',
                      u'Amazing :heart_eyes:'])

#Action
session.like_by_tags(['scarlettjohansson'], skip_top_posts=True, amount=20)
session.follow_user_followers(['scarlettjohanssonworld'], amount=40,
                              randomize=False, sleep_delay=30)
#session.unfollow_users(amount=35, allFollowing=True, style="LIFO",
#                       unfollow_after=24*60*60, sleep_delay=5)
session.end()