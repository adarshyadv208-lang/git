import requests
loc = input("Location: ")
date = input("Date (YYYY-MM-DD)")

print("Simple python weather appliacation")
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{loc}/{date}"
try:
    response = requests.get(url , params={'key':'LK7AJLDBWZWZWU77G3BEGFCD6'})
    data = response.json()
    print(data)
    print(data['description'])

except:
    print("Invalid response")

