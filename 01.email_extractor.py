text="Contact us at support@xyz.com, help@gmail.com, or sales@shop.net!"
valid_email=[item for item in text.split() if "@" in item and "." in item]
print(valid_email)
