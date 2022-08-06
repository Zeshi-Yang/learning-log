from django.shortcuts import render,redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
    '''The main page of learning log'''
    return render(request,'learning_logs/index.html')

@login_required
# 包含request和topic_id的视图函数
def topics(request):
    '''show all the topics'''
    topics=Topic.objects.filter(owner=request.user).order_by('data_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    '''Show one topic with all entries'''
    topic=Topic.objects.get(id=topic_id)
    check_topic_owner(topic,request)
    # mins symbol means descending
    entries=topic.entry_set.order_by('-data_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    '''添加新主题'''
    # Confirm the method of request
    if request.method !='POST':
        # Create a new form
        form=TopicForm()
    else:
        # Post the data and deal them
        form=TopicForm(request.POST)
    # 显示空表单或指出表单数据无效
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    check_topic_owner(topic,request)
    '''添加一个新条目'''
    if request.method !='POST':
        # Create a new form
        form=EntryForm()
    else:
        # Post the data and deal them
        form=EntryForm(request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id)
    context={'form':form,'topic':topic}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    check_topic_owner(topic,request)
    '''添加一个新条目'''
    if request.method !='POST':
        # Create a new form
        form=EntryForm(instance=entry)
    else:
        # Post the data and deal them
        # What is the meaning of instance
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context={'form':form,'topic':topic,'entry':entry}
    return render(request,'learning_logs/edit_entry.html',context)

def check_topic_owner(topic,request):
    if topic.owner != request.user:
        raise Http404