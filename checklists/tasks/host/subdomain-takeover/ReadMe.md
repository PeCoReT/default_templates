### Subdomain Takeover
A subdomain takeover is an attack where a subdomain that points to an external resource (e.g. Github, AWS, ...) does not exist anymore.
An attacker can register an account to this subdomain and serve content under the victim's domain.

#### How To Test
- Get CNAME entries which points to third party providers
- Register account at the provider

Get the *CNAME* for the domain:
```bash
dig -t CNAME <domain>
```
