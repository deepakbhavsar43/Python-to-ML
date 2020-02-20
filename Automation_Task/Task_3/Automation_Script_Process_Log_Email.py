from email import encoders
from email.mime.base import MIMEBase
import psutil
from Secrets import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MyProcess:
    def __init__(self):
        # Total CPU Cores
        self.path = '1rivet/'
        self.filename = "ProcessLog.log"
        print(psutil.cpu_count())

    def running(self):
        # Iterate over all running process
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                processID = proc.pid
                processMemory = proc.memory_info().vms / (1024 * 1024)
                # processMemory = MyProcess.Memory(proc)
                MyProcess.process_log(self, processID, processName, processMemory)
                # print(processID, ' ::: ', processName, ':::', processMemory)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def process_log(self, ID, Name, Memory):
        with open(self.path + self.filename, "a+", encoding='utf-8') as lf:
            lf.write(f"{ID} :: {Name} :: {Memory}\n")

    def send_mail(self):
        cc = 'godaseakshay24@gmail.com'
        bcc = ''
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = 'Sent using script'
        body = """
        Hi,
        
        Here i have attached the process log of my system.
        PFA
        """
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(self.path + self.filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)

        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text_msg = msg.as_string()
        server.sendmail(email, [email, cc, bcc], text_msg)
        server.quit()
        print("ProcessLog mailed successfully.")


if __name__ == "__main__":
    obj1 = MyProcess()
    obj1.running()
    flag = 1
    while flag == 1:
        obj1.send_mail()
