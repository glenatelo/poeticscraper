# Import relevant libraries
import requests
import lxml.html as lh
import pandas as pd

# The mainpage that is to be web-scraped
mainpage_url = "https://www.footballmanagerblog.org/2019/11/fm20-best-players-shortlist-top-300.html"

# Create a handle, page, to handle the contents of the website
page = requests.get(mainpage_url)

# Store contents of the website in doc (helps to declutter and create a succinct shortlist)
doc = lh.fromstring(page.content)

# Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

# Sanity check - see if the entire database is of the same width
# resultant output confirms that all rows have same width
[len(T) for T in tr_elements[:24]]

# Table header - parse first row as main header for the entire shortlist
tr_elements = doc.xpath('//tr')

# Create an empty shortlist (used in the dataframe afterwards)
col = []
i = 0

# For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    # Increments of 1, i.e. i = i + 1
    i+=1
    name=t.text_content()
    # Replacing the placeholders: Resultant output is 'CA', 'PA', 'Name', 'Position', 'Club', 'Nat', 'Age', 'Value' (corresponds to mainpage)
    print('%d:"%s"'%(i,name))
    # Information is stored in a list of tuples due to its efficiency
    col.append((name,[]))

# Since first row (row no. 0) is the header, data is stored from the second row (row no. 1) onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]

    # i is the index of the shortlist's column
    i=0

    # Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content()
        # Check if row is empty
        if i>0:
        # Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        # Append the data to the empty list of the i'th column
        col[i][1].append(data)
        # Increment i for the next column
        i+=1

[len(C) for (title,C) in col]

# Create the dataframe
Dict={title:column for (title,column) in col}

# Due to the irregular length of the arrays (some of the widths != "16"), this troubleshooting method is required
df = pd.DataFrame.from_dict(Dict, orient='index')

# The (resolved) outcome
df.transpose()

# Save the DataFrame to CSV; r is used to convert a normal string into a raw string
df.to_csv(r'C:\Users\ffree\Documents\python_work\telegram.bot\export_scrapeFM1.csv', index = False, header=True)
