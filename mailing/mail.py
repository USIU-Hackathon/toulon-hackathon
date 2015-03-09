#! /usr/bin/env python

import rethinkdb as r
import sendgrid

sg = sendgrid.SendGridClient('wjuma', 'obamanation2008')


def sendEmail(to, emailHTML):
    message = sendgrid.Mail()
    message.add_to(to)
    message.set_subject('USIU Hackathon')
    message.set_html(emailHTML)
    #message.set_text(body)
    message.set_from('no-reply <no-reply@usiuhackathon.me>')
    status, msg = sg.send(message)


conn = r.connect(host = 'localhost',
                 port = 29019,
                 db = 'hackathon',
                 auth_key = 'hackathon2015')


emailHTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta name="viewport" content="width=device-width" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>USIU-A Hackathon Confirmation</title>
<style>
/* -------------------------------------
        GLOBAL
------------------------------------- */
@import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400|Oswald:300,400,700);

* {
    margin: 0;
    padding: 0;
    font-family: "Open Sans", "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
    font-size: 100%;
    line-height: 1.6;
}

img {
    max-width: 100%;
}

body {
    -webkit-font-smoothing: antialiased;
    -webkit-text-size-adjust: none;
    width: 100%!important;
    height: 100%;
}


/* -------------------------------------
        ELEMENTS
------------------------------------- */

hr {
    border: none;
    border: 1px solid #CCC;
    margin: 1em 0;
}

img {
    height: 48px;
}


a {
    color: #444;
    text-decoration: none;
    border-bottom: 1px solid #FFCB08;
}
a:hover {
    color: #000;
}

.btn-primary {
    text-decoration: none;
    color: #FFF;
    background-color: #00A0E3;
    border: solid #00A0E3;
    border-width: 10px 20px;
    line-height: 2;
    font-weight: bold;
    margin-right: 10px;
    text-align: center;
    cursor: pointer;
    display: inline-block;
    border-radius: 25px;
}
.btn-primary:hover {
    color: #FFF;
    opacity: 0.7;
}

.last {
    margin-bottom: 0;
}

.first {
    margin-top: 0;
}

.padding {
    padding: 10px 0;
}


/* -------------------------------------
        BODY
------------------------------------- */
table.body-wrap {
    width: 100%;
    padding: 20px;
}

table.body-wrap .container {
    border: 1px solid #f0f0f0;
}


/* -------------------------------------
        FOOTER
------------------------------------- */
table.footer-wrap {
    width: 100%;    
    clear: both!important;
}

.footer-wrap .container p {
    font-size: 12px;
    color: #666;
    
}

table.footer-wrap a {
    color: #999;
}


/* -------------------------------------
        TYPOGRAPHY
------------------------------------- */
h1, h2, h3 {
    font-family: "Oswald", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;
    line-height: 1.1;
    margin-bottom: 15px;
    color: #000;
    margin: 40px 0 10px;
    line-height: 1.2;
    font-weight: 200;
}

h1 {
    font-size: 36px;
}
h2 {
    font-size: 28px;
    color: #00A0E3;
}
h3 {
    font-size: 22px;
    margin-top: 22px;
}
h4 {
    color: #888;
}

p, ul, ol {
    margin-bottom: 10px;
    font-weight: normal;
    font-size: 14px;
}

ul li, ol li {
    margin-left: 5px;
    list-style-position: inside;
}

/* ---------------------------------------------------
        RESPONSIVENESS
        Nuke it from orbit. It's the only way to be sure.
------------------------------------------------------ */

/* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
.container {
    display: block!important;
    max-width: 600px!important;
    margin: 0 auto!important; /* makes it centered */
    clear: both!important;
}

/* Set the padding on the td rather than the div for Outlook compatibility */
.body-wrap .container {
    padding: 20px;
}

/* This should also be a block element, so that it will fill 100% of the .container */
.content {
    max-width: 600px;
    margin: 0 auto;
    display: block;
}

/* Let's make sure tables in the content area are 100% wide */
.content table {
    width: 100%;
}

</style>
</head>

<body bgcolor="#f6f6f6">

<!-- body -->
<table class="body-wrap">
    <tr>
        <td></td>
        <td class="container" bgcolor="#FFFFFF">

            <!-- content -->
            <div class="content">
            <table>
                <tr>
                    <td>
                        <img src="https://www.usiuhackathon.me/images/logo_black.png">
                        <hr>

                        <h3>Thank you for registering for the hackathon on the 14th of March 2015.</h3>

                        <br>

                        <p>This is the first event of it&rsquo;s kind in USIU. We&rsquo;re at the beginings of a great new community here so get your friends to register as well!</p>
                        <br>
            
                        <p><center><h3>Give a shout-out to our awesome sponsors: </center></h3></p>
                        <p>
                        <a href="https://twitter.com/rethinkdb">RethinkDB</a>
                        is an open-source distributed database built with love. Enjoy an intuitive query language, 
                        automatically parallelized queries, and simple administration. Table joins and batteries included.
                        </p>

                        <br>

                        <p>
                        <a href="https://www.africastalking.com/">Africa's Talking</a> provides a way for people and companies 
                        across the African continent to connect via SMS messages. They offer bulk SMS, short codes and premium SMS, 
                        USSD, MMS and customized mobile messaging solutions for individuals, businesses and developers.
                        </p>

                        <br>

                        <p>
                        <a href="https://www.kuhustle.com/">Kuhustle</a> is an online tech community work place, 
                        Post a job and get bids to deliver it on time and budget.
                        </p>

                        <br>

                        <h3>In the meantime&hellip;</h3>
                        <p>You can keep up to date by following us on the following networks. We&rsquo;ll be posting updates on there as the hackathon draws near</p>
                        <br>
                        <a href="http://facebook.com/usiuhackathon">USIU-Hackathon Facebook Page</a>
                        <br>
                        <a href="http://github.com/USIU-Hackathon/">USIU-Hackathon Github Page</a>
                        <br>
                        <a href="http://twitter.com/usiuhackathon">USIU-Hackathon Twitter Page</a>
                        <br>
                        <br>
                        <p>Regards,</p>
                        <p>The USIU Hackathon Team</p>
                    </td>
                </tr>
            </table>
            </div>
            <!-- /content -->
            
        </td>
        <td></td>
    </tr>
</table>
<!-- /body -->

</body>
</html>
"""

for doc in r.table('Attendee').run(conn):
    sendEmail(doc['id'], emailHTML)
