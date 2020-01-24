from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.http.response import Http404, HttpResponseRedirect
from .forms import CreateForm
from django.contrib import messages
from django.db.models import Q

'''
    All about function base views
'''

def home(request):
    title = 'Home'
    post = Post.objects.all()
    query = request.GET.get('q',None)
    if query is not None:
        post = post.filter(
            Q(post_title__icontains=query)|
            Q(author_email__icontains=query)
    )
    
    context = {'title': title, 'post': post}
    return render(request, 'home.html', context)

def details(request,pk):
    ''' 
    queryset exist so give the value otherwise raise 404 error
    
    Simplest way:
    post = Post.objects.get(id=pk) simplest method to do
    
    First way:
    from django.http.response import Http404
    try:
        post = Post.objects.get(id=pk)
    except:
        raise Http404
        
    Second way:
    from django.shortcuts import render,get_object_or_404
    post = get_object_or_404(Post,id=pk)
    
    Third way:
    post = Post.objects.filter(id=pk)
    if not post.is_exists():
        raise Http404
    else:
        post = post.first()
    
    '''
    title = 'Single post'
    post = get_object_or_404(Post,id=pk)
    context = {'title': title, 'post': post}
    return render(request, 'details.html', context)


def delete(request,pk):
    title = 'Are you sure?'
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/")
    
    context = {'title': title, 'post': post}
    return render(request, 'delete.html', context)




def update(request,pk):
    post = Post.objects.get(id=pk)
    title = 'Update'
    form = CreateForm(request.POST or None , instance=post)
    context = {'title': title, 'post':post, 'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Post is Updated..')
        # return redirect('details/{num}'.format(num=obj.id))
        return redirect('/')

    return render(request, 'update.html', context)



def create(request):
    title = 'Create New Post!!'
    # form = CreateForm()
    # if request.method == 'POST':
    #     form = CreateForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)
    #         redirect('/')
    #     else:
    #         form = CreateForm()
    form = CreateForm(request.POST or None)
    context = {'title': title, 'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'New Post Created...')
        
        context = {
            'form' : CreateForm()
        } #allows to create multiple post at once
        # return HttpResponseRedirect('details/{num}'.format(num=obj.id))
        
    return render(request, 'create.html', context)
