# ESP32 Usage using WSL 2

Install usbipd to share USB ports between native windows and WSL
https://github.com/dorssel/usbipd-win

Run

`bash
usbipd wsl list
`

and look for the listed device

Run

`bash
usbipd wsl attach -b <ID> --auto-attach
`
Replace ID with the number of the device from the previous command. For example 3-1
