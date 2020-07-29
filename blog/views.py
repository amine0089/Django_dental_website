from django.shortcuts import render
from .models import BlogPost, Category
from django.core.paginator import Paginator
from django.utils import timezone
from taggit.models import Tag
from django.db.models import Q


def post_list(request):
	post_list = BlogPost.objects.all()
	latests = BlogPost.objects.filter(created__lte=timezone.now()).reverse()[:3]
	categories = Category.objects.all()
	search_query = request.GET.get('q')
	if search_query:
		post_list = post_list.filter(
			Q(title__icontains = search_query)|
			Q(description__icontains = search_query)|
			Q(tags__name__icontains = search_query)
			).distinct()
	paginator = Paginator(post_list, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)	

	context = {
			'post_list':page_obj,
			'categories':categories,
			'latests':latests,
			}
	return render(request,'blog/blog.html',context)

def post_detail(request,id):
	blog_detail = BlogPost.objects.get(id=id)
	latests = BlogPost.objects.filter(created__lte=timezone.now()).reverse()[:3]
	categories = Category.objects.all()
	all_tags = Tag.objects.all()
	context = {
					'blog_detail':blog_detail,
					'categories':categories,
					'latests':latests,
					'all_tags':all_tags,
				}
	return render(request,'blog/blog_detail.html',context)

def post_by_tag(request,tag):

	post_by_tag = BlogPost.objects.filter(tags__name__in=[tag])
	context = {
			'post_list':post_by_tag,
			}
	return render(request,'blog/blog.html',context)


def post_by_category(request,category):
	post_by_category = BlogPost.objects.filter(category__name=category)
	context = {
			'post_list':post_by_category,
			}
	return render(request,'blog/blog.html',context)