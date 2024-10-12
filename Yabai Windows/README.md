# Yabai Windows Alfred Workflow

[Download the workflow](https://github.com/jjdiazo1/AlfredWorkflows/blob/fd07c815b7c624da76c680563989aa1c21563e14/Yabai%20Windows/Yabai%20Windows.alfredworkflow) 

This Alfred workflow is designed to improve your window management experience using **Yabai**, a tiling window manager for macOS. With this workflow, you can quickly move and organize windows across different spaces (virtual desktops) using simple hotkeys.

<img width="759" alt="YABB" src="https://github.com/user-attachments/assets/6e4c3261-5161-4941-9f39-65c70066a686">

Check out this [video](https://www.youtube.com/watch?v=sFe9BwZ6Q6c) by EffectiveCo
for more info on Yabai or refer to their [GitHub repo](https://github.com/koekeishiya/yabai)

## Prerequisites

### What is Yabai?
[Yabai](https://github.com/koekeishiya/yabai) is a powerful window manager for macOS that enables you to control and manipulate windows on your screen through keyboard shortcuts and scripts. It uses the concept of *spaces* (virtual desktops) and tiling window management to help users quickly and efficiently organize their workspace. 

### Requirements:
- **Yabai** must be installed and configured on your system. Follow the instructions [here](https://github.com/koekeishiya/yabai/wiki/Installing-yabai) to set it up. I also recommend [this tutorial](https://www.josean.com/posts/yabai-setup) by Josean Martinez.
- **Alfred** must be installed along with the Powerpack, which is required to use workflows.
- **Scripting permissions** must be enabled for Alfred to allow it to run the `yabai` commands.

## Workflow Hotkeys

This workflow provides several hotkeys for quickly managing windows and spaces using Yabai commands. Each hotkey runs a specific script to move windows between spaces or perform other Yabai-related actions.

## How to Use

1. Install Yabai and ensure it's running.
2. Download and import the Alfred workflow into Alfred.
3. Use the hotkeys listed above to move windows between spaces or navigate between windows.


### Hotkeys and Commands

You can check them and change them by double clicking the scripts at the right of each command in the alfred workflow editor.

<img width="1782" alt="Screenshot 2024-10-12 at 4 21 01 PM" src="https://github.com/user-attachments/assets/e559bf59-d7cf-4e3e-afce-b1b5fab4daa6">

#### Move Window to Space 1
- **Hotkey**: `Ctrl + Shift + 1`
- **Command**: `yabai -m window --space 1`
  
This moves the currently active window to space 1.

#### Move Window to Space 2
- **Hotkey**: `Ctrl + Shift + 2`
- **Command**: `yabai -m window --space 2`
  
This moves the currently active window to space 2.

#### Move Window to Space 3
- **Hotkey**: `Ctrl + Shift + 3`
- **Command**: `yabai -m window --space 3`
  
This moves the currently active window to space 3.

#### Move Window to Space 4
- **Hotkey**: `Ctrl + Shift + 4`
- **Command**: `yabai -m window --space 4`
  
This moves the currently active window to space 4.

#### Move Window to Space 5
- **Hotkey**: `Ctrl + Shift + 5`
- **Command**: `yabai -m window --space 5`
  
This moves the currently active window to space 5.

#### Move Window to Space 6
- **Hotkey**: `Ctrl + Shift + 6`
- **Command**: `yabai -m window --space 6`
  
This moves the currently active window to space 6.

### Additional Hotkeys for Window Navigation

#### Focus on Previous Window
- **Hotkey**: `Cmd + Q`
- **Command**: `yabai -m window --focus prev`
  
This focuses on the previous window in the current space.

#### Focus on Next Window
- **Hotkey**: `Cmd + W`
- **Command**: `yabai -m window --focus next`
  
This focuses on the next window in the current space.

#### Focus on Window Above
- **Hotkey**: `Cmd + A`
- **Command**: `yabai -m window --focus north`
  
This focuses on the window directly above the current one.

#### Focus on Window Below
- **Hotkey**: `Cmd + S`
- **Command**: `yabai -m window --focus south`
  
This focuses on the window directly below the current one.

#### Focus on Window to the Left
- **Hotkey**: `Cmd + Z`
- **Command**: `yabai -m window --focus west`
  
This focuses on the window to the left of the current one.

#### Focus on Window to the Right
- **Hotkey**: `Cmd + X`
- **Command**: `yabai -m window --focus east`
  
This focuses on the window to the right of the current one.

### Example:
- Press `Ctrl + Shift + 2` to move the currently active window to space 2.
- Press `Cmd + Q` to focus on the previous window in the current space.

## Customization

You can customize the hotkeys and modify the Yabai commands by editing the workflow in Alfred:
- Open Alfred Preferences > Workflows.
- Select the **Yabai Windows** workflow.
- Modify the hotkeys or change the `yabai` commands in the "Run Script" actions.

To see a more complete list of all commands there's [Commands.txt](https://github.com/jjdiazo1/AlfredWorkflows/blob/8eed166a82939b3f251b09900498a384fe8d7cba/Yabai%20Windows/Commands.txt) under this same directory.

## Troubleshooting

If the hotkeys are not working:
- Ensure that Yabai is properly installed and running.
- Verify that scripting permissions are enabled for Alfred in **System Preferences** > **Security & Privacy** > **Privacy** > **Automation**.
- Check Yabai's configuration file (`~/.yabairc`) for any issues.


