from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone #models의 pub_date값은 자동으로 입력받을 예정이니까 timezone을 불러온다
from .models import Blog
from .forms import NewBlog, CommentForm
#맨처음 페이지
def welcome(request):
    return render(request,'viewcrud/index.html')

#조회 함수
def read(request):
    blogs = Blog.objects.all() #model의 모든 객체를 가져오고 싶음 왜냐? 조회하고 싶으니까
    return render(request, 'viewcrud/funccrud.html',{'blogs':blogs})

#글쓰기 함수
def create(request):
    # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        form = NewBlog(request.POST)       #NewBlog라고 하는 형식에 POST방식으로 입력을 받은걸 변수form에 저장할게
        if form.is_valid:                  #입력값이 유효한가
            post = form.save(commit=False) #form으로들어온 데이터를 저장할까?(아니 아직 하지마 왜냐? 아직 입력 안받은게 있어 그것은 날짜야)
            post.pub_date = timezone.now() #지금시간을 담아줘
            post.save()                    #이제 저장해줘
        return redirect('home')            #home으로 다시 가자
    # 글쓰기 페이지를 띄워주는 역할 == GET
    else:
        #단순히 입력받을 수 있는 form을 띄워줘라
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form':form})

#수정 함수
def update(request, pk):

    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk) 

    #해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewBlog(request.POST, instance=blog)

    if form.is_valid():               
        form.save()                   
        return redirect('home') 
    return render(request, 'viewcrud/new.html', {'form':form})

#삭제함수
def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk) #블로그 불러오기
    blog.delete() #블로그 삭제
    return redirect('home')

def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'viewcrud/add_comment.html', {'form': form})