from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from package.GlobelTools import GlobelTools
from package.models import classify, data


def showIndex(request):
    query_set = classify.objects.filter(is_delete=1).order_by('-id')
    site_query_set = data.objects.filter(is_delete=1)
    # print(query_set[0].class_name)

    Data = {
        'query_set': query_set,
        'site_query_set': site_query_set,
    }

    return render(request, 'index.html', context=Data)


def addClassify(request):
    if request.method == 'GET':
        name = request.GET.get('classify')
        tag = request.GET.get('tag')

        if name == '' or name == None:
            return redirect('../index/')
        try:
            classify.objects.create(class_name=name, tag=tag)
        except Exception as e:
            pass
    return redirect('../index/')


def subClassify(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(id)
        try:
            name = classify.objects.filter(id=id)
            name.update(is_delete=0)
        except Exception as e:
            return HttpResponse('['+name[0].class_name+'] 移除失败，请联系管理员！')
        return HttpResponse('['+name[0].class_name+'] 移除成功！')


def updateClassify(request):
    if request.method == 'GET':
        old_classify = request.GET.get('old_classify')
        new_classify = request.GET.get('new_classify')
        id = request.GET.get('id')
        tag = request.GET.get('tag')
        print(old_classify)
        print(new_classify)
        print(id)
        try:
            classify.objects.filter(id=id).update(class_name=new_classify,tag=tag)
            data.objects.filter(id=id).update(class_name=new_classify)
        except Exception as e:
            pass

    return redirect('../index/')


def addWebsite(request):

    if request.method == 'GET':
        id = request.GET.get('id')
        webTitle = request.GET.get('webTitle')
        webSite = request.GET.get('webSite')
        try:
            data.objects.create(title=webTitle,site_addr=webSite,classify_id=id)
        except Exception as e:
            return HttpResponse('网站添加失败！')
        return HttpResponse('网站添加成功！')


def delWebsite(request):
    if request.method == 'GET':
        id = request.GET.get('id')

        try:
            data.objects.filter(id=id).update(is_delete=0)
        except Exception as e:
            return HttpResponse('网站删除失败！')
        return HttpResponse('网站删除成功！')


def generateQrcode(request):
    if request.method == 'GET':
        id = request.GET.get('id')

        try:
            site_addr = data.objects.filter(id=id)[0].site_addr
            print(site_addr)
            img_name = GlobelTools().generateQrcode(site_addr)
        except Exception as e:
            return HttpResponse(0)

    return HttpResponse(img_name)

def is_delete_1(request):
    if request.method == 'GET':
        boolean = request.GET.get('data')
        print(boolean)
        try:
            classify.objects.all().update(is_delete=boolean)
            data.objects.all().update(is_delete=boolean)
        except Exception as e:
            pass
        return HttpResponse()


