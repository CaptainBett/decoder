# Import necessary libraries
import requests  # For making HTTP requests to fetch the document
from bs4 import BeautifulSoup  # For parsing the HTML content of the document

def decode_secret_message(url: str):
    """
    Decodes a secret message from a public Google Docs URL.

    This function fetches an HTML document from the given URL, parses it to find a
    table containing character and coordinate data, and then reconstructs the
    message on a grid.

    Args:
        url (str): The URL of the public Google Docs document.
    """
    print("Attempting to decode message from url...🥶")
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful (e.g., 404 Not Found)
        response.raise_for_status()
        
        # Parse the HTML content of the document using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Initialize a list to store the character data and variables for grid size
        char_data = []
        x_max = 0
        y_max = 0

        # Find the first 'table' element in the parsed HTML
        table = soup.find('table')
        if not table:
            print("No table found in the document.")
            return

        # Iterate over all table rows ('tr'), skipping the first one (header row)
        for row in table.find_all('tr')[1:]:
            # Find all cells ('td') in the current row
            cells = row.find_all('td')
            # Ensure the row has exactly three cells
            if len(cells) == 3:
                try:
                    # Extract the text from each cell and convert to the correct type
                    x = int(cells[0].get_text(strip=True))
                    char = cells[1].get_text(strip=True)
                    y = int(cells[2].get_text(strip=True))
                    
                    # Append the data as a tuple to the char_data list
                    char_data.append((char, x, y))
                    # Update the maximum x and y values to determine grid size
                    if x > x_max:
                        x_max = x
                    if y > y_max:
                        y_max = y
                except (ValueError, IndexError):
                    # If a row doesn't contain valid data, skip it
                    continue
    
        # If no character data was found, print a message and exit
        if not char_data:
            print("No valid data found in the document. The grid is empty.🤦‍♂️")
            return

        # Determine the width and height of the grid
        grid_width = x_max + 1
        grid_height = y_max + 1

        # Create a 2D list (grid) filled with spaces
        grid = []
        for _ in range(grid_height):
            grid.append([' '] * grid_width)
        
        # Populate the grid with the characters at their respective coordinates
        for char, x, y in char_data:
            if y < grid_height and x < grid_width:
                grid[y][x] = char
        
        # Print the success message and the decoded message
        print("Success✅ Here is your decoded message🥳:\n")
        for row in grid:
            print("".join(row))

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"🚨Error: Could not fetch url. Please check the link. Details: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred😱: {e}")

# The URL of the public Google Docs document containing the secret message
google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"

# Call the function to decode the message
decode_secret_message(google_doc_url)


