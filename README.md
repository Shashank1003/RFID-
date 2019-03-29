Hardware Connections:

On your RFID RC522 you will notice that there are 8 possible connections on it, these being SDA (Serial Data Signal), SCK (Serial Clock), MOSI (Master Out Slave In), MISO (Master In Slave Out), IRQ (Interrupt Request), GND (Ground Power), RST (Reset-Circuit) and 3.3v (3.3v Power In). you will need to wire all of these except IRQ to your Raspberry Pi’s GPIO pins as shown below:

SDA connects to pin 24

SCK connects to pin 23

MOSI connects to pin 19

MISO connects to pin 21

GND connect to pin 6 (or any other ground pin)

RST connects to pin 22

3.3v connects to pin 1 (or any other 3.3v power pin)

for led and buzzer connections (optional):

blue led connects to pin 3

red led connects to pin 5

buzzer connects to pin 7

Raspbian Part:

Enable SPI from raspberrypi configration>> Interfacing options and then type following commands in terminal window to install essential libraries

sudo pip install spidev

sudo pip install mfrc522


Code:

Use write.py file to assign a name or any specific user code to the id-card.

Use read.py file to add a user to the google-firestore database.

Use authentication.py file to check if user is allowed or not.
