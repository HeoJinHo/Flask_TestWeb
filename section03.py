import simplejson as json

test_dict = {'1': 84, '4': 77, '3': 65}

print(json.dumps(test_dict, sort_keys=True, indent=4 * ''))