from instapy import InstaPy
from selenium import webdriver
import os
import time
#Login 
def runner():
  session = InstaPy(username="scarlettjohansonoffcial", password="kj816g197a",
                              geckodriver_path = os.environ.get("GECKODRIVER_PATH"), browser_executable_path=os.environ.get("FIREFOX_BIN"),
                              headless_browser = True)

  session.login()
  session.set_quota_supervisor(enabled=True,
                               peak_likes_hourly=70,
                               peak_comments_hourly=21,
                               peak_follows_hourly=48,
                               peak_follows_daily=100,
                               peak_unfollows_hourly=35,
                               peak_unfollows_daily=402)

  session.like_by_tags(['scarlettjohansson'], skip_top_posts=True, amount=30)
  session.set_do_comment(True, percentage=100)
  session.set_comments([u'My Girl is fire :fire:',
                        u'So Awesome :flushed:',
                        u'Amazing :heart_eyes:'])

  '''session.follow_user_followers(['scarlettjohanssonworld'], amount=40,
                                randomize=False, sleep_delay=30)
  #session.unfollow_users(amount=35, allFollowing=True, style="LIFO",
  #                       unfollow_after=24*60*60, sleep_delay=5)'''
  session.end()
while 1:
  runner()
  time.sleep(60)
