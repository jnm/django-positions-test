from django.shortcuts import render
from forms import SillyForm
from models import Photo
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def silly_view(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    if request.POST:
        form = SillyForm(request.POST, instance=photo)
        form.save()
        print 'HEY!', request.POST
    else:
        form = SillyForm(instance=photo)
    return render_to_response('sillytemplate.html', {
        'form': form,                                                  
        'photo': photo,
    }, RequestContext(request, {}),)                                   
