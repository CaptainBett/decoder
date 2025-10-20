# Secret Message Decoder

This Python script decodes a secret message hidden within a public Google Docs document. The script fetches the document, parses its content to find character and coordinate data, and then reconstructs the message on a grid.

## How it Works

The script is designed to read data from a specific Google Docs URL, where the data is organized in an HTML table. Each row in the table contains a character and its corresponding `x` and `y` coordinates.

### Process Breakdown

1.  **Fetch the Document**: The script sends an HTTP GET request to the specified Google Docs URL to retrieve the HTML content of the page.
2.  **Parse the HTML**: It uses the `BeautifulSoup` library to parse the fetched HTML, making it easy to navigate and extract data from the document's structure.
3.  **Find the Data Table**: The script searches for the `<table>` element within the parsed HTML. This table contains the hidden data.
4.  **Extract Data from Rows**: It iterates through each row (`<tr>`) of the table, skipping the header row. For each row, it extracts the text from the three table cells (`<td>`):
    *   The first cell is the **x-coordinate**.
    *   The second cell is the **character**.
    *   The third cell is the **y-coordinate**.
5.  **Store Character Data**: The extracted character and its coordinates are stored in a list. The script also keeps track of the maximum `x` and `y` values to determine the size of the grid needed to display the message.
6.  **Create the Grid**: A 2D list (a grid) is created based on the maximum `x` and `y` coordinates found. The grid is initially filled with spaces.
7.  **Populate the Grid**: The script iterates through the stored character data and places each character at its correct `(x, y)` position on the grid.
8.  **Print the Decoded Message**: Finally, the script prints each row of the grid, revealing the secret message.
9.  **Error Handling**: The script includes error handling to manage potential issues, such as network problems or if the document format is not as expected.

## How to Run the Script

1.  **Prerequisites**: Make sure you have Python installed. You also need to install the required libraries:
    ```bash
    pip install requests beautifulsoup4
    ```

2.  **Execute the Script**: Run the script from your terminal:
    ```bash
    python decoder.py
    ```

The decoded message will be printed to the console.
