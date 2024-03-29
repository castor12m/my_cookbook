#
# https://easymcp2221.readthedocs.io/en/latest/examples.html
#
# I2C bus scan
#
################################################################

# Very simple I2C scan
import EasyMCP2221

# Connect to MCP2221
mcp = EasyMCP2221.Device()

# Optionally configure GP3 to show I2C bus activity.
mcp.set_pin_function(gp3 = "LED_I2C")

print("Searching...")

for addr in range(0, 0x80):
    try:
        mcp.I2C_read(addr)
        print("I2C slave found at address 0x%02X" % (addr))

    except EasyMCP2221.exceptions.NotAckError:
        pass