import json
from app1.models import profile
from django.forms.models import model_to_dict

from django.core import serializers

data = serializers.serialize("json",profile.objects.all())

print(data['work'][0])


# con = profile.objects.all().first()
# con = model_to_dict(con)
# print(con)

# def profiles():
#     data = profile.objects.all().values()
#     json_data = json.dumps(list(data))
#     print(json_data)

# profile()


