import re

def parse_query(query):
    age = re.search(r'(\d+)-year-old', query)
    gender = 'male' if 'male' in query else 'female' if 'female' in query else 'unknown'
    location = re.search(r'in (\w+)', query)
    policy_age = re.search(r'(\d+)-month-old', query)
    procedure = re.search(r'(surgery|procedure) on (\w+\s?\w+)', query)

    return {
        "age": int(age.group(1)) if age else None,
        "gender": gender,
        "location": location.group(1) if location else None,
        "procedure": procedure.group(2) if procedure else None,
        "policy_age_months": int(policy_age.group(1)) if policy_age else None
    }