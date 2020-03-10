from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, "builder/home.html")


def builder(request):
    return render(request, "builder/builder.html")


def your_robot(request):

    head_number = "head_" + str(random.randint(1, 3))
    body_element_1 = ""
    body_element_2 = ""
    body_element_3 = ""
    amount_body_elements = request.GET.get("height")

    # for body_element in range(amount_body_elements):
    #    message += random.choice(hostile_variants)

    legs_number = "legs_" + str(random.randint(1, 3))

    # Check how many body elements
    # Random numbers for head (hostile of friendly)
    # Random numbers for body elements (hostile of friendly)
    # Random numbers for legs

    hostile_variants = list("!@#$%^&*<>?{}[]|\/-_=+")

    friendly_variants = ["Blip ", "Blap ", "Blop ", "Pip ", "Bip ", "Clank "]

    message_length = random.randint(4, 10)
    robot_type = request.GET.get("status")
    message = ""

    if robot_type == "hostile":
        for variant in range(message_length):
            message += random.choice(hostile_variants)
        message += " !!11!"
        head_number += "_hostile"

    if robot_type == "friendly":
        for variant in range(message_length):
            message += random.choice(friendly_variants)
        message += "^.^"
        head_number += "_friendly"



    return render(request, "builder/your_robot.html", {"message": message, "amount_body_elements": amount_body_elements, "head_number": head_number})


def about(request):
    return render(request, "builder/about.html")
