import xml.etree.ElementTree as ET, time as t

tree = ET.parse('TXDOT_test.xml')
root = tree.getroot()
for c in root.iter('Charge'):
	try:
		print c.tag, c.attrib #c.text
		# t.sleep(1)
	except:
		print "oops"

		# root.remove(c)
	# except KeyError:
		# pass
# tree.write('output_txdot.xml')
tr