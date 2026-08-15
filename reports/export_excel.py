from openpyxl import Workbook
from models.event import Event

def export_events_excel(filename="events.xlsx"):
    events = Event.get_all_events()

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Events"

    headers = [
        "ID",
        "Title",
        "Date",
        "Location",
        "Required Volunteers",
        "Status"
    ]

    sheet.append(headers)

    for event in events:
        sheet.append([
            event['id'],
            event['title'],
            event['event_date'],
            event['location'],
            event['required_volunteers'],
            event['status']
        ])

    workbook.save(filename)

    return filename

if __name__ == "__main__":
    export_events_excel()
