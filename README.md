## Final Project CS50P:  Gradetificate
#### Video Demo:  https://www.youtube.com/watch?v=S2T_81jLUM8
#
## Description
#### I made a auto-generate program for certificate by just import some database. This program will create an e-certificate paper by importing a csv files and make it a certificate paper that formatted to pdf files. User must import a database in csv format, choose a templates that given and program will generate it to e-certificate
#

## Requirements:
Library requirements in this project:
1. FPDF
2. FPDF2
3. Cowsay
4. tabulate

Extensions requirements:
1.  PDF Viewer / PDF Preview

#
## About the Project

1. I created 2 empty global parameter containers to store user input data which contains the choice of image templates (templates), and also the name of the input csv file (data).
    ##
        templates = None
        data = None
    ##
    These variables are created as a global variables and can be used using setters and getters.

    Class template:
    ##
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
    ##
    Class Data:
    ##
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
    ##

2. I use the **definition function** called **title()** for welcome messages, input information, and menu options so that the main function is not hard to see. I rewrote the global variables from the template and data so they can be used.
    ##
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
    ##

3. I created a **main function()** which contains a welcome message, templates and csv file information stored in the current program, and what menu options the user can choose in this program.
    ##
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
    ##
    here you can see I use the while **True** loop at the beginning of the menu to make it easier for users to use this program. I use the try condition to make it easier for the program to check input.

4. In the main function, I also create conditions from the input given at the beginning

    In conditions **choose == 1** we are given a choice of what template we can choose. After that, the program will check function **template_choise** whether the input entered by the user is correct or not
    ##
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
    ##
    In conditions **choose == 2** we check the input whether the file name entered is a **.csv** file and whether the file exists or not
    ##
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
    ##
    In conditions **choose == 3** the program will check the check() function. After that, the program will enter into a suitable state. In that state the program will insert templates files and csv data into the appropriate certificate generator
    ##

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
    ##
    In conditions **choose == 4** the program will print some output by library cowsay and after that end the program
    ##
        elif choose == 4:
            this = "Thankyou for using grade generator by @nabilaluth"
            cowsay.cow(this)
            break

        input("\nPress Enter to continue...")
        print("="*70)
    ##
    I write **input("Press Enter to continue...")** so that the program doesn't immediately clear the display in the terminal because at the beginning of the program I write  **(os.system("cls||clear") )** so that the terminal used by the user looks clean and comfortable to use

5. I created **template_choise(input)** function that can perform conditions from user input in the main function
    ##
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
    ##

6.  I created a **check(templates)** function to do a check before the program does a generator certificate so the templates image is match with the data later
    ##
        def check(templates):
            if templates == "with_grades.png":
                return "grade"
            elif templates == "without_grades.png":
                return "certificate"
    ##

7. I created a 2 function to generate certificates according to the template image that has been filtered in **check(templates)**. After that, the data from csv files will transferred to class for being generated one by one by templates
    ##
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

    ##

8. This is a class to do a pdf generator. this class consists of 2 pieces: **PDF_Grade(FPDF)**, and **PDF_nograde(FPDF)**. The program will automatically enter data into the appropriate class before the program will create an e-certificate
    ##
    Class PDF_grade(FPDF):
    ##
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
    ##
    Class PDF_nograde(FPDF):
    ##
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
    ##