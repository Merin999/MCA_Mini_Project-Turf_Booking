import datetime
from datetime import timedelta
import json
import math
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from Turf.mail import bookmail
from django.db.models import Q

# from Turf.models import HR_Reg, Applicant_Reg, Employee, HrReport, AddWork
from Turf.models import Userreg, Turf, BookTurf, Feedback, Rating, TurfFeedback
from datetime import date


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user_index.html'
    login_url = '/'


class ViewProfile(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewProfile, self).get_context_data(**kwargs)
        p = Userreg.objects.get(user_id=self.request.user.id)

        context['p'] = p
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        addr = request.POST['addr']
        con = request.POST['con']

        oe = request.POST['oe']
        id = request.POST['id']

        t = Userreg.objects.get(pk=id)
        lid = t.user.id
        t.contact = con
        t.address = addr
        t.save()

        u = User.objects.get(pk=lid)
        u.email = oe
        u.first_name = name
        u.save()

        messages = "Updated Successfully"
        return render(request, 'user/user_index.html', {'message': messages})


class ViewTurf(LoginRequiredMixin, TemplateView):
    template_name = 'user/view_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurf, self).get_context_data(**kwargs)
        s = Turf.objects.filter(status='Added')
        context['s'] = s
        return context

    def post(self, request, *args, **kwargs):
        type = request.POST['type']
        loc = request.POST['loc']
        host = Turf.objects.filter(
            game__icontains=type, location__icontains=loc, status='Added')
        return render(request, 'user/search.html', {'s': host})


class TurfDetails(LoginRequiredMixin, TemplateView):
    template_name = 'user/turf_details.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(TurfDetails, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        s = Turf.objects.get(pk=id)
        r = Rating.objects.filter(turf=s).count()
        print(r)
        re = Rating.objects.filter(turf=s)
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

        try:
            p = Package.objects.get(turf=s)

            tdt = p.tdate

            fdt = p.fdate
            today = datetime.datetime.today()
            # date_to = datetime.datetime.strptime(today, '%Y-%m-%d')
            date_t = datetime.datetime.strptime(tdt, '%Y-%m-%d')
            date_f = datetime.datetime.strptime(fdt, '%Y-%m-%d')
            if date_f <= today <= date_t:
                context['p'] = p
            else:
                pass
        except:
            pass
        context['s'] = s
        return context


class BookTurfs(LoginRequiredMixin, TemplateView):
    template_name = 'user/book_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(BookTurfs, self).get_context_data(**kwargs)
        try:
            dis = self.request.GET['dis']
            pack = self.request.GET['pack']
            tprice = self.request.GET['tprice']
            id = self.request.GET['tid']

            tp = int(tprice)-((int(tprice)*int(dis))/100)
            print(tp)
            context['p'] = tp
            context['pack'] = pack
            context['id'] = id
        except:
            tprice = self.request.GET['tprice']
            id = self.request.GET['tid']
            size = self.request.GET['size']
            context['pack'] = ""
            context['id'] = id
            context['p'] = tprice
            context['siz'] = size
        return context

    def post(self, request, *args, **kwargs):

        tf = request.POST['tf']
        bodate = request.POST['bodate']

        uti = request.POST['ti']
        nos = request.POST['nos']
        to = request.POST['to']
        no = request.POST['no']
        forw = request.POST['forw']

        ufti = datetime.datetime.strptime(uti, '%H:%M')
        utfis = ufti.time()
        print(utfis)

        end = ufti + timedelta(hours=int(no))
        allend = end.time()

        # end_t = datetime.datetime.strptime(end, '%H:%M')

        end_time = end.time()

        s = Turf.objects.get(pk=tf)
        u = Userreg.objects.get(user_id=self.request.user.id)

        stdu = BookTurf.objects.filter(
            b_date=bodate, turf=s, status__icontains='Booked') | BookTurf.objects.filter(
            b_date=bodate, turf=s, status__icontains='Accepted')
        for i in stdu:
            ed = i.end_time
            st = i.time

            eds = datetime.datetime.strptime(ed, '%H:%M:%S')
            edss = eds.time()
            sts = datetime.datetime.strptime(st, '%H:%M:%S')
            stss = sts.time()
            if stss <= utfis <= edss:
                messages = "This Time Period Is Already Booked.Please Choose Another.."
                return render(request, 'user/user_index.html', {'message': messages})

            else:

                continue

        t = BookTurf()

        t.time = utfis
        t.total = to
        t.turf = s
        t.forwhat = forw
        t.user = u
        t.no_per = nos
        t.noh = no
        t.b_date = bodate
        t.end_time = allend

        t.status = 'Pay'
        t.save()
        return render(request, 'user/payment.html', {'b_id': t.id, 'to': to})

        # try:
        #     bookmail(s.owner.user.username, s.name, bodate)
        #     messages = "Booked Successfully"
        #     return render(request, 'user/user_index.html', {'message': messages})
        # except:
        #     messages = "Booked Successfully"
        #     return render(request, 'user/user_index.html', {'message': messages})

        # std = BookTurf.objects.filter(
        #     b_date=bodate, time=utfis, turf=s, status__icontains='Booked').count()
        # stds = BookTurf.objects.filter(
        #     b_date=bodate, time=utfis, turf=s, status__icontains='Accepted').count()
        # if std > 0 or stds > 0:
        #     # std = BookTurf.objects.filter(b_date=bodate)
        #     #
        #     # for std in std:
        #     #     tti = std.time
        #     #     tnoh = std.noh
        #     #     fti = datetime.datetime.strptime(tti, '%I:%M')
        #     #     ftit = fti.time()
        #     #     s = fti + datetime.timedelta(hours=int(tnoh))
        #     #     st = s.time()
        #     #     sti = datetime.datetime.strptime(st, '%I:%M')
        #     #     stis = sti.time()
        #     #
        #     #
        #     #     if ftit <= utfis <= stis:
        #     messages = "This Time Period Is Already Booked.Please Choose Another.."
        #     return render(request, 'user/user_index.html', {'message': messages})

        # else:


