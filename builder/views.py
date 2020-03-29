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

    # amount_body_elements means how high will be your robot
    amount_body_elements = request.GET.get("height")
    user_message = request.GET.get("message")
    robot_name = request.GET.get("name")
    robot_number = random.randint(13849, 78999)
    amount_body_elements = int(amount_body_elements) - 2
    img_format = ".png"

    robot_id = "Robot ID: #" + str(robot_number) + " a.k.a. " + robot_name
    # all_body_elements means how much body variations you have for each variant (hostile, friendly)
    all_body_elements = 3

    for x in range(1, all_body_elements + 1):
        globals()["body_element_{0}".format(x)] = ""

    legs_number = "legs_" + str(random.randint(1, 3)) + img_format
    id_cloud_number = 1
    for x in range(1, 4):
        globals()["cloud_number_{0}".format(x)] = '<img src="/media/' + "cloud_" + str(
            random.randint(1, 3)) + img_format + """" onerror="this.style.display='none'" width='25' """ + f"""id='id_cloud_{id_cloud_number}'""" + "><br>"
        id_cloud_number += 1

    hostile_variants = list("!@#$%^&*<>?{}[]|\/-_=+")

    friendly_variants = ["Blip ", "Blap ", "Blop ", "Pip ", "Bip ", "Clank "]

    message_length = random.randint(3, 7)
    robot_type = request.GET.get("status")
    message = ""
    id_body_number = 1

    if robot_type == "hostile":
        for variant in range(message_length):

            message += random.choice(hostile_variants)
        variant_option = "_hostile"
        message += " !!11! "
        head_number += variant_option + img_format

    if robot_type == "friendly":
        for variant in range(message_length):
            message += random.choice(friendly_variants)
        variant_option = "_friendly"
        message += "^.^ "
        head_number += variant_option + img_format

    for x in range(1, amount_body_elements + 1):
        globals()["body_element_{0}".format(x)] = '<img src="/media/' + "body_element_" + str(
            random.randint(1, all_body_elements)) + variant_option + img_format + """" onerror="this.style.display='none'" width='200' """ + f"""id='id_body_{id_body_number}'""" + "><br>"
        id_body_number += 1

        message += str(user_message)

    return render(request, "builder/your_robot.html", {"message": message, "head_number": head_number,
                                                       "body_element_1": body_element_1,
                                                       "body_element_2": body_element_2,
                                                       "body_element_3": body_element_3,
                                                       "robot_id": robot_id,
                                                       "legs_number": legs_number,
                                                       "cloud_number_1": cloud_number_1,
                                                       "cloud_number_2": cloud_number_2,
                                                       "cloud_number_3": cloud_number_3,
                                                       "amount_body_elements": amount_body_elements})


def about(request):
    return render(request, "builder/about.html")
