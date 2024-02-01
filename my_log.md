# Steps taken by me to get it up and running:
1. Run `make build` as directed in the docs. It will run `docker compose build`
2. Once done we need to install requirements with venv
3. For this I used python 3.8 using
```shell
$ py -3.8 -m venv venv
```
4. Activate virtual env
```shell
$ source venv/bin/activate
```
5. once installed, i had to install zlib because of incompatibility issues with following steps:
```shell
$ brew install zlib
```
5.1. Set following value in the `.zshrc`
```bashrc
export LDFLAGS="-L/opt/homebrew/opt/zlib/lib"
export CPPFLAGS="-I/opt/homebrew/opt/zlib/include"
```
6. I had to make change to the version of pip and pillow for compatibility as:
```shell
$ python -m pip install pip==20.0.2
```
7. Change the pillow version in the `requirements.txt` file as shown below:
```shell
Pillow==6.2.2
```
8. once installed now we can use virtual env
