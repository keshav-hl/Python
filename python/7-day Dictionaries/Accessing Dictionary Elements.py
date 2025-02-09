#normal assinging of the element/
subjects = {
    "kannada" : "first language",
    "english" : "second language",
    "hindi" : "third language"
}
print(subjects)
print(subjects["kannada"])

#and also we can access strings by key world called get()/
print(subjects.get("kannada"))
print(subjects.get("social" , "not found"))
