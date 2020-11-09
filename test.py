from core.send import Email

email=Email()
email.setServer("localhost",25)
email.setSubject('hello')
email.setEmailType('html')
email.setContent('<h3>Hello</h3>')
email.addToAddr('user@dev.loc')

#Optional
email.addCcAddr('user1@dev.loc')
email.addCcAddr('user2@dev.loc')
email.addBccAddr('user3@dev.loc')
email.addBccAddr('user4@dev.loc')
email.addAttachment(r'/home/o/Images/42606.jpeg') 

#send mail now
email.send()