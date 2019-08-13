#jobs.py uses apscheduler to do backgorund tasks whenever this project is started
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import requests
from aylienapiclient import textapi
import logging
import traceback
from trendinghackernews.models import Topstoryinfo


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

logging = logging.getLogger('__name__')
client = textapi.Client("29a82717","7eae2bea79dedcb29ef84c8e78202d80")

#this method is automatically called in backgroud after every 30 minutes
@register_job(scheduler, "interval", minutes=3, replace_existing=True)
def fetch_new_stories_job():

    #get top story ids from hacker news
    top_story_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    top_story_payload = "{}"
    top_story_ids = requests.request("GET", top_story_url, data=top_story_payload)
    top_story_ids= top_story_ids.text[1:-1].split(',')

    #get all story ids stored in db
    stored_story_ids = []
    stories = Topstoryinfo.objects.all()
    for row in stories:
        stored_story_ids.append(row.story_id)
    
    #find all new entries to store in db
    diff_list= list(set(top_story_ids) - set(stored_story_ids))

    #store only those stories that are not present in db and use aylien api to determine sentiments of titles
    for item_id in diff_list:
        try:
            item_url = "https://hacker-news.firebaseio.com/v0/item/{0}.json".format(item_id)
            item_payload = "{}"
            response = requests.request("GET", item_url, data=item_payload).json()

            create_top_story = Topstoryinfo(story_id = response.get('id'),
            username = response.get('by'),
            title = response.get('title'),
            url = response.get('url'),
            score = response.get('score'),
            story_type = response.get('type'),
            sentiment = client.Sentiment({'text': response.get('title')}).get('polarity'),
            )
            create_top_story.save()
            logging.debug('Saved data for story_id {}'.format(item_id))
        except Exception as e:
            logging.error("Exception Occured during story_id = {}".format(item_id),exc_info=True)

register_events(scheduler)
scheduler.start()