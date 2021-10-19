from django.shortcuts import render
from .models import blg
def index(request):

    blogdata1= blg()
    blogdata1.price=int(1200)
    blogdata1.title='raviLifestyle'
    blogdata1.sbtitle='raviBest Template Website for HTML CSS'   
    blogdata1.img='blog-post-01.jpg'
    blogdata1.desc='Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template collection site for the download purpose.'

    blogdata2= blg()
    blogdata2.price=int(2050)
    blogdata2.title='raviHealthy'
    blogdata2.sbtitle='Etiam id diam vitae lorem dictum'   
    blogdata2.img='blog-post-02.jpg'
    blogdata2.desc='You can support us by contributing a little via PayPal. Please contact'

    blogdata3= blg()
    blogdata3.price=int(1650)
    blogdata3.title='raviFashion'
    blogdata3.sbtitle='Donec tincidunt leo nec magna'   
    blogdata3.img='blog-post-03.jpg'
    blogdata3.desc='Nullam at quam ut lacus aliquam tempor vel sed ipsum. Donec pellentesque tincidunt imperdiet. Mauris sit amet justo vulputate, cursus massa congue, vestibulum odio. Aenean elit nunc, gravida in erat sit amet, feugiat viverra leo. Phasellus interdum, diam commodo egestas rhoncus, turpis nisi consectetur nibh, in vehicula eros orci vel neque.'

    blogdata = blg.objects.all()
    impath='assets/images/blog-post-01.jpg'
    for blog in blogdata:
        print(blog.img.url)

    return render(request,'index.html',{'blgdata':blogdata,'impath':impath})