## Password Reset Token Leak Via Referrer

The HTTP referrer is an optional HTTP header field that identifies the address of the webpage which is linked to the resource being requested.
The referrer request header contains the address of the previous web page from which a link to the currently requested page was followed.

### Test

- Request password reset to your email address
- Click on the password reset link
- Do not change password
- Click any 3rd party websites (e.g. Twitter)
- Intercept the request and check, if the referrer header is leaking password reset token

### Impact

It allows the person who has control of particular site to change the user’s password (CSRF attack), because this person knows reset password token of the user.
