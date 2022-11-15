import weakref


calendar = {
    1 : {
        "name" : "January",
        "start": 1 ,
        "end": 31,
        "minus": 0
    },
    2 : {
        "name" : "February",
        "start": 32 ,
        "end": 59 ,
        "minus": 31 
    },
    3 : {
        "name" : "March",
        "start": 60 ,
        "end": 90 ,
        "minus": 59 
    },
    4 : {
        "name" : "April",
        "start": 91 ,
        "end": 120 ,
        "minus": 90 
    },
    5 : {
        "name" : "May",
        "start": 121 ,
        "end": 151 ,
        "minus": 120 
    },
    6 : {
        "name" : "June",
        "start": 152 ,
        "end": 181 ,
        "minus": 160 
    },
    7 : {
        "name" : "July",
        "start": 182 ,
        "end": 212 ,
        "minus": 181 
    },
    8 : {
        "name" : "August",
        "start": 213 ,
        "end": 243 ,
        "minus": 212 
    },
    9 : {
        "name" : "September",
        "start": 244 ,
        "end": 273 ,
        "minus": 243 
    },
    10 : {
        "name" : "October",
        "start": 274 ,
        "end": 304 ,
        "minus": 273 
    },
    11 : {
        "name" : "November",
        "start": 305 ,
        "end": 334 ,
        "minus": 304 
    },
    12 : {
        "name" : "December",
        "start": 335 ,
        "end": 365 ,
        "minus": 334 
    }
}

def findHalfBDay(day):
    while day > 365:
        day -= 365
    print(day)


baseMonth = False
while baseMonth == False:
    monthCheck = input("What is your birth month (1 - 12): ")
    if monthCheck.isnumeric() and int(monthCheck) > 0 and int(monthCheck) <13:
        baseMonth = calendar[int(monthCheck)]
        print(baseMonth)
    else:
        print("\ninvalid input, please try again\n")

baseDay = False
while baseDay == False:
    dayCheck = input("\n\nWhat day of the month is your birth day: ")
    if dayCheck.isnumeric():
        baseDay = calendar[int(dayCheck)]
        print(baseDay)
    else:
        print("\ninvalid input, please try again\n")

while True:
    continue