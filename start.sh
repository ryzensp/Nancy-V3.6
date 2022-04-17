echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/cshowl/Nancy-V3.6.git /Nancy-V3.6
cd /Nancy-V3.6
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
