# OTP over SSH

This simple POC shows how you can issue an OTP over SSH. Simply download otp.py and place it somewhere on your SSH box. I chose `/opt/otp/otp.py`. Make sure to `chmod 755 /opt/otp/otp.py`. Now `adduser auth` and set the password to something like `auth`. 

Add the following to the bottom of your `/etc/ssh/sshd_config` followed with `service ssh restart`.

```
Match User auth
        PasswordAuthentication yes
        ForceCommand /usr/bin/python3 /opt/otp/otp.py
```

Now ssh to your box and login with `auth:auth` and you'll be greeted with a prompt:
```
Please enter your email address
>
```

Drop in a properly formatted email address like `bob+alice@example.com` and get your "token":
```
Please enter your email address
> bob+alice@example.com
Secure Login Token: b3bc3090b6178a0b6ece458b51fd834ac15ea999d47cc6e2ee3c351dbdd6a4400338b989ed83d773aa66de6e76e7970f9b16c176c7d73959fc96411fd829190e
Connection to localhost closed.
```

This script is probably not secure and shouldn't be used in a production setting. Pull requests are welcomes if you find a bug, want to add a feature, etc.
