> Lost & Found Management System Project Statement Document
>
> Shubham Sharma Registration Number: 25BCG10011
>
> November 23, 2025

1 Problem Statement

In educational institutions, workplaces, and public spaces, lost items
are frequently misplaced and found items often go unclaimed due to the
lack of an organized tracking system. Cur-rently, many organizations
rely on manual registers, physical lost-and-found boxes, or informal
communication channels, which result in:

• Ineficient tracking: No centralized database to record and search for
lost or found items

• Poor communication: Limited ability for owners to check if their lost
items have been found

• Data loss: Paper-based systems are prone to damage, loss, and dificult
to maintain over time

• Time wastage: Manual searching through logs or physical storage areas
is time-consuming

• Low recovery rates: Owners often give up searching, and found items
remain unclaimed

This project addresses these challenges by providing a simple,
command-line based digital system to eficiently manage lost and found
items with persistent storage, search capabilities, and status tracking.

2 Scope of the Project

The Lost & Found Management System is designed to provide core
functionality for tracking lost and found items in a lightweight,
terminal-based application.

2.1 Included in Scope

• Item Registration: Record lost and found items with details (name,
location, contact, notes)

• Data Persistence: Store all records in a JSON file for long-term
retention

• Status Management: Track item status (lost/found/claimed/returned)

• Search Functionality: Search items by name or location

• CRUD Operations: Create, read, update, and delete item records

• Undo Capability: Restore accidentally deleted items

• Unique Identification: Auto-generated ID system for each item

• Timestamp Tracking: Record when each item was reported

2.2 Excluded from Scope

• Web or graphical user interface

• Image upload or storage of item photographs

• User authentication and role-based access control

• Email or SMS notification systems

• Multi-location or distributed system support

• Advanced analytics or reporting dashboards

• Integration with external databases or services

3 Target Users

The system is designed for the following user groups:

1\. Security Personnel & Front Desk Staff

> • Primary operators who record found items
>
> • Update item status when owners claim their belongings • Perform
> searches to help visitors locate their items

2\. Administrative Staff

> • Manage and maintain the lost-and-found database • Edit records to
> correct errors or add information • Generate periodic reviews of
> unclaimed items

3\. Students & Employees

> • Report lost items with detailed descriptions
>
> • Check with staff if their items have been found • Provide contact
> information for notifications

4\. Facility Managers

> • Oversee lost-and-found operations • Review all items in the system
>
> • Make decisions on unclaimed item disposal
>
> 2

4 High-Level Features

4.1 Core Functionality

1\. Item Reporting System

> • Report lost items with description, location, and contact details •
> Register found items for matching with lost item reports
>
> • Capture optional notes for additional item characteristics •
> Automatic timestamp recording for all entries

2\. Viewing & Listing

> • Display all lost items with current status
>
> • Display all found items available for claiming
>
> • Show comprehensive details including ID, item name, location, and
> contact • View combined list of all items in the system

3\. Status Tracking

> • Mark lost items as ”claimed” when recovered by owner
>
> • Mark found items as ”returned” when handed back to owner • Prevent
> duplicate status updates
>
> • Maintain status history through timestamps

4\. Search & Discovery

> • Search across both lost and found items simultaneously • Query by
> item name or location keywords
>
> • Case-insensitive partial matching
>
> • Display results categorized by lost/found status

5\. Data Management

> • Edit existing item records (update description, location, contact) •
> Delete items with confirmation prompts
>
> • Undo last deletion to recover accidentally removed items •
> Persistent JSON storage for data retention

6\. User Interface

> • Interactive menu-driven command-line interface • Clear prompts with
> examples for ease of use
>
> • Confirmation dialogs for critical operations
>
> • Helpful feedback messages and error handling
>
> 3

4.2 Data Structure

Each item record contains:

> • Unique numeric identifier (auto-generated)
>
> • Item name/description
>
> • Specific location where lost or found
>
> • Contact information (optional)
>
> • Additional notes (optional)
>
> • Status (lost, found, claimed, or returned)
>
> • Timestamp of when reported

This Lost & Found Management System provides a practical, easy-to-deploy
solution for or-ganizations seeking to improve their lost item recovery
rates through better organization and searchability.

> 4
