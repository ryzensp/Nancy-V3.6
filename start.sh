echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/Hacker-Jr-TG/Nancy-V3.5.git /Nancy-V3.5
cd /Nancy-V3.5
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
