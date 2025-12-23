. setenv
<img width="852" height="185" alt="image" src="https://github.com/user-attachments/assets/1a05a364-5eff-4bba-b9b2-8c08b86c9115" />

sudo apt update
<img width="825" height="337" alt="image" src="https://github.com/user-attachments/assets/104531a4-a2c0-4e3b-8aad-604190426eee" />

sudo apt install -y build-essential clang lld git python3 python3-pip \
                    qtbase5-dev libqt5opengl5-dev libgl1-mesa-dev \
                    libxml2-dev zlib1g-dev
<img width="932" height="577" alt="image" src="https://github.com/user-attachments/assets/3e100f67-7066-4fac-a286-1331a60e77b7" />

https://github.com/inet-framework/inet.git
<img width="932" height="199" alt="image" src="https://github.com/user-attachments/assets/b91f249b-15b4-41b2-ba1e-d2b2b33e8f3b" />

cd inet
git checkout v4.5.4
<img width="932" height="396" alt="image" src="https://github.com/user-attachments/assets/57548ffb-4c19-43ad-aa01-8414e4c0f1cc" />

<img width="940" height="686" alt="image" src="https://github.com/user-attachments/assets/c8ceba11-bd28-4800-977a-45e7ad54362a" />
source setenv
<img width="940" height="76" alt="image" src="https://github.com/user-attachments/assets/e6763e5f-936d-4904-a5b4-b58a5e3adf98" />
echo $INET_ROOT
<img width="940" height="76" alt="image" src="https://github.com/user-attachments/assets/317ace0c-4477-47a1-87fb-c5ef04bac1d1" />
make makefiles
<img width="940" height="76" alt="image" src="https://github.com/user-attachments/assets/1168cede-fcab-4c3b-9a08-4969e117387a" />

make -j$(nproc)
<img width="921" height="903" alt="image" src="https://github.com/user-attachments/assets/35c443c0-657b-4b35-829f-5e0dd56a1a1e" />
cd examples/inet

<img width="926" height="125" alt="image" src="https://github.com/user-attachments/assets/062117ec-ee15-42c6-bad8-172e31803d27" />
