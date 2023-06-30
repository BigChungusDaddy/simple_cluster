"""This profile allocates 3 nodes and connects them together with 2 links. Have been updated to use Ubuntu 22

Instructions:
Click on any node in the topology and choose the `shell` menu item. When your shell window appears, use `ping` to test the link."""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

NODETYPE = "d710"
NODEIMAGE = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Add a raw PC to the request and give it an interface.
node1 = request.RawPC("node1")
node1.hardware_type = NODETYPE
node1.disk_image = NODEIMAGE
iface1 = node1.addInterface()

# Specify the IPv4 address
iface1.addAddress(pg.IPv4Address("192.168.1.1", "255.255.255.0"))

# Add another raw PC to the request and give it an interface.
node2 = request.RawPC("node2")
node2.hardware_type = NODETYPE
node2.disk_image = NODEIMAGE
iface2 = node2.addInterface()

# Specify the IPv4 address
iface2.addAddress(pg.IPv4Address("192.168.1.2", "255.255.255.0"))

# Add another raw PC to the request and give it an interface.
node3 = request.RawPC("node3")
node3.hardware_type = NODETYPE
node3.disk_image = NODEIMAGE
iface3 = node3.addInterface()

# Specify the IPv4 address
iface3.addAddress(pg.IPv4Address("192.168.1.3", "255.255.255.0"))

link = request.LAN("link")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)