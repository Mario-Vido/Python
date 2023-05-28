from bs4 import BeautifulSoup

# Read the HTML file
with open('Formulár bez názvu.html', 'r') as f:
    html_data = f.read()

# Parse the HTML data using BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Print the pretty version of the HTML
print(soup.prettify())