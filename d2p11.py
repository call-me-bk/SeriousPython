import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('bk.bk2000.kb@gmail.com', 'xnhvaltokhnoggsb')
imapObj.select_folder('INBOX', readonly=True)
messages = imapObj.search(['FROM','assistant-noreply@google.com']) 
print("%d messages from our best friend" % len(messages))
for msgid, data in imapObj.fetch(messages, ['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']
    print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))
imapObj.logout()