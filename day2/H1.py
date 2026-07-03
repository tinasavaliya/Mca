block_list = ['tina@gmail.com', 'prinsi@gmail.com', 'dhruv@gmail.com', 'atri@gmail.com']

email = 'tina@gmail.com'

if email not in block_list:
    print('its not spam email')
else:
    print("its spam email")