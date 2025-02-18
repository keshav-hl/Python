#first home work problem/
dishes = {
    "ramanagara" : "ragi rude",
    "bangluru" : "dosa",
    "kunigal" : "pani puri",
    "magadi" : "biriyani",
    "mysuru" : "mysur pak"
}
dishes["davangere"] = "bene dose"
print(dishes)

dishes["bangluru"] = "masala dose"
print(dishes)

del dishes["kunigal"]
print(dishes)

print(dishes.keys())
print(dishes.values())

#second home work problem/
d = {
    "ff1" : {
        "name" : "pramod",
        "f_sub" : "java",
        "f_dish" : "mude"
    },
    "ff2" : {
        "name" : "shiva",
        "f_sub" : "python",
        "f_dish" : "biryani"
    }
}

print(d)
print(d["ff1"] ["f_dish"])