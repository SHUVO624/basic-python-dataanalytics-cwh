Student = {
    "name": "shuvo",
    "city": "chattagram",
    "company": "meta"
}

print(Student["company"])
# print(Student["namee"]) Get error

print(Student.get("nameee")) # won't get error
print(Student.get("name"))