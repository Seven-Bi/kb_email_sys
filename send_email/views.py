from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from .forms import EmailForm
from django.core.mail import EmailMessage
import traceback



def index(request):
	form = EmailForm()
	return render(request, 'send_email/send_email_end.html', {'form': form})


def send_off(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			customer_email = form.cleaned_data['contact_email']
			email_content = form.cleaned_data['email_content']
			if customer_email:
				email = EmailMessage(
					subject='Warm Greeting',
					body=email_content,
					from_email='it@bhkb.com.au',
					to=[customer_email,],
				)
				email.content_subtype = 'html'
				try:
					email.send(fail_silently=False)
					return JsonResponse({'output': 'yes!!!'})
				except Exception:
					print(traceback.format_exc())				
			else:
				return JsonResponse({'output': 'no email data'})
		else:
			print(form.cleaned_data['email_content'])
			return JsonResponse({'output': 'form data errors'})
	else:
		return JsonResponse({'output': 'invalid request'})
