from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# from Turf.models import HR_Reg, Applicant_Reg, Employee, HrReport, AddWork
from Turf.models import Ownerreg, Turf, BookTurf, Rating, TurfFeedback


class IndexView(TemplateView):
    template_name = 'owner/owner_index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        u = Ownerreg.objects.get(user_id=self.request.user.id)
        b = BookTurf.objects.filter(turf__owner_id=u, status='Booked').count()
        bb = BookTurf.objects.filter(turf__owner_id=u, status='Cancel').count()
        t = b+bb

        context['b'] = t
        return context


class ManageTurf(LoginRequiredMixin, TemplateView):
    template_name = 'owner/manage_turf.html'
    login_url = '/'


class ViewProfile(LoginRequiredMixin, TemplateView):
    template_name = 'owner/profile.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewProfile, self).get_context_data(**kwargs)
        p = Ownerreg.objects.get(user_id=self.request.user.id)

        context['p'] = p
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        addr = request.POST['addr']
        con = request.POST['con']
        od = request.POST['od']
        oe = request.POST['oe']
        id = request.POST['id']

        t = Ownerreg.objects.get(pk=id)
        lid = t.user.id
        t.contact = con
        t.address = addr
        t.owner_addr = od
        t.save()

        u = User.objects.get(pk=lid)
        u.email = oe
        u.first_name = name
        u.save()

        messages = "Updated Successfully"
        return render(request, 'owner/owner_index.html', {'message': messages})


class AddTurf(LoginRequiredMixin, TemplateView):
    template_name = 'owner/add_turf.html'
    login_url = '/'

    def post(self, request, *args, **kwargs):
        fullname = request.POST['name']
        size = request.POST['size']
        description = request.POST['description']
        location = request.POST['location']
        price = request.POST['price']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        fec = request.POST['fec']
        licence = request.FILES['licence']
        type = request.POST['type']
        video = request.FILES['image4']

        ow = Ownerreg.objects.get(user_id=self.request.user.id)

        t = Turf()
        t.owner = ow
        t.name = fullname
        t.descri = description
        t.location = location
        t.price = price
        t.image1 = image1
        t.image2 = image2
        t.image3 = image3
        t.facility = fec
        t.status = 'Post'
        t.licence = licence
        t.game = type
        t.video = video
        t.size = size
        t.save()

        messages = "Added Successfully"
        return render(request, 'owner/owner_index.html', {'message': messages})


class ViewTurfFeedback(LoginRequiredMixin, TemplateView):
    template_name = 'owner/view_turf_feed.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurfFeedback, self).get_context_data(**kwargs)
        id = self.request.GET['id']

        t = TurfFeedback.objects.filter(turf=id)

        context['t'] = t
        return context


class ViewTurf(LoginRequiredMixin, TemplateView):
    template_name = 'owner/view_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurf, self).get_context_data(**kwargs)
        ow = Ownerreg.objects.get(user_id=self.request.user.id)
        p = Turf.objects.filter(owner_id=ow)
        context['p'] = p
        return context


class ViewRate(LoginRequiredMixin, TemplateView):
    template_name = 'owner/rate.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewRate, self).get_context_data(**kwargs)

        p = self.request.GET['id']
        r = Rating.objects.filter(turf=p).count()
        print(r)
        re = Rating.objects.filter(turf=p)
        if(r > 0):
            rate = 0
            for i in re:
                rate = rate+int(i.rate)
            total = r*5
            avg = (rate/total)*5
            i = 0
            li = []
            while(int(avg) > i):
                li.append(i)
                i = i+1

            # print(math.floor(avg))

            context['avg'] = li
        context['re'] = re
        return context


class UpdateTurf(LoginRequiredMixin, TemplateView):
    template_name = 'owner/update_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(UpdateTurf, self).get_context_data(**kwargs)
        t = self.request.GET['id']
        p = Turf.objects.get(pk=t)
        context['p'] = p
        return context

    def post(self, request, *args, **kwargs):
        fullname = request.POST['name']
        game = request.POST['game']
        description = request.POST['description']
        location = request.POST['location']
        price = request.POST['price']
        fec = request.POST['fec']
        id = request.POST['id']

        t = Turf.objects.get(pk=id)

        t.name = fullname
        t.descri = description
        t.location = location
        t.price = price
        t.facility = fec
        t.game = game
        t.save()

        messages = "Updated Successfully"
        return render(request, 'owner/owner_index.html', {'message': messages})


class DeleteTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']

        t = Turf.objects.get(pk=id)
        t.status = 'Removed'
        t.save()
        return render(request, 'owner/owner_index.html', {'message': "Turf Deleted"})


class ViewTurfBooking(TemplateView):
    template_name = 'owner/view_turf_booking.html'

    def get_context_data(self, **kwargs):
        context = super(ViewTurfBooking, self).get_context_data(**kwargs)
        u = Ownerreg.objects.get(user_id=self.request.user.id)
        b = BookTurf.objects.filter(turf__owner_id=u).exclude(status='Pay')
        context['b'] = b
        return context


class AcceptTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        s = BookTurf.objects.get(pk=id)
        s.status = 'Accepted'
        s.save()
        return render(request, 'owner/owner_index.html', {'message': "Booking Accepted"})


class RejectTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        s = BookTurf.objects.get(pk=id)
        s.status = 'Reject'
        s.save()
        return render(request, 'owner/owner_index.html', {'message': "Booking Reject"})
