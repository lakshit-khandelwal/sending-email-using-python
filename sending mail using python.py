import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("lakshitkhandelwal91@gmail.com","khandelwal2000")
subject="sending email using python"
body="Hi , My name is lakshit and this is a email sending program using python "
message="Subject:{}\n\n{}".format(subject,body)
# print(message)
listofaddress=["........"]

ob.sendmail("lakshitkhandelwal91",listofaddress,message)
print("send successfully......")
ob.quit()
