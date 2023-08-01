
# Install the dependencies
force_reinstall = False

with open('/dev/null', 'w') as devnull:
    import requests, os, time, importlib;

    open('/workspace/mainrunpodA1111.py', 'wb').write(requests.get('https://huggingface.co/datasets/TheLastBen/RNPD/raw/main/Scripts/mainrunpodA1111.py').content)
    os.chdir('/workspace')
    time.sleep(2)
    import mainrunpodA1111;
    importlib.reload(mainrunpodA1111);
    from mainrunpodA1111 import *;
    Deps(force_reinstall)
    
import gradio
gradio.close_all()
time.sleep(2)

User = ""
Password= ""
configf=sd(User, Password, model) if 'model' in locals() else sd(User, Password, "")

cmd = f'python /workspace/sd/stable-diffusion-webui/webui.py {configf}'

with open('/workspace/runsd.sh','w') as f:
    f.write(cmd)
import subprocess
subprocess.run(['chmod','+x','/workspace/runsd.sh'])

print(cmd)
print ('Now, run: sh runsd.sh')