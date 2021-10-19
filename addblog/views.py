from django.shortcuts import redirect, render
import psycopg2


# Create your views here.

def addblog(request):
    if request.method=='POST':
        title=request.POST['title']
        subtitle=request.POST['subtitle']
        desc=request.POST['desc']
        img=request.POST['img']
        username='rajeev'
        print(img)
        conn = psycopg2.connect(host='localhost', dbname='dummy' ,user='postgres',password='43216199')
        cur = conn.cursor() 
        cur.execute("INSERT INTO blogsite_blg VALUES (%s,%s, %s, %s, %s, %s)", (1,title, subtitle, img, desc, username))
        conn.commit()
        return redirect('index')
    else:
        return render(request, 'addblog.html')