import requests
from bs4 import BeautifulSoup
import os
import pandas

# Get Element by ID

URL = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="date")
#print(results.prettify())

# Finding Job Title
print("Finding Text Started")

URL2 = "https://realpython.github.io/fake-jobs/"
page2 = requests.get(URL2)

soup2 = BeautifulSoup(page2.content, "html.parser")
result2=soup2.find(id="ResultsContainer")

job_elements = result2.find_all("div", class_="card-content")

#Using Pandas for writing in the CSV

#Declare Data Frame

df = pandas.DataFrame()


result =[]

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title is-5")
    print("Job Title is="+title_element.text)
    result.append(title_element.text)
    print()
    print()

    
df["Job Title"]=pandas.Series(result)


df.to_csv('test.csv', index=True)

    

    