# Calendar Jump Alfred Workflow (Days)

[Download the workflow](#) 

This Alfred workflow allows you to quickly jump to a specific day in the Calendar app, based on your input. You simply type a day of the week (e.g., "Monday", "Tuesday") and Alfred will open the Calendar app on that specific day.

> Query

<img width="646" alt="Screenshot 2024-10-12 at 4 47 51 PM" src="https://github.com/user-attachments/assets/b66d2dd4-74c2-483b-9705-efacfed5e979">

> Result

<img width="751" alt="Screenshot 2024-10-12 at 4 53 10 PM" src="https://github.com/user-attachments/assets/af760b6f-dccc-459a-b2b1-c7b858b382f9">

## Prerequisites

### Requirements:
- **macOS**: Ensure you have macOS and the Calendar app installed.
- **Alfred**: Ensure that you have Alfred installed along with the Powerpack, which is required to use workflows.
- **System Events Accessibility**: Make sure that **System Events** has accessibility permissions in **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**.

## Workflow Overview

The workflow uses AppleScript to:
1. Detect the current day.
2. Calculate how many days away the requested day is (e.g., Monday, Tuesday, etc.).
3. Open the Calendar app and display that specific day.

### Trigger

- **Keyword**: `monday`, `tuesday`, etc.

When you type a day of the week into Alfred, the script will open the Calendar app and display that day.

## How to Use the Workflow

1. **Download and Install the Workflow**: Import the workflow into Alfred.
2. **Ensure Accessibility Permissions**: 
   - Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**.
   - Ensure that Alfred and System Events have the necessary permissions.
3. **Trigger the Workflow**: 
   - Open Alfred (`⌘ + Space`).
   - Type a day of the week (e.g., "Monday") and press **Enter**.
   - The script will automatically open the Calendar app and show the requested day.

## Customization

If you need to modify the AppleScript to adjust which view or calendar opens by default (e.g., month view or specific calendars), you can tweak the script to fit your preferences.

