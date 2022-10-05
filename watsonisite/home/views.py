from django.shortcuts import render
from django.shortcuts import HttpResponse
import mysql.connector
from django.shortcuts import render, redirect
import sqlite3

# Create your views here.


def home(requests):
    return render(requests, 'home.html')


def login(requests):
    return HttpResponse("Login page")


def calc(requests):
    return render(requests, 'calc.html')


def contact(requests):
    return render(requests, 'contact copy.html')


def faq(requests):
    return render(requests, 'faq2.html')


def news(requests):
    return render(requests, 'news copy.html')


def subscribe(requests):
    if requests.method == 'POST':
        firstname = requests.POST['firstname']
        lastname = requests.POST['lastname']
        email = requests.POST['email']

        cursor = sqlite3.connect('database.db')

        # mydb = mysql.connector.connect(
        # host='vatsa312.mysql.pythonanywhere-services.com', user='vatsa312', passwd='watsonisite', database='Users', autocommit='true')

        # cursor = myd2.cursor()

        cursor.execute(
            f"insert into user values ('{firstname}', '{lastname}', '{email}')")
        cursor.commit()
        print("User login done")
        return redirect('/')
    # return render(requests, 'subscribe.html')
    else:
        return render(requests, 'subscribe.html')


def Bitocin(requests):
    return render(requests, 'Bitcoin.html')


def Ethereum(requests):
    return render(requests, 'Ethereum.html')


def XRP(requests):
    return render(requests, 'XRP.html')


def Cardano(requests):
    return render(requests, 'Cardano.html')


def Dogecoin(requests):
    return render(requests, 'Dogecoin.html')
