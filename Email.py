email=input("Enter a Email address:").strip()
print(email)
if '@' in email:
    # username=email[:email.index("@")]
    # domain=email[email.index("@")+1:]
    username,domain=email.split("@",1)
    print(f"Username is {username} and Domain {domain}")
else:
    print("pls enter a valid email id")