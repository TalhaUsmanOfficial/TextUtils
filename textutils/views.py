"""
Created On Sun August 25 11:27 PM 2024

@author: Talha Usman
Status: Learner
"""

# ! I Have Created This File - Talha Usman
from django.http import HttpResponse
import os
from django.shortcuts import render

# ! Code For Video 06-Ex-01 Personal Navigator.py
# def index(requests):
#     return HttpResponse(
#         """<h1>Hello Mr. Talha</h1>\n<h4>Open Chat GPT</h4>\n<a href = "https://chatgpt.com/">Chat GPT</a>
#         <h4>Open Youtube</h4>\n<a href = "https://www.youtube.com/">Youtube</a>
#         <h4>Open Google</h4>\n<a href = "https://www.google.com/">Google</a>"""
#     )


# def about(requests):
#     """At The End Of Your Web Address Type /about To Check The Text Of About Function"""
#     return HttpResponse("About Mr Talha")


# def open_txt(requests):
#     file_name = r"textutils\content.txt"

#     with open(file_name, "r") as file:
#         read_content = file.read()
#         return HttpResponse(read_content)


# ! Code For Video 07-Laying Pipeline.py


# def index(request):
#     return HttpResponse("<h4>Home</h4>")


# def remove_punc(request):
#     return HttpResponse("Remove Punc")


# def cap_first(request):
#     return HttpResponse("Cap First")


# def new_line_remove(request):
#     return HttpResponse("New Line Remove")


# def space_remover(request):
#     return HttpResponse("Space Remover")


# def char_counter(request):
#     return HttpResponse("Character Counter")


# ! Code For Video 08-Templates.py

# ? from django.shortcuts import render Don't Forget To Import This


# def index(request):
#     # ! render(request, name_of_file.html)
#     params = {
#         "name": "Talha",
#         "place": "Lahore",
#     }
#     return render(request, "index.html", params)
#     # return HttpResponse("<h4>Home</h4>")


# def remove_punc(request):
#     return HttpResponse("Remove Punc")


# def cap_first(request):
#     return HttpResponse("Cap First")


# def new_line_remove(request):
#     return HttpResponse("New Line Remove")


# def space_remover(request):
#     return HttpResponse("Space Remover")


# def char_counter(request):
#     return HttpResponse("Character Counter")


# ! Code For Video 09-Creating Home Page.py

# ? from django.shortcuts import render Don't Forget To Import This


# def index(request):
#     # ! render(request, name_of_file.html)
#     params = {
#         "name": "Talha",
#         "place": "Lahore",
#     }
#     return render(request, "index.html", params)
#     # return HttpResponse("<h4>Home</h4>")


# def remove_punc(request):
#     # ! "text" Is The Name Of textarea You Passed In index.html
#     # ! If User Doesn't Type So It Prints The default On Terminal
#     my_text = request.GET.get("text", "default")
#     print(my_text)
#     return HttpResponse("Remove Punc")


# def cap_first(request):

#     return HttpResponse("Cap First")


# def new_line_remove(request):
#     return HttpResponse("New Line Remove")


# def space_remover(request):
#     return HttpResponse("Space Remover")


# def char_counter(request):
#     return HttpResponse("Character Counter")

# ! Code For Video 10-Coding The Backend.py

# ? from django.shortcuts import render Don't Forget To Import This


# def index(request):
#     # ! render(request, name_of_file.html)
#     params = {
#         "name": "Talha",
#         "place": "Lahore",
#     }
#     return render(request, "index.html", params)
#     # return HttpResponse("<h4>Home</h4>")


# def analyze(request):
#     # ! "text" Is The Name Of textarea You Passed In index.html
#     # ! If User Doesn't Type So It Prints The 'default' On The Terminal
#     my_text = request.GET.get("text", "default")
#     # ! If User On The removepunc Button So It Shows On Else Off
#     remove_punc = request.GET.get("removepunc", "off")
#     full_caps = request.GET.get("full_caps", "off")
#     new_line_remover = request.GET.get("new_line_remover", "off")
#     extra_space_remover = request.GET.get("extra_space_remover", "off")
#     print(f"Punctuation: {remove_punc}")
#     print(f"UPPERCASE: {full_caps}")
#     print(my_text)
#     punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_`~="""
#     analyzed = my_text

#     if remove_punc != "off":
#         analyzed = "".join(char for char in analyzed if char not in punctuations)
#         operation = "Punctuations Removed"
#     else:
#         operation = "Punctuations Not Removed"

