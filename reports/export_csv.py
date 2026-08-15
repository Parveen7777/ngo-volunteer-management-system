import csv
from models.volunteer import Volunteer

def export_volunteers_csv(filename="volunteers.csv"):
    volunteers = Volunteer.get_all_volunteers()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Name",
            "Email",
            "Phone",
            "Skills",
            "Status"
        ])

        for v in volunteers:
            writer.writerow([
                v['id'],
                v['name'],
                v['email'],
                v['phone'],
                v['skills'],
                v['status']
            ])

    return filename

if __name__ == "__main__":
    export_volunteers_csv()
