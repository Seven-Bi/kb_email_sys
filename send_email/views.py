#############################
# Author: Chen Bi
# Date: 18 May 2020
#############################

from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from .forms import EmailForm
from django.core.mail import EmailMessage
from concurrent.futures import ThreadPoolExecutor as Executor
import traceback
import time



group_email = ['seven.albany.bi@live.com.au', 'steven.bb.0221@gmail.com', 'seven.albany.bi@gmail.com', '258933996@qq.com', 'yumeng950411@gmail.com', '353260410@qq.com', 'Tang353260410@gmail.com']
executor = Executor(max_workers=2)


#############################
# Index view
#############################
def index(request):
	form = EmailForm()
	return render(request, 'send_email/send_email_end.html', {'form': form})



#############################
# Group-Email send function
#############################
def send_group_emails(subject, body, sender, receiver):
	email = EmailMessage(subject=subject,body=body, 
		from_email=sender, to=[receiver,])
	email.content_subtype = 'html'
	try:
		email.send(fail_silently=False)
		# next = request.POST.get('next', '/')
		# return JsonResponse({'output': 'yes!!!'})
	except Exception:
		pass
		# print(traceback.format_exc())


#############################
# Group-Email send view
#############################
def send_off(request):
	if request.method == 'POST':
		start = time.time()
		form = EmailForm(request.POST)
		if form.is_valid():
			# customer_email = form.cleaned_data['contact_email']
			email_content = form.cleaned_data['email_content']
			for single_email in group_email:

				executor.submit(send_group_emails, 'Warm Greeting', email_content, 'it@bhkb.com.au', single_email)

			end = time.time()
			time_cost = str(end - start)
			return JsonResponse({'output': time_cost})
		else:
			return JsonResponse({'output': 'form data errors'})
	else:

		return JsonResponse({'output': 'invalid request'})






# def send_off(request):
# 	if request.method == 'POST':
# 		form = EmailForm(request.POST)
# 		if form.is_valid():
# 			customer_email = form.cleaned_data['contact_email']
# 			email_content = form.cleaned_data['email_content']
# 			if customer_email:
# 				email = EmailMessage(
# 					subject='Warm Greeting',
# 					body=email_content,
# 					from_email='it@bhkb.com.au',
# 					to=[customer_email,],
# 				)
# 				email.content_subtype = 'html'
# 				try:
# 					email.send(fail_silently=False)
# 					# next = request.POST.get('next', '/')
# 					return JsonResponse({'output': 'yes!!!'})
# 				except Exception:
# 					print(traceback.format_exc())				
# 			else:
# 				return JsonResponse({'output': 'no email data'})
# 		else:
# 			return JsonResponse({'output': 'form data errors'})
# 	else:

# 		return JsonResponse({'output': 'invalid request'})
