hscience = {'ann':50,'sammy':89,'eric':2}
math= {'sue':58,'sammy':96,'eric':1}
def merge_dicts(dict1,dict2):
    totals_dict = dict1.copy()
    for key, value in dict2.items():
        if key in totals_dict:
            totals_dict[key] += value
        else:
            totals_dict[key] = value
    return totals_dict
print(merge_dicts(math,hscience))