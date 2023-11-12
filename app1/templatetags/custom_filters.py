from django import template
from app1.models import profile
from django.contrib.auth.models import User,auth
import math

register = template.Library()

@register.filter
def custom_filters(id,cuid):
    try:
        
        per = 0
        li = []
        cuserp = profile.objects.get(id=cuid)
        muserp = profile.objects.get(id=id)
        
        if cuserp.work==muserp.work:
            per +=10
            li.append('work')
        if cuserp.marrital_status==muserp.marrital_status:
            per +=10
            li.append('ms')

        
        if cuserp.dob==muserp.dob:
            per +=10
            li.append('dob')
            
        if cuserp.height==muserp.height:
            per +=10
            li.append('height')
            
        if cuserp.color==muserp.color:
            per +=10
            li.append('color')
            
        if cuserp.Qualification==muserp.Qualification:
            per +=10
            li.append('qli')
            
        if cuserp.experience==muserp.experience:
            per +=10
            li.append('ex')
            
        if cuserp.hobbies==muserp.hobbies:
            per +=10
            li.append('hob')
            
        if cuserp.income==muserp.income:
            per +=10
            li.append('inc')

        if cuserp.medical_condition==muserp.medical_condition:
            per +=10
            li.append('mc')

        if cuserp.city==muserp.city:
            per +=10
            li.append('ct')
            
            
        print(li)
        
        max = 110
        
        tres = (per/max)*100
        res = math.ceil(tres)
            
        return res  # Replace with the actual field you want to retrieve
    except profile.DoesNotExist:
        return "Not found"  # You can customize the return value for non-existent IDs


@register.filter(name='sort_filter')
def sort_filter(value):
    
    value=str(value)
    chars_to_remove = "[{}]"

    for t in chars_to_remove:
        value=value.replace(t, " ")
        value=value.replace('"', " ")
        value = value.replace('value : ', '')

        
    return value