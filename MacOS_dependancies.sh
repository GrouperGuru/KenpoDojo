#!/bin/bash
# Setup for MacOS

curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
brew install portaudio
pip install virtualenv
python3 -m venv KenpoDojo
mv main.py KenpoDojo/
mv require.txt KenpoDojo/
mv techniques.txt KenpoDojo/
cd KenpoDojo/
pip install -r require.txt