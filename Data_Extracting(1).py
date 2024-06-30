# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd


# # data = []
# # for i in range(1,4):
# #     url = r'https://results.eci.gov.in/AcResultGenJune2024/statewiseS01'+str(i)+'.htm'
# # # Fetch the page
# #     response = requests.get(url)
# #     response.raise_for_status()  # Check for HTTP issues
    
# #     # Parse the HTML, ensuring the correct encoding is used
# #     soup = BeautifulSoup(response.content, 'html.parser', from_encoding=response.encoding)
    
 
    
# #     # Data extraction from the table
    
# #     for row in table.find_all('tr')[1:]:  # Skip header row
# #         cols = row.find_all('td')
# #         if len(cols) >= 28 :  # Ensure all columns are present
# #             data.append({
# #                 'Constituency': cols[0].text.strip(),
# #                 'Const. No.': cols[1].text.strip(),
# #                 'Leading Candidate': cols[2].text.strip(),
# #                 'Leading Party': cols[3].text.strip(),
# #                 'Trailing Candidate': cols[5].text.strip(),
# #                 'Trailing Party': cols[6].text.strip(),
# #                 'Margin': cols[8].text.strip(),
# #                 'Round': cols[9].text.strip(),
# #                 'Status': cols[0].text.strip()
# #             })

# # # Create a DataFrame
# # df = pd.DataFrame(data)
# # df.to_csv('election_results_Andra_Pradesh.csv', index=False)

# # print('Data has been extracted and saved to election_results.csv')


# --------------------------------------------



# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# data = []
# for i in range(1, 10):
#     url = r'https://results.eci.gov.in/AcResultGenJune2024/statewiseS01' + str(i) + '.htm'
#     # Fetch the page
#     response = requests.get(url)
#     response.raise_for_status()  # Check for HTTP issues
    
#     # Parse the HTML, ensuring the correct encoding is used
#     soup = BeautifulSoup(response.content, 'html.parser', from_encoding=response.encoding)
    
#     # Find the table in the parsed HTML
#     table = soup.find('table', {'class': 'table table-striped table-bordered'})  # Adjust the class or other attributes as needed
    
#     # Data extraction from the table
#     if table:
#         for row in table.find_all('tr')[0:]:  # Skip header row
#             # cols = row.find_all('td')
#             cols = row.select(':scope > td')
#             if len(cols) >= 9:  # Ensure all columns are present
#                 data.append({
#                     'Constituency': cols[0].text.strip(),
#                     'Const. No.': cols[1].text.strip(),
#                     'Leading Candidate': cols[2].text.strip(),
#                     'Leading Party': cols[3].text.strip(),
#                     'Trailing Candidate': cols[4].text.strip(),
#                     'Trailing Party': cols[5].text.strip(),
#                     'Margin': cols[6].text.strip(),
#                     'Round': cols[7].text.strip(),
#                     'Status': cols[8].text.strip()
#                 })

# # Create a DataFrame
# df = pd.DataFrame(data)
# df.to_csv('election_results_Andhra_Pradesh.csv', index=False)

# print('Data has been extracted and saved to election_results_Andhra_Pradesh.csv')


# --------------------------------------



import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for i in range(1, 3):
    url = r'PASTE YOUR URL :)' + str(i) + '.htm'
    # Fetch the page
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP issues
    
    # Parse the HTML, ensuring the correct encoding is used
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding=response.encoding)
    
    # Find the table in the parsed HTML
    table = soup.find('table', {'class': 'table table-striped table-bordered'})  # Adjust the class or other attributes as needed
    
    # Data extraction from the table
    if table:
        for row in table.find_all('tr')[1:]:  # Skip header row
            cols = row.select(':scope > td')
            if len(cols) >= 9:  # Ensure all columns are present
                # Remove span elements with the class 'tooltip-icon' from the relevant columns
                for span in cols[3].find_all('div', {'class': 'tooltip'}):
                    span.decompose()
                for span in cols[5].find_all('div', {'class': 'tooltip'}):
                    span.decompose()
                
                data.append({
                    'Constituency': cols[0].text.strip(),
                    'Const. No.': cols[1].text.strip(),
                    'Leading Candidate': cols[2].text.strip(),
                    'Leading Party': cols[3].text.strip(),
                    'Trailing Candidate': cols[4].text.strip(),
                    'Trailing Party': cols[5].text.strip(),
                    'Margin': cols[6].text.strip(),
                    'Round': cols[7].text.strip(),
                    'Status': cols[8].text.strip()
                })

# Create a DataFrame
df = pd.DataFrame(data)
df.to_csv('election_results_Arunachal_Pradesh.csv', index=False)

print('Data has been extracted and saved to election_results_Arunachal_Pradesh.csv')
