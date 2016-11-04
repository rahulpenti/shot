from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pymongo,json


def main(request):
    if request.method == "POST":
        roll_no,name,mail, mobile = request.POST.get("roll_no"),  request.POST.get("name"), request.POST.get('email'), request.POST.get('mobile')
        client = pymongo.MongoClient()
        mdb = client['shot']
        table = mdb.posts
        check = table.find({"roll_no": roll_no}).count()
        if check > 0:
            message = "Sorry, Roll Number has already been registered"
            return HttpResponse(json.dumps({'message': message}))
        else:
            table.insert_one({'name': name, 'roll_no': roll_no, 'mail': mail, 'mobile': mobile})
            message = "Registered Successfully"
            return HttpResponse(json.dumps({'message': message}))
    return render_to_response("index.html",{},RequestContext(request))

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
