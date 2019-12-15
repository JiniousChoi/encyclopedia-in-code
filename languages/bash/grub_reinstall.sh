#Grub 2 typically gets overridden when you install Windows or another Operating System. To make Ubuntu control the boot process, you need Reinstall (Repair/Restore) Grub using a Ubuntu Live CD.

#Mount the partition your Ubuntu Installation is on. If you are not sure which it is, launch GParted (included in the Live CD) and find out. It is usually a EXT4 Partition. Replace the XY with the drive letter, and partition number, for example: sudo mount /dev/sda1 /mnt.

DEVICE="$1"         #/dev/sda
PARTITIONNUMBER="$2"   #2
if [[ -z $1 || -z $2 ]] then
    echo "DEVICE or PARTITIONNUMBER is not specified";
    exit 1;

sudo mount "$DEVICE$PARTITIONNUMBER" /mnt

#Now bind the directories that grub needs access to to detect other operating systems, like so.
sudo mount --bind /dev /mnt/dev &&
sudo mount --bind /dev/pts /mnt/dev/pts &&
sudo mount --bind /proc /mnt/proc &&
sudo mount --bind /sys /mnt/sys

#Now we jump into that using chroot.
sudo chroot /mnt

#Now install, check, and update grub.
#This time you only need to add the drive letter (usually a) to replace X, for example: grub-install /dev/sda, grub-install –recheck /dev/sda.
grub-install $DEVICE
grub-install --recheck $DEVICE
update-grub

#Now grub is back, all that is left is to exit the chrooted system and unmount everything.
exit &&
sudo umount /mnt/sys &&
sudo umount /mnt/proc &&
sudo umount /mnt/dev/pts &&
sudo umount /mnt/dev &&
sudo umount /mnt

#Shut down and turn your computer back on, and you will be met with the default Grub2 screen.
#You may want to update grub or re-install burg however you like it.

#Congratulations, you have just Repaired/Restored/Reinstalled Grub 2 with a Ubuntu Live CD!

#http://howtoubuntu.org/how-to-repair-restore-reinstall-grub-2-with-a-ubuntu-live-cd
