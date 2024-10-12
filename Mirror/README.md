# Screen Mirroring Alfred Workflow

This Alfred workflow automates the process of mirroring your Mac's display to another device, such as an iPad, by interacting with macOS’s **Control Center** using AppleScript. With a simple keyword trigger, you can quickly initiate screen mirroring to your device without manually navigating through the Control Center.

<img width="299" alt="Screenshot 2024-10-12 at 4 05 26 PM" src="https://github.com/user-attachments/assets/67c610d8-ff65-4a8f-8aec-59cce3837dbb">

## Prerequisites

### Requirements:
- **macOS Big Sur (or newer)**: The workflow interacts with the Control Center, which is available starting in macOS Big Sur.
- **Alfred**: Ensure that you have Alfred installed along with the Powerpack, which is required to use workflows.
- **System Events Accessibility**: Make sure that **System Events** has accessibility permissions in **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**.

## Workflow Overview

The workflow uses AppleScript to:
1. Open the macOS Control Center.
2. Navigate to the **Screen Mirroring** section.
3. Select the desired device (e.g., an iPad) to mirror the screen.

### Trigger

- **Keyword**: `mirror`

When you type `mirror` into Alfred, the script will trigger the screen mirroring process to your selected device.

## How to Use the Workflow

1. **Download and Install the Workflow**: Import the workflow into Alfred.
2. **Ensure Accessibility Permissions**: 
   - Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility** 
   - Ensure that Alfred and System Events have the necessary permissions.
3. **Trigger the Workflow**: 
   - Open Alfred (`⌘ + Space`).
   - Type `mirror` and press **Enter**.
   - The script will automatically open the Control Center and start screen mirroring to your iPad or other compatible device.

## Customization

If you need to change the device you're mirroring to (in case you have multiple options), you can:

- Modify the **checkbox** selection in the script (the checkbox index might vary depending on the number of devices available).
- Adjust delays (`delay 0.5`) if your system is faster or slower to respond to UI interactions.

### Example Customization

If you want to mirror to a different device (if it’s the second one in the list), change the line:

```applescript
set myScreen to checkbox 1 of its scroll area 1 of group 1
```

to:

``` applescript
set myScreen to checkbox 2 of its scroll area 1 of group 1
```
