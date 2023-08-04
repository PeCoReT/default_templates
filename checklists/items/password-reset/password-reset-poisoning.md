## Password Reset Poisoning

- Trigger the password reset function and intercept the request
- manipulate the host header and observe the content of the mail
- Try to inject other `X-Forwarded-` headers and observe the content of the mail


### References
- https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning