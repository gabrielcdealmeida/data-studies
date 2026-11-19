# Notes: JSON and CSV

## JSON

### What it is
JSON stands for **JavaScript Object Notation**. It is a text format for exchanging data, and one of the most common formats in web APIs, in both directions (client to server and server to client). Typical examples are form submissions and user data.

### Why it is used
- **Readable and beginner friendly**: simple syntax.
- **Easy to use in JavaScript**: the text is converted into an object with one call (`JSON.parse`), because its syntax is close to JS objects.
- **More compact than XML**: the same data with fewer characters, since there are no closing tags.
- **Interoperable**: many languages have built-in functions to read and write it (Python has the `json` module).
- **Widely used** across the industry, especially in APIs.

### Syntax rules
- Data is stored in **key-value pairs**: `"key": value`.
- Pairs are separated by `,`.
- `{ }` defines an **object**; `[ ]` defines an **array**.
- Keys and strings need **double quotes**.
- No comments and no trailing commas.

### Data types
string, number, boolean, null, object and array.

### Example
```json
{
  "name": "Gabriel",
  "age": 24,
  "active": true,
  "skills": ["SQL", "Python", "Git"],
  "address": { "city": "Sao Paulo", "country": "Brazil" }
}
```
An object can have a key that stores an array (`skills`), and objects can contain other objects (`address`). This is called nesting.

## CSV

### What it is
CSV stands for **Comma-Separated Values**. It is a plain text format that represents a table: each line is a row and values are separated by commas. The first line is usually the header.

### Characteristics
- **Very simple**, and easy to create, even in a text editor.
- **Not proprietary**: it opens in Excel, Google Sheets, LibreOffice and others.
- **No data types**: everything is text, and the program that reads it decides what is a number or a date.

### Example
```csv
year,make,model
2021,Ford,Fusion
2019,Hyundai,HB20
```

### Quotes and delimiters
- Values that contain the separator go inside double quotes, so `"2.520,30"` stays as one value instead of two columns.
- The delimiter is not always a comma. In Brazil, Excel often exports CSV with a semicolon (`;`), because the comma is the decimal separator.

## Related terms
- **Parsing**: reading text in a format (JSON, CSV, XML) and turning it into data the program can use.
- **Serialization**: the opposite, turning data into text to save or send.

## Practice
- As an exercise, I created two files (`items.csv` and `items.json`) containing similar information. The JSON file contains two objects with some additional information. I then wrote Python code to read both files and manipulate the extracted data.
- Next, I created a script (`csv_to_json.py`) to practice converting CSV data into JSON format. To accomplish this, I initialized an empty list to store the CSV records as dictionaries, resulting in a list of dictionaries.
- Since all data read from the CSV file is initially treated as strings, I had to convert some values to integers and floats before adding them to the list.
- Finally, using `json.dump()`, I was able to export the list into a new file called `items_from_csv.json`, properly formatted as JSON.
- To practice the reverse conversion, I created a script (json_to_csv.py). First, I initialized an empty list to store the JSON field names extracted from the file.
- Next, using csv.DictWriter() along with the fieldnames list, I was able to create a new file called items_from_json.csv and write the data to it, properly formatted as CSV.