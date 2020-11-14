# ESLAB_HW5

## Section 1

This part used the button project in the course. The STM32L4 node acts as the GATT server and RPi acts as the GATT peripheral. RPi will receive a signal when we press the button on the STM32L4. Upload the **ble_scan_connect.py** to RPi and **main.cpp** and  **ButtonService.h** to STM32L4. To make them connected, run STM32L4 through MbedOS and run RPi by entering *sudo python ble_scan_connect.py* in terminal.

## Section 2

Instead of recieving a message, RPi will receive a notification when pressing the button. Upload the **ble_scan_connect.py** to RPi and **main.cpp** and  **ButtonService.h** to STM32L4. To make them connected, run STM32L4 through MbedOS and run RPi by entering *sudo python ble_scan_connect.py* in terminal.

## Section 3

When pressing the button once, a digit of my student id will send from STM32L4 to RPi. Press nine times to get the full student id. Upload the **ble_scan_connect.py** to RPi and **main.cpp** and  **ButtonService.h** to STM32L4. To make them connected, run STM32L4 through MbedOS and run RPi by entering *sudo python ble_scan_connect.py* in terminal.
