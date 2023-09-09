## Broken Access

Check if the application correctly enforces authorized access to different resources or data. Try accessing resources or features that are restricted to specific roles or permissions assigned to other users. Determine whether the system allows unauthorized access or reveals sensitive information.


###  Test for vertical privilege escalation
* Verify whether users with lower privileges can escalate their access to perform actions restricted to higher-privileged roles. For example, check if a regular user can elevate their role to an administrator and gain unauthorized control over the system.


### Test for horizontal privilege escalation
* Confirm whether users can access resources they should not have access to in their own role but are accessible to others with different roles. For example, ensure that a user in a regular role cannot access sensitive information designated for privileged users only.
* Try to guess parameters like `isAdmin=true`
