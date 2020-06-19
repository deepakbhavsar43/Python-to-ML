my_nested_dict = {"global": {"peers": {"15.1.1.1": {"remote_id": "15.1.1.1", "address_family": {"ipv4": {"sent_prefixes": 1, "received_prefixes": 4, "accepted_prefixes": 4}}, "remote_as": 65002, "uptime": 13002, "is_enabled": True, "is_up": True, "description": "== R3 BGP Neighbor ==", "local_as": 65002}}, "router_id": "15.1.1.2"}}

filtered_list = ['peers', 'remote_id', 'remote_as', 'uptime']

def seek_keys(d, key_list):
    for k, v in d.items():
        if k in key_list:
            if isinstance(v, dict):
                print(k + ": " + list(v.keys())[0])
            else:
                print(k + ": " + str(v))
        if isinstance(v, dict):
            seek_keys(v, key_list)

seek_keys(my_nested_dict, filtered_list)