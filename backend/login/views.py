from django.shortcuts import render
from django.http import HttpResponse
from gensim.summarization import bm25
from nltk.tokenize import word_tokenize
import numpy as np
import json
import time
# Create your views here.

from .models import User, Item


def login(request):
    phone = request.GET.get('phone', '')
    pwd = request.GET.get('pwd', '')
    users = User.objects.filter(phone=phone)
    if len(users) == 0:
        return HttpResponse("User does not exist!")
    if users[0].pwd == pwd:
        return HttpResponse("Login successfully!")
    else:
        return HttpResponse("Wrong password!")


def register(request):
    phone = request.GET.get('phone', '')
    name = request.GET.get('name', '')
    pwd = request.GET.get('pwd', '')
    users = User.objects.filter(phone=phone)
    if len(users) > 0:
        return HttpResponse("User already exists!")
    else:
        user = User(phone=phone, name=name, pwd=pwd)
        user.save()
        return HttpResponse("Register successfully!")


def list(request):
    users = User.objects.all()
    out = ""
    for u in users:
        out += "<p>" + str(u) + "</p>"
    return HttpResponse(out)


def items(request):
    items = Item.objects.all()
    items_dict = []
    for t in items:
        items_dict.append({"id": t.id, "ques": t.ques,
                           "ans": t.ans, "author": t.author})
    return HttpResponse(json.dumps(items_dict))


def search(request):
    q = request.GET.get('q', '')
    items = Item.objects.all()
    items_dict = []
    corpus = []
    for t in items:
        items_dict.append({"id": t.id, "ques": t.ques,
                           "ans": t.ans, "author": t.author})
        corpus.append(word_tokenize(t.ques.lower()))
    # print(corpus)
    # create BM25 model
    bm25_model = bm25.BM25(corpus)
    # tokenize query
    query_seg = word_tokenize(q.lower())
    print("search：{}".format(query_seg))
    start = time.time()
    scores = bm25_model.get_scores(query_seg)
    search_time = time.time() - start
    cnt = sum(np.array(scores) != 0)
    log = "get {} results, time: {:.6f} s".format(cnt, search_time)
    print(log)
    # print(scores)
    sort_score = np.argsort(-np.array(scores))
    # print(sort_score)
    res_cnt = min(cnt, 10)
    result = [items_dict[sort_score[index]]
              for index in range(res_cnt) if scores[sort_score[index]] != 0]
    # print(result)
    response = {"search_time": round(
        search_time, 6), "count": int(cnt), "res": result}
    return HttpResponse(json.dumps(response))


def hot(request):
    hot = ["work feedback", "miss exam",
           "change course", "fall sick", "study abroad"]
    return HttpResponse(str(hot))


def add_ques(request):
    q = request.GET.get('q', '')
    author = request.GET.get('author', '')
    t = Item(ques=q, add=1, author=author)
    t.save()
    return HttpResponse("Add successfully!")


def ans_ques(request):
    id = request.GET.get('id', '')
    ans = request.GET.get('ans', '')
    t = Item.objects.get(id=id)
    t.ans = ans
    t.save()
    return HttpResponse("Answer successfully!")


def added_items(request):
    items = Item.objects.filter(add=1)
    items_dict = []
    for t in items:
        items_dict.append({"id": t.id, "ques": t.ques,
                           "ans": t.ans, "author": t.author})
    return HttpResponse(json.dumps(items_dict))
