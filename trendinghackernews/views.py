from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from aylienapiclient import textapi
import requests
from .models import Topstoryinfo

logging = logging.getLogger('__name__')


def index(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)

        #get top story ids from hacker news
        top_story_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        top_story_payload = "{}"
        top_story_ids = requests.request("GET", top_story_url, data=top_story_payload)
        top_story_ids= top_story_ids.text[1:-1].split(',')

        #get title and sentiment (stored in db) of top stories 
        show_top_story_list = []
        for item_id in top_story_ids:
            try:
                story = Topstoryinfo.objects.get(story_id='{0}'.format(item_id))
                show_top_story_list.append({'title':story.title,'sentiment':story.sentiment,})
            except Exception as e:
                logging.error("Record not found for story: {0}".format(item_id),exc_info=True)

        return render(request,'trendinghackernews/index.html',{'stories_list':show_top_story_list})

    else:
        return JsonResponse({'code':0})

@csrf_exempt
def partial_search(request):
    if 'word' in request.GET:
        word=request.GET.get('word')
        searched_stories = []

        #search table topstoryinfo for any matching results in title which contains word (ignore case) 
        stories = Topstoryinfo.objects.filter(title__icontains=word)
        for row in stories:
            searched_stories.append({'title':row.title,'sentiment':row.sentiment})
        searched_stories = searched_stories[::-1]
        return JsonResponse({'data':searched_stories})
    else:
        return JsonResponse({'code':0})