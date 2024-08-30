import pandas as pd
from lxml import etree

def excel_to_xml(excel_file, xml_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Create the root element
    root = etree.Element('root')
    
    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        # Create a new 'record' element for each row
        record = etree.SubElement(root, 'record')
        
        # Iterate through each column in the row
        for col_name in df.columns:
            # Create a sub-element with the column name
            child = etree.SubElement(record, col_name)
            # Set the text content of the sub-element to the cell value
            child.text = str(row[col_name])
    
    # Convert the ElementTree to a string
    xml_data = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8')

    # Write the XML data to the output file
    with open(xml_file, 'wb') as f:
        f.write(xml_data)

    print(f"XML file '{xml_file}' has been created successfully.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python excel_to_xml.py <input_excel_file> <output_xml_file>")
    else:
        excel_file = sys.argv[1]
        xml_file = sys.argv[2]
        excel_to_xml(excel_file, xml_file)

# How the Script Works
# Read Excel File: The script uses pandas to read the Excel file into a DataFrame.
# Create XML Structure: It creates a root XML element and iterates through the DataFrame rows to generate XML sub-elements for each cell.
# Generate XML File: The XML tree is converted to a string and saved to an XML file.
# Instructions to Use the Script
# Place the script in the same directory as your Excel file or provide the full path to the Excel file.
# Run the script using Python, specifying the input Excel file and desired output XML file as arguments.
# Customization Tips
# Change Root Element: Modify etree.Element('root') to your preferred root element name.
# Change Record Tag: Modify etree.SubElement(root, 'record') if you want to use a different tag name for each row.
# Add Attributes: You can add attributes to the elements by setting child.set('attribute_name', 'attribute_value').
