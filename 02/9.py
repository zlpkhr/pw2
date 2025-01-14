from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from my_package.iec62325_451_6_outage_v4_0 import UnavailabilityMarketDocument

# Read XML file
with open('Changes in Actual Availability of Consumption Units [7.1.B].xml', 'r') as f:
    xml_content = f.read()

# Configure parser to handle namespaces
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(config=config)
doc = parser.from_string(xml_content, UnavailabilityMarketDocument)

# Debug print the entire object
from pprint import pprint
print("Full document structure:")
pprint(vars(doc))

print(f"Document ID: {doc.m_rid}")
print(f"Type: {doc.type_value}")
print(f"Start: {doc.unavailability_time_period_time_interval.start}")
print(f"End: {doc.unavailability_time_period_time_interval.end}")

for ts in doc.time_series:
    print(f"\nQuantity: {ts.available_period[0].point[0].quantity}")
    print(f"Unit: {ts.quantity_measure_unit_name}")
    if hasattr(ts, 'reason') and ts.reason:
        print(f"Reason: {ts.reason[0].text}")