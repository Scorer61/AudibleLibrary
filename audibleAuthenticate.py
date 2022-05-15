import audible

USERNAME = input('User: ')
PASSWORD = input('Password: ')
COUNTRY_CODE = 'us'
FILENAME = 'auth/audible_auth.txt'

# Authorize and register in one step
auth = audible.Authenticator.from_login(
    USERNAME,
    PASSWORD,
    locale=COUNTRY_CODE,
    with_username=False
)

# Save credendtials to file
auth.to_file(FILENAME)
