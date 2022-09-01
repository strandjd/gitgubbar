
Docker through VScode on Windows.

Thanks to The Digital Life, https://github.com/xcad2k/videos/tree/main/docker-python-debugging-vscode

Can´t run docker container natively on windows 10 so use a subsystem; example 
    https://docs.microsoft.com/en-us/windows/wsl/install
    (Recommended Ubuntu 20.04 LTS)

Install Docker from: 
    https://docs.docker.com/desktop/install/windows-install/

Visual Studio code extensions:
    Docker              - Work with Docker through VScode.
    remote - WSL        - Lets you open vscode in WSL/WSL2 through click on green button down left in VScode terminal or through code in terminal: 
            >>> mkdir vscode-example 
            >>> code vscode-example



Put in your app.py.

Press the F1-key and choose 
    "Docker: Add Docker Files to Workspace..."
    Choose your template
    Select your projects main python-file that might be "app.py"
    Choose "No" at add "Include optional Docker Compose files?" 

Use the created "requirements.txt" to store libraries in your desired version, flask applications and request python packages requests. 

Open "TERMINAL" in VScode:
    >>> docker build . # to build this image OR use:
        right click the "Dockerfile" inside Explorer and choose "Build Image..."
    Exit the terminal

In "Terminal":
    >>> docker image list # lets you see the newly built image with same name as the folder you are building from.
    >>> docker run "your image name" # now the docker image should run and be exited if code is built that way.

