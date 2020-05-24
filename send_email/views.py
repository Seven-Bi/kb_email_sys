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
from django.template.loader import render_to_string
from .read_email_data import read_data_from_excel
import traceback
import time


all_client_emails = []
# group_email = ['seven.albany.bi@live.com.au', 'steven.bb.0221@gmail.com', 'seven.albany.bi@gmail.com']
# group_email = ['meigao40@yahoo.com.au','seven.albany.bi@live.com.au', 'steven.bb.0221@gmail.com', 'seven.albany.bi@gmail.com', '258933996@qq.com', 'yumeng950411@gmail.com', '353260410@qq.com', 'Tang353260410@gmail.com']
# boss = 'meigao40@yahoo.com.au'

executor = Executor(max_workers=3)

map_dict_email = {
	'a': 'Email Group',
	'b': 'Email One',
	'c': 'Email All',
	'd': 'Schedule Email'
}

map_dict_template = {
	'1': 'Best Offer',
	'2': 'Promotion',
	'3': 'For Our Member',
	'4': 'New Event'
}

current_template = 'new_demo'
email_strategy = 'Email Group'
template_chose = 'Best Offer'


#############################
# Index view
#############################
def index(request):
	form = EmailForm()
	global template_chose
	global email_strategy
	global current_template
	global email_strategy
	return render(request, 'send_email/send_email_end.html', {'form': form, 'email_strategy': email_strategy, 'template_chose': template_chose})

# update page email strategy select
def email_strategy_select(request, strategy):
	form = EmailForm()
	global template_chose
	global current_template
	global email_strategy
	email_strategy = map_dict_email[strategy]
	return render(request, 'send_email/send_email_end.html', {'form': form, 'email_strategy': email_strategy, 'template_chose': template_chose})

# update page email template select
def email_template(request, template):
	form = EmailForm()
	global current_template
	global email_strategy
	global current_template
	template_chose = map_dict_template[template]
	return render(request, 'send_email/send_email_end.html', {'form': form, 'email_strategy': email_strategy, 'template_chose': template_chose})


#
def change_template(request, template_name):
	current_template = template_name


#
def get_latest_email_data(request):
	form = EmailForm()
	global template_chose
	global email_strategy
	global current_template
	global email_strategy

	global all_client_emails
	all_client_emails.clear()
	all_client_emails = read_data_from_excel()
	all_client_emails.append('manager@bhkb.com.au')
	all_client_emails.append('meigao40@yahoo.com.au')
	all_client_emails.append('philip.hooper@myboulevarde.com.au')
	all_client_emails.append('steven.bb.0221@gmail.com')
	all_client_emails = all_client_emails[3100:3121]
	print(all_client_emails)

	return render(request, 'send_email/send_email_end.html', {'form': form, 'email_strategy': email_strategy, 'template_chose': template_chose})



#############################
# Enable template quick-view
#############################
def staticpage(request):
	return render(request, 'send_email/'+ current_template +'.html')


#############################
# Email send function
#############################
def send_group_emails(subject, body, sender, receiver):
	email = EmailMessage(subject=subject,body=body, 
		from_email=sender, to=[receiver,])
	email.content_subtype = 'html'
	try:
		email.send(fail_silently=False)
	except Exception:
		warnings.warn('<' + receiver + '> email is failed to send')
		logging.info(traceback.format_exc())
		pass


#############################
# Group-Email send view
#############################
def send_off(request):
	global all_client_emails
	if request.method == 'POST':
		start = time.time()
		form = EmailForm(request.POST)
		if form.is_valid():
			# customer_email = form.cleaned_data['contact_email']
			# email_content = form.cleaned_data['email_content']
			html_content = render_to_string('send_email/new_demo.html')
			email_content = html_content

			# for single_email in group_email:
			for single_email in all_client_emails:
				# thread pool launchs new work thread
				executor.submit(send_group_emails, 'Greeting', email_content, 'it@bhkb.com.au', single_email)


			end = time.time()
			time_cost = str(end - start)
			# return JsonResponse({'output': time_cost})
			return JsonResponse({'output': 'all done:>'})
		else:
			return JsonResponse({'output': 'form data errors'})
	else:

		return JsonResponse({'output': 'invalid request'})

