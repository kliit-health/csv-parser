list_one = open('old.csv','r')
list_two = open('new.csv','r')

clean_list = open('clean.csv', 'w')

previous_students = []
new_students = []

def clean_phone_number(list_item):
    item_to_clean = list_item.split(",")
    cleaned_item = ""
    for entry in item_to_clean[3]:
        if entry.isdigit():
            cleaned_item += entry
    item_to_clean[3] = cleaned_item + "\n"
    if len(item_to_clean) > 4:
        del item_to_clean[4]

    joined = ","

    sanitized = joined.join(item_to_clean)

    return sanitized

def clean_email(list_item):

    item_to_clean = list_item.split(",")
    item_to_clean[2] = item_to_clean[2].lower()
    joined = ","
    sanitized = joined.join(item_to_clean)

    return sanitized

for list_one_entry in list_one:
    clean_one = list_one_entry
    clean_phone = clean_phone_number(clean_one)
    cleaned = clean_email(clean_phone)
    previous_students.append(cleaned)

for list_two_entry in list_two:
    clean_two = list_two_entry
    clean_phone = clean_phone_number(clean_two)
    cleaned = clean_email(clean_phone)
    new_students.append(cleaned)

if len(previous_students) >= len(new_students):
    for entry in new_students:
        if entry not in previous_students:
            clean_list.write(entry)
             
else:
    for entry in new_students:
        if entry in previous_students:
            continue
        else:
            clean_list.write(entry)



clean_list.close()
list_one.close()
list_two.close()
