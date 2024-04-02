#!/bin/bash
# Setup for MacOS

curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
brew install portaudio
pip install virtualenv
python3 -m venv KenpoDojo
mv main.py KenpoDojo/
mv main2.py KenpoDojo/
mv require.txt KenpoDojo/
mv techniques.txt KenpoDojo/
mv intro.mp3 KenpoDojo/
mv outro.mp3 KenpoDojo/
mv README.md KenpoDojo/
cd KenpoDojo/
pip install -r require.txt