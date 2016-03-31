import json


def _cleanup_empty_entries(data_dict):
    for key in data_dict.keys():
        if not data_dict[key]:
            del data_dict[key]
    return data_dict


def cleanup(data):
    orgs_list = data.get('profile').get('person_data').get('organizations', False)
    if orgs_list:
        for org in orgs_list:
            org = _cleanup_empty_entries(org)
    for org in orgs_list:
        if not org:
            orgs_list.remove(org)
    data = _cleanup_empty_entries(data)
    return data

