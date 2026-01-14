---
title: "Pop-Out a box effect in DaVinci Resolve 16"
date: 2019-10-08T04:36:40
slug: "pop-out-a-box-effect-in-davinci-resolve-16"
categories:
  - Ideas
---

[![1508177128_1366318](/img/wp-content/uploads/2019/10/1508177128_1366318-e1570508489301.jpg)](https://www.blackmagicdesign.com/in/products/davinciresolve/) I have been working on some video editing using [DaVinci Resolve 16](https://www.blackmagicdesign.com/in/products/davinciresolve/) for the Tutorial videos I have been posting on YouTube. One of the most used effect in tutorial videos is the pop-out effect (I don't really know the exact name) where a portion of the screen is cut and enlarged while the rest of the screen is darkened to bring the focus to that particular area of the frame.

![chosen-area](/img/wp-content/uploads/2019/10/chosen-area.png)![enlarged](/img/wp-content/uploads/2019/10/enlarged.png)

This is really useful to bring the attention of the user to a particular area on the screen. I have searched the internet and haven't found the right tutorial to do it. Finally after much trial and error I figure out a Fusion graph that will get it done.

![fusion-map.png](/img/wp-content/uploads/2019/10/fusion-map.png)
### Workflow


1. Go to the start of the clip
2. Add a rectangle node (or any shape for that matter)
3. Create a keyframe. Adjust the rectangle to the area to popout
4. Add a transform node between the MediaIn and MediaOut
5. Add a keyframe with default values on the first frame
6. Connect the rectangle as the mask for the Transform Node
7. Add a Color Gain node after the transform and add a keyframe, set Lock the RGB values and set the gain to 0.5
8. Connect the rectangle to the Color Gain and Use the Apply Inverted Mask option on the mask tab in inspector
9. Move to the end of the effect (something like frame 30)
10. Adjust the transform size and position
11. Match the size and position of the rectangle
12. Play, test and adjust for any artifacts.

