# shoes_inventory

A project created to demonstrate the use of class objects in Python.

## Table of Contents
1. Overview of the Project
2. Installing and Running the Project
3. Usage of the Project
4. Credits

### Overview of the Project

This project was written as part of the HyperionDev University of Edinburgh Online Software Engineering Bootcamp, to demonstrate and practice the use of class objects in Python.

### Installing and Running the Project

The project was written in Python 3.11.0 using the Visual Studio Code IDE version 1.75.0.
You will require Python 3 to run this project in your IDE.

### Usage of the Project

The default datafile for this program is inventory.txt.  You can either proceed with this default datafile or enter the details of a new source datafile.

![Screenshot 2023-02-06 at 14 36 40](https://user-images.githubusercontent.com/124285490/217000594-9cce6f89-4d0a-4be7-925e-f332ea282c3f.png)

![Screenshot 2023-02-06 at 14 37 03](https://user-images.githubusercontent.com/124285490/217000536-0ac76433-7c58-4a9c-bc62-16d829baa3e1.png)

You will then be presented with a menu of options, which can be selected using the appropriate number.

![Screenshot 2023-02-03 at 14 09 25](https://user-images.githubusercontent.com/124285490/216624168-3467c4d3-e8a1-4d7c-b415-d96a56acfde8.png)

Selecting option 1 allows you to add a new shoe to the inventory. The Product Code SKU number has to be in the correct format (SKU plus 5 digits), so the user is only prompted for a number up to 5 digits, and then the program automatically fills the rest of the Product Code.

![Screenshot 2023-02-03 at 14 10 51](https://user-images.githubusercontent.com/124285490/216624627-dabadb62-48cb-403f-b517-48664ddfb793.png)

Option 2 displays a complete list of shoes in the inventory.  If you have used option 1 to add a new shoe, you will see it displayed in this list.

![Screenshot 2023-02-03 at 14 12 23](https://user-images.githubusercontent.com/124285490/216624929-9077e1ee-b869-4c5e-82b7-3f6ad3822ff8.png)

Option 3 enables you to find the shoe with the lowest stock, and restock it for a quantity you determine.  If you use option 2 to show the complete list of shoes after this, you will see the new stock level displayed.

![Screenshot 2023-02-03 at 14 13 42](https://user-images.githubusercontent.com/124285490/216625315-c9ac5e20-98f7-4094-8df5-29f678da5c71.png)

Option 4 allows you to search for a shoe by SKU number (hence the importance of the correct formatting of this data field).

![Screenshot 2023-02-03 at 14 16 11](https://user-images.githubusercontent.com/124285490/216625716-c4d5b9ce-b16b-4e27-9f5d-280b4b3eecff.png)

If should be noted that throughout, the program will check user input and respond appropriately to incorrect input, for example:

![Screenshot 2023-02-03 at 14 16 27](https://user-images.githubusercontent.com/124285490/216625845-239d08e5-76a4-4b71-bb2c-760a253d85b0.png)

Option 5 shows the value of all inventory in stock, both by individual shoe and in total.

![Screenshot 2023-02-03 at 14 18 09](https://user-images.githubusercontent.com/124285490/216626041-23a357e9-c76b-4da3-beff-af2ff1fb03fe.png)

Option 6 allows you to put the highest inventory item on sale.

![Screenshot 2023-02-03 at 14 19 01](https://user-images.githubusercontent.com/124285490/216626237-ef03eef1-51f8-449e-bd8a-01aca229bd44.png)

Option 7 exits the program.

### Credits

The Python code was written by Jonathan Hughes.
The inventory.txt file was provided by HyperionDev as part of the coursework material.
The HyperionDev website is at https://www.hyperiondev.com
