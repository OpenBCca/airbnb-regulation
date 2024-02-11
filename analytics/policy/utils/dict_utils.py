def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict
