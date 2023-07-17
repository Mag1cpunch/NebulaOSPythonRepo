import xml.etree.ElementTree as ET

def create_interface():
    # Create the root element of the XML document
    root = ET.Element("Interface")

    # Add input fields
    input_section = ET.SubElement(root, "InputFields")
    input_field1 = ET.SubElement(input_section, "InputField")
    input_field1.set("name", "username")
    input_field1.set("type", "text")
    input_field2 = ET.SubElement(input_section, "InputField")
    input_field2.set("name", "password")
    input_field2.set("type", "password")

    # Add buttons
    button_section = ET.SubElement(root, "Buttons")
    button1 = ET.SubElement(button_section, "Button")
    button1.set("name", "submit")
    button2 = ET.SubElement(button_section, "Button")
    button2.set("name", "cancel")

    # Create the XML tree from the root element
    tree = ET.ElementTree(root)

    # Write the XML tree to a file
    tree.write("interface.xml")

# Call the function to create the XML interface
create_interface()
