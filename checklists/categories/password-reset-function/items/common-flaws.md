## Password Reset - Common Flaws

There are some common flaws and tests you should perform, while testing a password reset function.

### Tests

- Check uniqueness of the reset link/code/token. Can the token be guessed?
- How long is the link valid? Does the link expire?
- Are there any fields in the link you can tamper with (e.g. user id)
- Try to guess hidden parameters or remove existing parameters
- Request a second reset link and use the older one
- Append a second email parameter
- Check ratelimiting (e.g. Denial of Service by resetting all accounts)
- Try to bypass email validation:
  - Use carbon copy email
    - `email=victim@mail.com%0a%0dcc:hacker@example.com`
  - use other domain
    - `victim@gmail.com@target.com`
