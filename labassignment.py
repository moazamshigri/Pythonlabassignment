print("Hello world")
names = ["Moazam","Khurram","Ali","Saeed","Ahmed","Khattak","Shigri","Tariq","Shahid","Sajid"]
ages = [22,23,24,25,26,27,28,29,30,31]
cities = ["Karachi","Lahore","Islamabad","Peshawar","Quetta","Multan","Faisalabad","Hyderabad","Gujranwala","Sialkot"]


people = []
for i in range(len(names)):
    people.append({
        "name": names[i],
        "age": ages[i],
        "city": cities[i]
    })
   




def create_people(names_list, ages_list, cities_list):
    result = []
    for i in range(len(names_list)):
        result.append({
            "name": names_list[i],
            "age": ages_list[i],
            "city": cities_list[i]
        })
    return result


people_from_function = create_people(names, ages, cities)




print("Indexes of cities:")
i =0
while i <len(cities):
    print(f"Index: {i} , City: {cities[i]}")
    i+=1





print("\nAccessing values from person dictionary:")
for person in people:
    for key in person:
        print(f"Key: {key}, Value: {person[key]}")





for person in people:
    print("Values:", person["name"], person["age"], person["city"])

# print("\nKey and Values from person:")
# for person in people:
#     for key, value in person.items():
#         print(f"Key: {key}, Values: {value}")
