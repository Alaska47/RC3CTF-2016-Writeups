#200 - Graphic Design
>Problem description here

#Solution
We are giving an `.obj` file which is a 3D Object file. Opening it up in any 3D modeling software reveals a model of a stegosaurus. Thinking that this may be a hint towards stegonography, I tried to binwalk it. However, this revealed to be quite misleading as the `.cpio` files revealed from the binwalk command were just the coordinates for the 3D model.

![stego1.png]()

Looking at the 3D model, I started playing around with it. Its mouth was open, so I decided to try zooming in on its mouth to see if I could get inside. Suprisingly, there was some text inside the model! Playing with the zoom settings and maneuvering around reveals the entire flag.

![flag.png]()

#Flag


