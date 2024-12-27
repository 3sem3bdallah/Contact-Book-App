# UML Documentation

This directory contains the UML diagrams for the Contact Book application.

## Class Diagram

The `class_diagram.puml` file contains the PlantUML representation of the application's class structure. The diagram shows:

1. **Contact Class**
   - Core data structure for storing contact information
   - Implements a linked list node structure

2. **ContactBook Class**
   - Manages the collection of contacts
   - Implements CRUD operations and sorting

3. **ContactBookApp Class**
   - Handles the GUI implementation
   - Manages user interactions and display

### Relationships
- ContactBookApp uses ContactBook for data management
- ContactBook manages Contact objects
- Contact links to other Contact objects in the linked list

To view the diagram, use a PlantUML viewer or online service.