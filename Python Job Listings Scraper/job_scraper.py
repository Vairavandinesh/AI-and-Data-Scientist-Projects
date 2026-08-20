import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_data = []

for job in jobs:

    title_element = job.find("h2", class_="title")
    company_element = job.find("h3", class_="company")
    location_element = job.find("p", class_="location")
    link = job.find("a")

    title = title_element.text.strip() if title_element else "N/A"
    company = company_element.text.strip() if company_element else "N/A"
    location = location_element.text.strip() if location_element else "N/A"
    job_url = link.get("href", "N/A") if link else "N/A"

    job_data.append({
        "title": title,
        "company": company,
        "location": location,
        "url": job_url
    })

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["title", "company", "location", "url"]
    )

    writer.writeheader()
    writer.writerows(job_data)

print(f"Scraped {len(job_data)} jobs.")
print("Data saved to jobs.csv")