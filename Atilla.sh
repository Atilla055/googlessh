sudo apt-get install tmate -y && unset TMUX 
nohup docker run -p 8080:80 dorowu/ubuntu-desktop-lxde-vnc  > /dev/null 2>&1 &
tmate