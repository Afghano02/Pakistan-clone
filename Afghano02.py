import os, platform
os.system("git pull")
os.system("git pull")
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Qadir import main
    main()
elif bit == '32bit':
    from Qadir32 import main
    main()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