class PaymentView(View):
    def dispatch(self, request, *args, **kwargs):
        bid = self.request.GET['bid']
        user = BookTurf.objects.get(pk=bid)
        user.status = 'Booked'

        user.save()

        return render(request, 'user/user_index.html', {'message': "Booked Successfully"})


class ViewTurfBooking(LoginRequiredMixin, TemplateView):
    template_name = 'user/view_turf_booking.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurfBooking, self).get_context_data(**kwargs)
        u = Userreg.objects.get(user_id=self.request.user.id)
        b = BookTurf.objects.filter(user_id=u).exclude(status='Pay')
        context['b'] = b
        return context


class AddFeedback(LoginRequiredMixin, TemplateView):
    template_name = 'user/feedback.html'
    login_url = '/'

    def post(self, request, *args, **kwargs):

        feed = request.POST['feed']

        u = Userreg.objects.get(user_id=self.request.user.id)
        f = Feedback()

        f.feed = feed
        f.user = u
        f.save()
        messages = "Feedback Added Successfully"
        return render(request, 'user/user_index.html', {'message': messages})


class AddTurfFeedback(LoginRequiredMixin, TemplateView):
    template_name = 'user/turf_feed.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AddTurfFeedback, self).get_context_data(**kwargs)
        id = self.request.GET['id']

        context['id'] = id
        return context

    def post(self, request, *args, **kwargs):

        feed = request.POST['feed']
        id = request.POST['id']

        t = Turf.objects.get(pk=id)

        u = Userreg.objects.get(user_id=self.request.user.id)
        f = TurfFeedback()

        f.feed = feed
        f.turf = t
        f.user = u
        f.save()
        messages = "Feedback Added Successfully"
        return render(request, 'user/user_index.html', {'message': messages})


class ViewTurfFeedback(LoginRequiredMixin, TemplateView):
    template_name = 'user/view_turf_feed.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurfFeedback, self).get_context_data(**kwargs)
        id = self.request.GET['id']

        t = TurfFeedback.objects.filter(turf=id)

        context['t'] = t
        return context


class CancelBooking(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET.get('book_id')
        print(id)
        today = datetime.date.today()
        b = BookTurf.objects.get(pk=id)
        bdate = b.b_date
        # sd_obj = datetime.datetime.strptime(today, '%Y-%m-%d')
        fd_obj = datetime.datetime.strptime(bdate, '%Y-%m-%d')
        fd_obj_minus = fd_obj - datetime.timedelta(days=3)
        minus = fd_obj_minus.date()
        if today < minus:
            total = b.total
            per = (int(float(total))/10)*3
            gt = int(float(total))-int(per)

            b.status = 'Cancel'
            b.total = gt
            b.save()
            dict = {'name': 'true'}
            sorted_string = json.dumps(dict)
            # print(sorted_string)
            print("true")
            return JsonResponse(sorted_string, safe=False)

        else:
            dict = {'name': 'false'}
            sorted_string = json.dumps(dict)
            # print(sorted_string)
            print("false")
            return JsonResponse(sorted_string, safe=False)

        # return redirect(request.META['HTTP_REFERER'])


class AddRate(LoginRequiredMixin, TemplateView):
    template_name = 'user/add_rate.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AddRate, self).get_context_data(**kwargs)
        u = self.request.GET['id']
        context['u'] = u
        return context

    def post(self, request, *args, **kwargs):

        rate = request.POST['rate']
        id = request.POST['id']
        us = Userreg.objects.get(user_id=self.request.user.id)

        s = Turf.objects.get(pk=id)

        u = Rating()
        u.rate = rate
        u.turf = s
        u.user = us

        u.save()
        messages = "Rate Added Successfully"
        return render(request, 'user/user_index.html', {'message': messages})
