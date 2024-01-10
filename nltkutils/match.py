from app1.models import profile
from django.contrib.auth.models import User,auth
from django.forms.models import model_to_dict


    


def matchfun(work,profiles):
    matched = []
    for i in profiles:
        if i["work"] == work:
            matched.append(i["id"])
            
    return matched