#     if full_caps != "off":
#         analyzed = analyzed.upper()

#         operation += ", Converted To UPPERCASE"
#     else:
#         operation += ", Not Converted To UPPERCASE"

#     if new_line_remover != "off":
#         analyzed = analyzed.replace("\n", " ").replace("\r", "")
#         operation += ", New Lines Removed"
#     else:
#         operation += ", New Lines Not Removed"

#     if extra_space_remover != "off":
#         plate_text = ""
#         for idx, char in enumerate(analyzed):
#             if analyzed[idx] == " " and analyzed[idx + 1] == " ":
#                 continue
#             else:
#                 plate_text += char
#         analyzed = plate_text
#         operation += ", Extra Spaces Removed"
#     else:
#         operation += ", Extra Spaces Not Removed"

#     params = {
#         "purpose": "Remove Punctuations",
#         "analyzed_text": analyzed,
#         "status": operation,
#         "total_char": len(analyzed),
#     }
#     return render(request, "analyze.html", params)


# def remove_punc(request):
#     # ! "text" Is The Name Of textarea You Passed In index.html
#     # ! If User Doesn't Type So It Prints The default On Terminal
#     my_text = request.GET.get("text", "default")
#     print(my_text)
#     return HttpResponse("Remove Punc")


# def cap_first(request):

#     return HttpResponse("Cap First")


# def new_line_remove(request):
#     return HttpResponse("New Line Remove")


# def space_remover(request):
#     return HttpResponse("Space Remover")


# def char_counter(request):
#     return HttpResponse("Character Counter")

# ! Code For Video 15-CSRF Tokens And Post Requests.py

# ? from django.shortcuts import render Don't Forget To Import This


def index(request):
    """<h1>Info:</h1>
    This Is Just A Simple Code Which Is Sending Name And Place To index.html
    """
    # ! render(request, name_of_file.html)
    params = {
        "name": "Talha",
        "place": "Lahore",
    }
    return render(request, "index.html", params)


def analyze(request):
    # ! "text" Is The Name Of textarea You Passed In index.html
    # ! If User Doesn't Type So It Prints The 'default' On The Terminal
    # ? We Use request.POST.get() Instead of request.GET.get()
    # * Also The Method 'get' To Post In Form Of index.html
    my_text = request.POST.get("text", "default")
    # ! If User On The removepunc Button So It Shows On Else Off
    remove_punc = request.POST.get("removepunc", "off")
    full_caps = request.POST.get("full_caps", "off")
    new_line_remover = request.POST.get("new_line_remover", "off")
    extra_space_remover = request.POST.get("extra_space_remover", "off")
    # print(f"Punctuation: {remove_punc}")
    # print(f"UPPERCASE: {full_caps}")
    # print(my_text)
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_`~="""
    analyzed = my_text

    if remove_punc != "off":
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        operation = "Punctuations Removed"
    else:
        operation = "Punctuations Not Removed"

    if full_caps != "off":
        analyzed = analyzed.upper()

        operation += ", Converted To UPPERCASE"
    else:
        operation += ", Not Converted To UPPERCASE"

    if new_line_remover != "off":
        analyzed = analyzed.replace("\n", " ").replace("\r", "")
        operation += ", New Lines Removed"
    else:
        operation += ", New Lines Not Removed"

    if extra_space_remover != "off":
        plate_text = ""
        for idx, char in enumerate(analyzed):
            if analyzed[idx] == " " and analyzed[idx + 1] == " ":
                continue
            else:
                plate_text += char
        analyzed = plate_text
        operation += ", Extra Spaces Removed"
    else:
        operation += ", Extra Spaces Not Removed"

    params = {
        "purpose": "Remove Punctuations",
        "analyzed_text": analyzed,
        "status": operation,
        "total_char": len(analyzed),
    }

    return render(request, "analyze.html", params)


# def remove_punc(request):
#     # ! "text" Is The Name Of textarea You Passed In index.html
#     # ! If User Doesn't Type So It Prints The default On Terminal
#     my_text = request.GET.get("text", "default")
#     print(my_text)
#     return HttpResponse("Remove Punc")


# def cap_first(request):

#     return HttpResponse("Cap First")


# def new_line_remove(request):
#     return HttpResponse("New Line Remove")


# def space_remover(request):
#     return HttpResponse("Space Remover")


# def char_counter(request):
#     return HttpResponse("Character Counter")
