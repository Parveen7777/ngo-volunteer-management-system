from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from models.volunteer import Volunteer
from models.event import Event
from models.attendance import Attendance

def generate_pdf_report(output_file="ngo_report.pdf"):
    volunteers = Volunteer.get_all_volunteers()
    events = Event.get_all_events()
    attendance = Attendance.get_attendance_records()

    doc = SimpleDocTemplate(output_file)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>NGO Volunteer Management Report</b>", styles['Title']))

    elements.append(Paragraph(f"Total Volunteers: {len(volunteers)}", styles['Normal']))
    elements.append(Paragraph(f"Total Events: {len(events)}", styles['Normal']))
    elements.append(Paragraph(f"Attendance Records: {len(attendance)}", styles['Normal']))

    elements.append(Paragraph("<b>Volunteer List</b>", styles['Heading2']))

    data = [["ID", "Name", "Email", "Status"]]

    for v in volunteers:
        data.append([
            v['id'],
            v['name'],
            v['email'],
            v['status']
        ])

    table = Table(data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.grey),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige)
    ]))

    elements.append(table)

    doc.build(elements)

    return output_file

if __name__ == "__main__":
    generate_pdf_report()
