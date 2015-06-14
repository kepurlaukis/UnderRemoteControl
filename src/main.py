import sys
import usb.core

dev = usb.core.find(find_all=True)

for cfg in dev:
    sys.stdout.write('VendorID: 0x{:04X}, ProductID: 0x{:04X}\r\n'.format(cfg.idVendor, cfg.idProduct))


dev = usb.core.find(idVendor=0x0DF7, idProduct=0x0620)

if dev is None:
    raise ValueError('IrDA is not found')

#sys.stdout.write(str(dev[0]))
#first cfg of device, first insterface with first settings, and first
#endpoint
endpoint = dev[0][(0, 0)][0]
sys.stdout.write(str(endpoint))
