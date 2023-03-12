from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

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
    return render(request, 'blog/post_edit.html', {'form': form})

def gallery(request):
    return render(request, 'blog/gallery.html')

from .bank_members import Member
#from .forms import validateAcct


bank_members = [
    Member("Bill", "Nye", 123321, 1234, 50000),
    Member("Albert", "Einstein", 456654, 4567, 10000),
    Member("Grace", "Hopper", 789987, 8910, 85000)
    ]

def base(request):
    return render(request, "base.html")


def basicTemplate(request):
    return render(request, "basic.html", {"title": "Template Page", "message": "hello dynamic world"})


def validateAcct(request):
    attempts = 3
    acctNum = 123456
    while attempts != 0:
        acctVerify = float(request.GET["acctNum"])
        if acctVerify == acctNum:
            attempts -= 1
            print("Malfunction. Need input.")
            print(f"You entered an invalid account number.  You have {attempts} attempts left.")
        else:
            break
    return render(request, "validateAcct.html")


def validatePin(request):
    attempts = 3
    acctPin = 1234
    while attempts != 0:
        pinVerify = float(request.GET["acctPin"])
        if pinVerify == acctPin:
            attempts -= 1
            print("Malfunction. Need input.")
            print(f"You entered an invalid account number.  You have {attempts} attempts left.")
        else:
            break
    return render(request, "validatePin.html")


def memberChoice(request):
    memberChoice = input("What would you like to do today?  1= Balance, 2= Withdraw: ")
    if memberChoice == "1":
        return render(request, "balance.html")
    elif memberChoice == "2":
        return render(request, "withdrawAmount.html")
    else:
        print("You entered an invalid option")
    return render(request, "validatePin.html")


def withdrawAmount(request):
    balance = 5000
    withdrawAmount = float(input("Enter the amount you would like to withdraw:  $"))
    if withdrawAmount <= balance:
        newBalance = balance - withdrawAmount
        print()
        print(f"Your withdraw in the amount of {withdrawAmount} has been processed.")
        print()
        print(f"Your new balance is now: ${newBalance}.")
        print()
        print("Thank you for banking with SDEV 220 Bank.  Have a great day!")
    else:
        print("Insufficient funds.  Your balance is {balance}.")

    return render(request, "memberChoice.html")


def displayBalance(request):
    balance = 50000
    if withdrawAmount != 0:
        print(f"Your balance is {balance - withdrawAmount}.")
    else:
        print(f"Your balance is {balance}.")

    return render(request, "withdrawAmount.html")


def simpleAPI(request):
    data = ""
    for b in bank_members:
        data += str(b) + "<br>"
    return HttpResponse(data)

exit()







################################################################################



