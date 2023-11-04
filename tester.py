## this is the UDP that lets us connect SonicPi with Python

from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 36611)
# Edit params to [70] if just using `play` function on server
sender.send_message('/bpm', [80, 75, 70, 85] )
