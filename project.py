# Final Project <Gradetificate>
# Name: Nabila Luthfiyah
# City: Bekasi
# Country: Indonesia
# linkedin : www.linkedin.com/in/nabila-luthfiyah

# About the project:
# this program will make an e-certificate paper by importing a csv files and make it a certificate paper that formatted to pdf files
# user must import a csv files, a choose a templates that given and program will generate it to e-certificate


from fpdf import FPDF
import csv, os, cowsay
from tabulate import tabulate

# wadah template background
templates = None
# wadah template data
data = None

def main():
    while True:
        # menu
        os.system("cls||clear")
        title()

        # pengecekan input value awal
        try:
            choose = int(input("Choose your option: "))
            if choose > 4 or choose < 1:
                print("Invalid Input")

        except ValueError:
            print("Invalid Input")
            input("Press Enter to continue...")
            continue

        # choose certificate template
        if choose == 1:
            os.system("cls||clear")
            print("="*70)
            print("+"," "*22,"Choose Your Template"," "*22,"+")
            print("="*70)
            print("[1] Template Certificate Only")
            print("[2] Template Certificate With Grades")

            try:
                if template_choise(int(input("Choose your option: "))) == True:
                    print("your data imported successfully")
            except FileNotFoundError:
                print("File does not exist")

        # choose the csv file
        elif choose == 2:
            os.system("cls||clear")
            print("="*70)
            print("+"," "*20,"Write Name of The Files"," "*20,"+")
            print("="*70)
            temp_csv = input("link: ")
            try:
                if check_input_csv(temp_csv) == True:
                    print("your data imported successfully")
            except FileNotFoundError:
                print("File does not exist")

        # Built the certificate
        elif choose == 3:
            if templates != None and data != None :
                do = check(templates.image)
                if do == "grade":
                    print(certificate_grades(templates.image, data.data))
                elif do == "certificate":
                    print(certificate_without_grades(templates.image, data.data))
            else:
                print("You must input templates and data first!")

        elif choose == 4:
            this = "Thankyou for using grade generator by @nabilaluth"
            cowsay.cow(this)
            break

        input("\nPress Enter to continue...")
        print("="*70)

def template_choise(input):
    global templates

    if input >= 1 and input <= 2:
        if input == 1:
            templates = Template("without_grades.png")
            return True
        elif input == 2:
            templates = Template("with_grades.png")
            return True

    else:
        print("Invalid Input")

def check(templates):
    if templates == "with_grades.png":
        return "grade"
    elif templates == "without_grades.png":
        return "certificate"

# check input in csv
def check_input_csv(temp):
    global data

    if not temp.endswith(".csv"):
        print("Not a Csv file")
    else:
        with open(temp, "r") as file:
            data = Data(temp)
            reader = csv.reader(file)
            print(tabulate(reader, headers='firstrow', tablefmt='fancy_grid'))
            print("\nyou can edit the data in the csv by edited it directly in your files")
        return True



def certificate_grades(templates, data):
    with open(data, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            id, name, course, grade, date = row[0], row[1], row[2], row[3], row[4]
            pdf = PDF_grade(templates, name, course, grade, id, date)

    return "Certificate is finished"


def certificate_without_grades(templates, data):
    with open(data, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            id, name, course, date = row[0], row[1], row[2], row[4]
            pdf = PDF_nograde(templates, name, course, id, date)

    return "Certificate is finished"

def title():
    global templates
    global data

    print("="*70)
    print("+"," "*20,"WELCOME TO GRADETIFICATE"," "*20,"+")
    print("="*70)

    print(f"Certificate Templates: {templates}")
    print(f"CSV Data: {data}\n")

    print("[1] Upload Certificate Templates")
    print("[2] Upload CSV Data File")
    print("[3] Make the Certificate")
    print("[4] Exit")
    print("="*70)

class Template:
    def __init__(self, image):
        self.image = image

    def __str__(self):
        return self._image

    # getter
    @property
    def image(self):
        return self._image

    # setter
    @image.setter
    def image(self, image):
        if not image:
            raise ValueError("No data")
        self._image = image

class Data:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self._data

    # getter
    @property
    def data(self):
        return self._data

    # setter
    @data.setter
    def data(self, data):
        if not data:
            raise ValueError("No data")
        self._data = data

class PDF_grade(FPDF):
    def __init__(self, templates, name, course, grade, id, date):
        super().__init__()
        self.set_page_background(templates)
        self.add_page(orientation="L", format="A4")
        self.name(name.title())
        self.course(course)
        self.grade(grade)
        self.id(id, date)
        self.output(f"Grade_{name}.pdf")


    def name(self, name):
        self.set_font("helvetica", "", 32)
        self.text(44, 100, name)

    def course(self, course):
        self.set_font("helvetica", "B", 20)
        self.text(42, 125, course)

    def grade(self, grade):
        self.set_font("helvetica", "", 20)
        self.text(42, 160, grade)

    def id(self, id, date):
        self.set_font("helvetica", "", 16)
        self.text(88, 185, id)
        self.set_font("helvetica", "", 12)
        self.text(42,192, f"Verified in {date}")

class PDF_nograde(FPDF):
    def __init__(self, templates, name, course, id, date):
        super().__init__()
        self.set_page_background(templates)
        self.add_page(orientation="L", format="A4")
        self.name(name.title())
        self.course(course)
        self.id(id, date)
        self.output(f"Certificate_{name}.pdf")

    def name(self, name):
        self.set_font("helvetica", "I", 32)
        self.cell(0, 153, name, align="C")

    def course(self, course):
        self.ln(20)
        self.set_font("helvetica", "B", 18)
        self.cell(0, 160, course, align="C")


    def id(self, id, date):
        self.set_font("helvetica", "", 12)
        self.set_text_color(255, 255, 255)
        self.text(240, 6, f"Certificate id: {id}")
        self.text(12, 6, f"Verified in: {date}")

if __name__ == "__main__":
    main()