from app1.models import profile

p = profile.objects.values('id','work','Qualification')
profiles = list(p)

data_to_match = {"id": "30", "work": "software","Qualification":"B.Tech"}





matched_results = []
matched_fields = []



for profile in profiles:
    matched_fields_profile = []
    for field,value in data_to_match.items():
        if field in profile and profile[field] == value:
            matched_fields_profile.append(field)
    
    if matched_fields_profile:
        matched_results.append(profile["id"])
        matched_fields.append(matched_fields_profile)

print("matched id", matched_results)
print("matched fields", matched_fields)