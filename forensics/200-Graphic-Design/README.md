#200 - Graphic Design
>Problem description here

#Solution
We are giving an `.obj` file which is a 3D Object file. Opening it up in any 3D modeling software reveals a model of a stegosaurus. Thinking that this may be a hint towards stegonography, I tried to binwalk it. However, this revealed to be quite misleading as the `.cpio` files revealed from the binwalk command were just the coordinates for the 3D model.

![stego1.png]()

At first, I was using a random 3D modelling software that I found on the Windows Store with 0 additional features. Finding "3D Builder" useless, I decided to switch to a more featured 3D modelling software, [Open 3D Model Viewer](http://www.open3mod.com/). After opening it in that software, I found some text inside the dinosaur. Zooming in more closely revealed the flag shown below.

![flag.png]()

#Flag
RC3-2016-St3GG3rz

