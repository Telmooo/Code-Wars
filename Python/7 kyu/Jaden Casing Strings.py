def toJadenCase(string):
    '''
    Want To Be Just Like Lord Jaden Smith? Let's Start With The Basic
    Capitalize Every Word Is My Only Religion. 
    If You Cant Handle This Kind Of Raw Power And Emotion Please Unfollow Me.
    '''
    words = string.split()
    jaden = ""
    for word in words:
        jaden += word.capitalize() + " "
    return jaden[:-1]
