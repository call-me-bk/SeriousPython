import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
type(smtpObj)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('katharguppe33@gmail.com','2306-srini')
smtpObj.sendmail('katharguppe33@gmail.com ', 'srinivasks@pes.edu ',r'Subject: \nDear Prof, You seem to love cricket and am therefore send a few crickets\(keech keech\) by courier. Sincerely,keetch...keetck')
smtpObj.quit()