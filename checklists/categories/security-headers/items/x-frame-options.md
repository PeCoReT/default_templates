## X-Frame-Options

The X-Frame-Options HTTP header is a security feature that helps to prevent clickjacking attacks on web pages. It allows web developers to control whether or not their site can be embedded within an iframe on another site. The header can be set to three different values: DENY, SAMEORIGIN, and ALLOW-FROM.

### Tests
- Check for missing `X-Frame-Options` header.
- Use Burp's Clickbandit to build the proof.