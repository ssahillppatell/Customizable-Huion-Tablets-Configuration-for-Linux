## Customizable Huion Tablets Configuration for Linux

### Disclaimer
- Tested on Huion HS610
- Inspiration from [1](https://askubuntu.com/questions/500141/huion-h610-tablet), [2](https://askubuntu.com/questions/1000869/how-to-run-the-new-huion-tablets-on-linux)

### Procedure
1. Make a file in `usr/share/X11/xorg.conf.d` named `99-huion[Model Name].conf`. In my case, it is `99-huionHS610.conf`. (You might need super user  priveleges to do so)

2. Add this to your newly made conf file:
```
Section "InputClass"
    Identifier "Huion tablets with Wacom driver"
    MatchUSBID "256c:006d*"
    MatchIsTablet "true"
    MatchDevicePath "/dev/input/event*"
    Driver "wacom"
EndSection
```
'006d' is your product ID. In most cases it will remain the same.

3. Restart X server:
```
sudo systemctl restart display-manager
```

4. Now you should be able to see your tablet added to the xsetwacom list. To ensure that run:
```
xsetwacom --list
```

5. Now we can customize the buttons:  
In my case:  
![Pad Button Names](assets/Pad-Button-Names.png)  

A single button can be customized as follows:
```
xsetwacom --set 'DEVICE NAME' Button NUMBER "key KEYSTROKES"
```
I customized all the 12 buttons for using gimp as follows:
```
xsetwacom --set "HUION Huion Tablet Pad pad" Button 1 "key ["
xsetwacom --set "HUION Huion Tablet Pad pad" Button 2 "key ]"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 3 "key -"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 8 "key shift +"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 9 "key p"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 10 "key shift e"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 11 "key ctrl z"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 12 "key ctrl y"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 13 "key r"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 14 "key e"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 15 "key shift up"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 16 "key shift down"
```

6. Stylus can be customized in the same fashion.