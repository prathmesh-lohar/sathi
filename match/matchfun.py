def matchfun(profiles,data):
    
    matched_results = []
    matched_fields = []
    for profile in profiles:
        num_fields_matched = 0  # Count of matched fields for this profile

        for field in data[0]:  # Assuming data only contains one item
            if field in profile and data[0][field] == profile[field]:
                num_fields_matched += 1
                matched_fields.append(field)

        if num_fields_matched > 0:
            matched_results.append({'id': profile['id'], 'num_fields_matched': num_fields_matched})

    # Sort the matched results by the number of matched fields in descending order
    matched_results.sort(key=lambda x: x['num_fields_matched'], reverse=True)

    # Extract the IDs and fields from the sorted results
    matched_ids = [result['id'] for result in matched_results]
    # Ensure it's the same length as matched_ids
    matched_fields = matched_fields[:len(matched_ids)]

    #print("Matched IDs:", matched_ids)
    #print("Matched Fields:", matched_fields)
    return matched_ids
