import cgi
import subprocess


class CGIInterfacing:
    def __init__(self):
        self.file_name = None
        self.arguments = None
        self.form = None

    def create_cgi_field(self):
        self.form = cgi.FieldStorage()

    def get_form_data(self):
        self.file_name = self.form.getvalue('filename')
        self.arguments = self.form.getlist('arguments')

    def get_results(self):
        result = subprocess.getoutput(['python', self.file_name] + self.arguments)
        result = result.decode('utf-8').strip('\n')
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<title>CGI Interfacing</title>")
        print("</head>")
        print("<body>")
        print("<h2>The Output of the program is: -</h2>")
        print(f"<h5>{result}</h5>")
        print("</body>")
        print("</html>")
