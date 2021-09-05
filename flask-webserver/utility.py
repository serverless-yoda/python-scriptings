import csv

def save_to_text(data):
    email = data["email"]
    subject=data["subject"]
    message=data["message"]
    with open('database.txt', 'a') as db:
        db.write(f'\n{email},{subject},{message}')

def save_to_csv(data):
    email = data["email"]
    subject=data["subject"]
    message=data["message"]
    with open('database.csv', 'a', newline='') as db:
        writer = csv.writer(db, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email,subject,message])
