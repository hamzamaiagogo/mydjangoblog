from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from maiagogo.models import Post, Contact
from maiagogo.forms import PostForm, ContactForm
from maiagogo.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def aboutMe(request):
  return render(request, 'Aboutme.html',{})

def ramadan(request):
  return render(request, 'ramadan.html',{})

def islam(request):
  return render(request, 'islam.html',{})


def sample(request):
  return render(request, 'post.html',{})

def About(request):
    posts=Post.objects.order_by('-published_date')
    #posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_new(request):
	if request.method == "POST":
           form	= PostForm(request.POST)
	   if form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.published_date = timezone.now()
		post.save()
		return	redirect('post_detail',	pk=post.pk)
	else:
	      form = PostForm()
	return	render(request,	'post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

 
def contact(request):
	if request.method == "POST":
           form	= ContactForm(request.POST)
	   if form.is_valid():
		form.save(commit=True)
		return	redirect(About)
           else: 
# The supplied form contained errors - just print them to the terminal. 
               print form.errors  
	else:
	      form = ContactForm()
	return	render(request,	'contact.html', {'form': form})
def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code change
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
       # Attempt to grab information from the raw form information.
       # Note that we make use of both UserForm and UserProfileForm.
       user_form = UserForm(data=request.POST)
       profile_form = UserProfileForm(data=request.POST)
       # If the two forms are valid...
       if user_form.is_valid() and profile_form.is_valid():
          # Save the user's form data to the database.
          user = user_form.save()
          # Now we hash the password with the set_password method.
          # Once hashed, we can update the user object.
          user.set_password(user.password)
          user.save()
          # Now sort out the UserProfile instance.
          # Since we need to set the user attribute ourselves, we set commit=False.
          # This delays saving the model until we're ready to avoid integrity problems.
          profile = profile_form.save(commit=False)
          profile.user = user
           # Did the user provide a profile picture?
           # If so, we need to get it from the input form and put it in the UserProfile model.
          if 'picture' in request.FILES:
              profile.picture = request.FILES['picture']
          # Now we save the UserProfile model instance.
          profile.save()
# Update our variable to tell the template registration was successful.
          registered = True
# Invalid form or forms - mistakes or something else?
# Print problems to the terminal.
# They'll also be shown to the user.
       else:
               print user_form.errors, profile_form.errors
# Not a HTTP POST, so we render our form using two ModelForm instances.
# These forms will be blank, ready for user input.
    else:
          user_form = UserForm()
          profile_form = UserProfileForm()
# Render the template depending on the context.
    return render(request,
'register.html',
{'user_form': user_form, 'profile_form': profile_form, 'registered': registered } )

def user_login(request):
        context_dict = {}
	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']
		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)
		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user is not None:
			# Is the account active? It could have been disabled.
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/maiagogo/')
			else:
                                context_dict['disabled_account'] = True
				# An inactive account was used - no logging in!
				return render(request, 'login.html', context_dict)
		else:
			# Bad login details were provided. So we can't log the user in.
			print "Invalid login details: {0}, {1}".format(username, password)
                        context_dict['bad_details'] = True
			return render(request, 'login.html', context_dict)
			# The request is not a HTTP POST, so display the login form.
			# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render(request, 'login.html', {})
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/maiagogo/')





