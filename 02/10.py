from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from my_package.iec62325_451_6_outage_v4_0 import UnavailabilityMarketDocument

def format_datetime(dt_str):
    """Convert ISO datetime to more readable format"""
    if not dt_str:
        return "N/A"
    # Remove the 'Z' and split into date and time
    dt = dt_str.replace('Z', '')
    date, time = dt.split('T')
    return f"{date} {time}"

def get_reason_text(reasons):
    """Extract reason text from list of reasons"""
    for reason in reasons:
        if reason.text:
            return reason.text
    return "No reason provided"

def print_outage_report(doc):
    print("\n=== Outage Report ===")
    print(f"\nDocument ID: {doc.m_rid}")
    print(f"Revision: {doc.revision_number}")
    print(f"Created: {format_datetime(doc.created_date_time)}")
    
    print("\nParticipants:")
    print(f"  Sender: {doc.sender_market_participant_m_rid.value} (Role: {doc.sender_market_participant_market_role_type})")
    print(f"  Receiver: {doc.receiver_market_participant_m_rid.value} (Role: {doc.receiver_market_participant_market_role_type})")
    
    print("\nOutage Period:")
    interval = doc.unavailability_time_period_time_interval
    print(f"  Start: {format_datetime(interval.start)}")
    print(f"  End: {format_datetime(interval.end)}")
    
    print("\nTime Series Details:")
    for ts in doc.time_series:
        print(f"\n  Series ID: {ts.m_rid}")
        print(f"  Business Type: {ts.business_type}")
        print(f"  Curve Type: {ts.curve_type}")
        print(f"  Measurement Unit: {ts.quantity_measure_unit_name}")
        
        if ts.asset_registered_resource:
            for asset in ts.asset_registered_resource:
                print(f"  Asset ID: {asset.m_rid.value}")
                if asset.name:
                    print(f"  Asset Name: {asset.name}")
        
        if ts.available_period:
            for period in ts.available_period:
                print("\n  Available Period:")
                print(f"    Start: {format_datetime(period.time_interval.start)}")
                print(f"    End: {format_datetime(period.time_interval.end)}")
                print(f"    Resolution: {period.resolution}")
                for point in period.point:
                    print(f"    Position {point.position}: {point.quantity} {ts.quantity_measure_unit_name}")
        
        if ts.reason:
            print(f"\n  Series Reason: {get_reason_text(ts.reason)}")
    
    if doc.reason:
        print(f"\nDocument Reason: {doc.reason[0].code}")

# Read and parse the XML file
with open('Changes in Actual Availability of Consumption Units [7.1.B].xml', 'r') as f:
    xml_content = f.read()

config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(config=config)
doc = parser.from_string(xml_content, UnavailabilityMarketDocument)

# Generate the report
print_outage_report(doc)